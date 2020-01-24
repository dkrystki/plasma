from datetime import date, datetime
from pathlib import Path
from typing import Dict, Any, List
import pdfrw
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, BooleanObject, IndirectObject, TextStringObject, NumberObject
from PyPDF2.pdf import PageObject
from django.conf import settings
from pdfrw import PdfName, PdfString


class PdfFile:
    mapping: List[Dict[str, Any]]

    def __init__(self, path: Path) -> None:
        self.path = path
        self.pages: List[PageObject] = []

        self.input_pdf = PdfFileReader(str(self.path), strict=False)

        if "/AcroForm" in self.input_pdf.trailer["/Root"]:
            self.input_pdf.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)}
            )

        self.pdf = PdfFileWriter()
        catalog = self.pdf._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            self.pdf._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(self.pdf._objects), 0, self.pdf)})

        need_appearances = NameObject("/NeedAppearances")
        self.pdf._root_object["/AcroForm"][need_appearances] = BooleanObject(True)

    def fill(self, input_dict: Dict[str, Any]) -> None:
        for p, m in zip(self.input_pdf.pages, self.mapping):
            if "/Annots" not in p:
                continue
            for j in range(0, len(p['/Annots'])):
                writer_annot = p['/Annots'][j].getObject()
                a = 1
                #                 writer_annot.update({
                #                     NameObject("/Ff"): NumberObject(1)  # make ReadOnly
                #                 })

                for mk, mv, in m.items():
                    if writer_annot.get('/T') == mk:
                        # if mv != "signature":
                        #     writer_annot.update({
                        #         NameObject("/Ff"): NumberObject(1)  # make ReadOnly
                        #     })
                        input_value: Any = input_dict[mv]
                        value: str
                        if type(input_value) == bool:
                            value = "/1" if input_value else "Off"
                            # writer_annot.update({
                            #     NameObject("/V"): NameObject(value),
                            #     NameObject("/AS"): NameObject(value)
                            # })
                        else:
                            value = str(input_value)
                            writer_annot.update({
                                NameObject("/V"): TextStringObject(value),
                                NameObject("/AP"): TextStringObject(value),
                                # NameObject("/DA"): TextStringObject("/ArialMT 11 Tf 0 g"),
                            })

            self.pdf.addPage(p)

    def save(self, path: Path):
        with open(str(path), 'wb') as f:
            self.pdf.write(f)


class LeasePdf(PdfFile):
    # Input dictionary to pdf fields mapping
    # Each of list elements is responsible for mapping elements on the corresponding pdf page
    mapping: List[Dict[str, Any]] = [
        {
            "TextField[5]": "person.full_name",
            "TextField[6]": "person.phone",
            "TextField[7]": "person.email",
            "TextField[29]": "unit_address",
            "TextField[31]": "room.number",
        },
        {
            "Date[1]": "starting_on",
            "Date[0]": "ending_on",
            "TextField[0]": "rent",
            "TextField[5]": "payment_reference",
            "TextField[17]": "bond_amount",
        },
        {}, {}, {}, {}, {}
    ]

    def __init__(self) -> None:
        super(LeasePdf, self).__init__(settings.BASE_DIR / "tenants/templates/lease.pdf")


class EntryNoticePdf(PdfFile):
    mapping: List[Dict[str, Any]] = [
        {
            "TextField[0]": "room_number",
            "TextField[1]": "unit_number",
            "TextField[6]": "person1.full_name",
            "TextField[7]": "person2.full_name",
            "TextField[8]": "manager.name",
            "TextField[9]": "details",
            "TextField[10]": "issued_on_day_name",
            "TextField[11]": "method_of_issue",
            "Date[0]": "issued_on",
            "TextField[12]": "planned_on_day_name",
            "Date[1]": "planned_on",
            "TextField[13]": "planned_time",
            "Date[2]": "issued_on",
            "CheckBox[2]": "is_inspection",
            "CheckBox[3]": "is_cleaning",
            "CheckBox[4]": "is_repairs_or_maintenance",
            "CheckBox[5]": "is_pest_control",
            "CheckBox[6]": "is_showing_to_buyer",
            "CheckBox[7]": "is_valutation",
            "CheckBox[8]": "is_fire_and_rescue",
            "TextField[14]": "signature",
        },
    ]

    def __init__(self) -> None:
        super(EntryNoticePdf, self).__init__(settings.BASE_DIR / "tenants/templates/entry-notice-form.pdf")
