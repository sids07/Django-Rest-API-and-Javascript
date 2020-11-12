## Serializer can be used to make validation set that is used on form as we are expecting two integers for calculation.
## But user may give us string instead of number which will throw some error.

from rest_framework import serializers
from .models import Info

class AddTwoNumber(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)

    def create(self,validated_data):
        print("context on serializer",self.context)
        #if serializer doesn't get input directly and we have to pass it manually then we can use context.
        return Info.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']

        instance.save()

        return instance

class InfoModelSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    # if we have to make the use of defined field to give message
    
    class Meta:
        model = Info
        fields = ['name','address','message','id']
        read_only_fields=['id']
        #to use only while reading and ignore while posting
        #exclude=['id']

    @staticmethod
    def get_message(obj):
        name = obj.name
        return f"Hi my name is {name}"

    @staticmethod
    def validate_name(name):
        #(Specific field)field level validation ko lagi
        # calling static method decoraters, we can skip writing self on the parameter
        if len(name)<=1:
            raise serializers.ValidationError("Length of Name Should be greater than 1")

        return name

    def validate(self,data):
        #(every field validation no specific field mentioned)
        print(data)
        #we can see data is in Ordered dict form
        name = data['name']
        address = data['address']
        if name==address:
            raise serializers.ValidationError("Name and Address cannot be same")
            # as no field is mentioned to be related for this error we will get non field error
        return data