from pathlib import Path
from typing import Dict, Any, List
import pdfrw
from django.conf import settings


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
                        value = str(input_dict[mapped])
                        # annotation['/V'] = value
                        annotation.update(pdfrw.PdfDict(V=value))
                        self.template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))

    def save(self, path: Path):
        pdfrw.PdfWriter().write(str(path), self.template_pdf)


class LeasePdf(PdfFile):
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
