from typing import Dict, Any

from housing.models import Room, Unit
from tenants.models import Application, Person, Address, Referrer
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ReferrerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    applicant = serializers.PrimaryKeyRelatedField(required=False, queryset=Person.objects.all())

    class Meta:
        model = Referrer
        fields = "__all__"

    def create(self, validated_data) -> Referrer:
        address = Address.objects.create(**validated_data.pop('address'))
        applicant = validated_data.pop('applicant')
        referrer = Referrer.objects.create(address=address, applicant=applicant, **validated_data)
        return referrer


class ApplicationSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    current_address = AddressSerializer()
    referrers = ReferrerSerializer(many=True)
    room_number = serializers.IntegerField(write_only=True)
    unit_number = serializers.IntegerField(write_only=True)

    class Meta:
        model = Application
        fields = ["room_number", "unit_number", "person", "room", "current_address",
                  "number_of_ppl_to_move_in", "move_in_date", "guarantor_will_pay",
                  "centerlink_will_pay", "is_employed", "have_sufficient_funds",
                  "is_local_student", "is_international_student", "is_young_professional",
                  "referrers", "digital_signature"]

    def update(self, instance: Application, validated_data):
        unit_number: int = instance.room.unit.number
        room_number: int = instance.room.number

        if 'room_number' in validated_data:
            room_number = validated_data.pop('room_number')

        if 'unit_number' in validated_data:
            unit_number = validated_data.pop('unit_number')

        room = Room.objects.get(unit__number=unit_number, number=room_number)
        instance.room = room

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance

    def create(self, validated_data):
        person = Person.objects.create(**validated_data.pop('person'))

        current_address = Address.objects.create(**validated_data.pop('current_address'))
        referrers_data = validated_data.pop('referrers')

        room_number = validated_data.pop('room_number')
        unit_number = validated_data.pop('unit_number')
        room = Room.objects.get(unit__number=unit_number, number=room_number)

        application = Application.objects.create(person=person, room=room, current_address=current_address,
                                                 **validated_data)

        for r in referrers_data:
            r["applicant"] = person.pk
            referrer_serializer = ReferrerSerializer(data=r)
            referrer_serializer.is_valid(raise_exception=True)
            referrer = referrer_serializer.save()
            application.referrers.add(referrer)

        return application
