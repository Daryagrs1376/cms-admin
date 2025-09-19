from rest_framework import serializers
from .models import Entry, ContentType


class ContentTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentType
        fields = '__all__'    
        

class EntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Entry
        fields = '__all__'

#Validation schema هنوز برای کلاس EntrySerializer انجام ندادم 
#بخاطر همین اگر یه دیتای اشتباه برخلاف منطق تسک وارد بشه یعنی 
#رشته بجای عدد وارد بشه قبول میکنه و ذخیره میشه چون چک نمیکنه
#اینجا باید یه مکانیزم بسازم که چک کنه باschema همخونی داره یا ن
#اینطوری اگر schema بگه فیلد باید عدد باشه توی entry نباید بشه یه رشته گذاشت
#که این کار با کتابخونه jsonschema انجام میشه