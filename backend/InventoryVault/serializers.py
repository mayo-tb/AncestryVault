from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    parents = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all(), required=False)
    spouse = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), required=False, allow_null=True)
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = [
            'id', 'full_name', 'date_of_birth', 'gender', 'profession',
            'profile_picture', 'video_description', 'parents', 'spouse', 'children'
        ]