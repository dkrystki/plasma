import pytest

from tenants.bin import import_from_propertytree
from tenants.models import Person, Tenant


@pytest.mark.django_db
def test_import_from_propertytree(create_rooms, data_dir):
    importer = import_from_propertytree.Importer(data_dir / "tenants_propertytree.csv")
    importer.start()

    assert Person.objects.get(first_name="Dang").middle_names == "Vu Anh"

    assert Person.objects.get(first_name="Hui").email == "leehuijing25@yahoo.com"
    assert Person.objects.get(first_name="Tze").email == "ctxin96@gmail.com"

    assert Person.objects.all().count() == 70
    assert Tenant.objects.all().count() == 65
