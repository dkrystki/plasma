from typing import Any, Dict

from rest_framework import serializers

from housing.models import Room
from housing.serializer import RoomSerializer
from tenants.models import Address, Application, EntryNotice, Person, Referrer, Tenant


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class EntryNoticeSerializer(serializers.ModelSerializer):
    tenant = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tenant.objects.all())
    str_repr = serializers.ReadOnlyField(source="__str__")

    class Meta:
        model = EntryNotice
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    people = PersonSerializer(many=True)
    room = RoomSerializer(read_only=True)
    str_repr = serializers.ReadOnlyField(source="__str__")
    room_number = serializers.IntegerField(write_only=True)
    unit_number = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tenant
        fields = "__all__"

    def create(self, validated_data) -> Referrer:
        person = Person.objects.create(**validated_data.pop("person"))
        room_number = validated_data.pop("room_number")
        unit_number = validated_data.pop("unit_number")
        room = Room.objects.get(unit__number=unit_number, number=room_number)

        referrer = Tenant.objects.create(person=person, applicant=room, **validated_data)
        return referrer

    def update(self, instance: Referrer, validated_data):
        unit_number: int = instance.room.unit.number
        room_number: int = instance.room.number

        if "room_number" in validated_data:
            room_number = validated_data.pop("room_number")

        if "unit_number" in validated_data:
            unit_number = validated_data.pop("unit_number")

        if "people" in validated_data:
            serializer = PersonSerializer(data=validated_data.pop("people"), partial=True, many=True)
            serializer.is_valid(raise_exception=True)

            pd: Dict[str, Any]
            for pd, p in zip(serializer.validated_data, instance.people.all()):
                for field, value in pd.items():
                    setattr(p, field, value)
                p.save()

        room = Room.objects.get(unit__number=unit_number, number=room_number)
        instance.room = room

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        return instance


class ReferrerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    applicant = serializers.PrimaryKeyRelatedField(required=False, queryset=Person.objects.all())

    class Meta:
        model = Referrer
        fields = "__all__"

    def create(self, validated_data) -> Referrer:
        address = Address.objects.create(**validated_data.pop("address"))
        applicant = validated_data.pop("applicant")
        referrer = Referrer.objects.create(address=address, applicant=applicant, **validated_data)
        return referrer

    def update(self, instance: Referrer, validated_data):
        if "address" in validated_data:
            for field, value in validated_data.pop("address").items():
                setattr(instance.address, field, value)
            instance.address.save()

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        return instance


class ApplicationSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    current_address = AddressSerializer()
    referrers = ReferrerSerializer(many=True)
    room = RoomSerializer(read_only=True)
    room_number = serializers.IntegerField(write_only=True)
    unit_number = serializers.IntegerField(write_only=True)

    class Meta:
        model = Application
        fields = [
            "id",
            "room_number",
            "room",
            "unit_number",
            "person",
            "room",
            "current_address",
            "number_of_ppl_to_move_in",
            "move_in_date",
            "guarantor_will_pay",
            "centerlink_will_pay",
            "is_employed",
            "have_sufficient_funds",
            "is_local_student",
            "is_international_student",
            "is_young_professional",
            "referrers",
            "digital_signature",
        ]

    def update(self, instance: Application, validated_data):
        unit_number: int = instance.room.unit.number
        room_number: int = instance.room.number

        if "room_number" in validated_data:
            room_number = validated_data.pop("room_number")

        if "unit_number" in validated_data:
            unit_number = validated_data.pop("unit_number")

        if "person" in validated_data:
            for field, value in validated_data.pop("person").items():
                setattr(instance.person, field, value)
            instance.person.save()

        if "current_address" in validated_data:
            for field, value in validated_data.pop("current_address").items():
                setattr(instance.current_address, field, value)
            instance.current_address.save()

        if "referrers" in validated_data:
            referrers_data = validated_data.pop("referrers")

            for i, r in enumerate(instance.referrers.all()):
                r_data = referrers_data[i]
                if "address" in r_data:
                    for field, value in r_data.pop("address").items():
                        setattr(r.address, field, value)
                    r.address.save()

                for field, value in r_data.items():
                    setattr(r, field, value)
                r.save()

        room = Room.objects.get(unit__number=unit_number, number=room_number)
        instance.room = room

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance

    def create(self, validated_data):
        person = Person.objects.create(**validated_data.pop("person"))

        current_address = Address.objects.create(**validated_data.pop("current_address"))
        referrers_data = validated_data.pop("referrers")

        room_number = validated_data.pop("room_number")
        unit_number = validated_data.pop("unit_number")
        room = Room.objects.get(unit__number=unit_number, number=room_number)

        application = Application.objects.create(
            person=person, room=room, current_address=current_address, **validated_data
        )

        for r in referrers_data:
            r["applicant"] = person.pk
            referrer_serializer = ReferrerSerializer(data=r)
            referrer_serializer.is_valid(raise_exception=True)
            referrer = referrer_serializer.save()
            application.referrers.add(referrer)

        return application
