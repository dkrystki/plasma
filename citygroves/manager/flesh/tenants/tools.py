from datetime import date, datetime
from pathlib import Path
from typing import Dict, Any, List
import pdfrw
from django.conf import settings
from pdfrw import PdfName, PdfString


class PdfFile:
    mapping: List[Dict[str, Any]]

    def __init__(self, path: Path) -> None:
        self._path = path
        self.template_pdf = pdfrw.PdfReader(path)

    def fill(self, input_dict: Dict[str, Any]) -> None:
        for page_n, page in enumerate(self.template_pdf.pages):
            annotations = page["/Annots"]
            if not annotations:
                continue
            for annotation in annotations:
                if annotation["/Subtype"] == "/Widget":
                    key = annotation["/T"][1:-1]
                    if key in self.mapping[page_n].keys():
                        mapped = self.mapping[page_n][key]
                        input_value: Any = input_dict[mapped]
                        if type(input_value) in (str, int, float, date, datetime):
                            value = str(input_value)
                            annotation.update(pdfrw.PdfDict(AS=PdfName(value), V=PdfName(value)))
                        elif type(input_value) == bool:
                            value = "1" if input_value else "Off"
                            annotation.update(pdfrw.PdfDict(AS=PdfName(value), V=PdfName(value)))

                        self.template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))

    def save(self, path: Path):
        pdfrw.PdfWriter().write(str(path), self.template_pdf)


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
    ]

    def __init__(self) -> None:
        super(EntryNoticePdf, self).__init__(settings.BASE_DIR / "tenants/templates/entry-notice-form.pdf")
