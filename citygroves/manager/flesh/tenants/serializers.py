from typing import Dict, Any

from housing.models import Room, Unit
from tenants.models import Application, Person, Address, Referrer
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ReferrerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    applicant = serializers.IntegerField(required=False)

    class Meta:
        model = Referrer
        fields = "__all__"

    def create(self, validated_data) -> Referrer:
        address = Address.objects.create(**validated_data.pop('address'))
        applicant = Person.objects.get(id=validated_data.pop('applicant'))
        referrer = Referrer.objects.create(address=address, applicant=applicant, **validated_data)
        return referrer


class ApplicationSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    current_address = AddressSerializer()
    referrers = ReferrerSerializer(many=True)
    room = serializers.PrimaryKeyRelatedField(read_only=True, pk_field="number")

    class Meta:
        model = Application
        fields = "__all__"

    def create(self, validated_data):
        person = Person.objects.create(**validated_data.pop('person'))

        current_address = Address.objects.create(**validated_data.pop('current_address'))
        referrers_data = validated_data.pop('referrers')

        application = Application.objects.create(person=person, current_address=current_address,
                                                 **validated_data)

        for r in referrers_data:
            r["applicant"] = person.id
            referrer_serializer = ReferrerSerializer(data=r)
            referrer_serializer.is_valid(raise_exception=True)
            referrer = referrer_serializer.save()
            application.referrers.add(referrer)

        return application
