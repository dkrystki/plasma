from pathlib import Path
from typing import Dict, Any, List
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, TextStringObject, NumberObject, BooleanObject, IndirectObject
from PyPDF2.pdf import PageObject
from django.conf import settings


class PdfFile:
    mapping: List[Dict[str, Any]]

    def _set_appearances_to_reader(self, reader: PdfFileReader) -> None:
        if "/AcroForm" in reader.trailer["/Root"]:
            reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)}
            )

    def _set_appearances_to_writer(self, writer: PdfFileWriter) -> None:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)

    def __init__(self, template_path: Path, signature_path: Path) -> None:
        self.template_path = template_path
        self.signature_path = signature_path
        self.pages: List[PageObject] = []

        self.input_pdf = PdfFileReader(str(self.template_path), strict=False)

        self._set_appearances_to_reader(self.input_pdf)

        self.pdf = PdfFileWriter()
        self._set_appearances_to_writer(self.pdf)

    def fill(self, input_dict: Dict[str, Any]) -> None:
        for p, m in zip(self.input_pdf.pages, self.mapping):
            if "/Annots" not in p:
                self.pdf.addPage(p)
                continue
            for j in range(0, len(p['/Annots'])):
                writer_annot = p['/Annots'][j].getObject()
                writer_annot.update({
                    NameObject("/Ff"): NumberObject(1)  # make ReadOnly
                })

                for mk, mv, in m.items():
                    if writer_annot.get('/T') == mk:
                        input_value: Any = input_dict[mv]
                        value: str
                        if type(input_value) == bool:
                            if input_value:
                                writer_annot.update({
                                    NameObject("/V"): NameObject("/1"),
                                    NameObject("/AS"): NameObject("/1"),
                                })
                            else:
                                if '/V' in writer_annot:
                                    del writer_annot['/V']
                                writer_annot.update({
                                    NameObject("/AS"): NameObject("/Off"),
                                })
                        else:
                            value = str(input_value)
                            writer_annot.update({
                                NameObject("/V"): TextStringObject(value),
                                NameObject("/AP"): TextStringObject(value),
                            })

            self.pdf.addPage(p)

    def save(self, path: Path):
        with open(str(path), 'wb') as f:
            self.pdf.write(f)

        self._add_signature(path)

    def _add_signature(self, path: Path):
        template = PdfFileReader(str(path), strict=False)
        self._set_appearances_to_reader(template)

        signature = PdfFileReader(str(self.signature_path), strict=False)
        self._set_appearances_to_reader(signature)

        output = PdfFileWriter()
        self._set_appearances_to_writer(output)

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            watermark = signature .getPage(i)

            page.mergePage(watermark)
            output.addPage(page)

        with open(str(path), 'wb') as f:
            output.write(f)


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
        super(LeasePdf, self).__init__(template_path=settings.BASE_DIR / "tenants/templates/lease.pdf",
                                       signature_path=settings.BASE_DIR / "tenants/templates/lease-signature.pdf")


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
        },
        {}
    ]

    def __init__(self) -> None:
        super(EntryNoticePdf, self).__init__(
            template_path=settings.BASE_DIR / "tenants/templates/entry-notice-form.pdf",
            signature_path=settings.BASE_DIR / "tenants/templates/entry-notice-form-signature.pdf")
