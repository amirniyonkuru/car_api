from .models import Car
from rest_framework import serializers


# using slugrelatedfield to return name instead of id if many to many, you put many=true
class CarSerializer(serializers.ModelSerializer):
    # carmake = serializers.SlugRelatedField(read_only=True, slug_field="name")
    # carmodel = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Car
        fields = "__all__"
