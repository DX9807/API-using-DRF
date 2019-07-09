from rest_framework import serializers
from DRFS.models import Status

'''
Serializers --> JSON
Serializers --> Also validate data
'''
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
             'id',
             'user',
             'content',
             'image'
        ]
