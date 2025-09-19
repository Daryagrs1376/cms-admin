from rest_framework import serializers
from .models import Entry, ContentType
from jsonschema import validate



class ContentTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentType
        fields = '__all__'    
        


class EntrySerializer(serializers.ModelSerializer):
    
    def validate_data(self, value):
        content_type = self.instance.content_type if self.instance else ContentType.objects.get(id=self.initial_data['content_type'])
        schema = content_type.schema
        validate(instance=value, schema=schema)
        return value
    
    
    class Meta:
        model = Entry
        fields = '__all__'