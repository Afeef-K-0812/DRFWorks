from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    place=serializers.CharField(max_length=30)
    gender_choices=[('male','Male'),('female','Female')]    # ('db value','display value)
    gender=serializers.ChoiceField(choices=gender_choices)
    joiningdate=serializers.DateField()
    salary=serializers.IntegerField()
    designation=serializers.CharField(max_length=30)
    profile=serializers.ImageField()

    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError('Age must be Positive')
        if data['age']<18:
            raise serializers.ValidationError('Age must be greater than 18')
        return data

    def create(self,validated_data):                # After validation and before saving
        e=Employee.objects.create(**validated_data)
        return e

    def update(self,i,validated_data):  # After validation and before saving
        i.empid=validated_data.get('empid',i.empid)
        i.name=validated_data.get('name',i.name)
        i.age=validated_data.get('age',i.age)
        i.place=validated_data.get('place',i.place)
        i.gender=validated_data.get('gender',i.gender)
        i.joiningdate=validated_data.get('joiningdate',i.joiningdate)
        i.salary=validated_data.get('salary',i.salary)
        i.designation=validated_data.get('designation',i.designation)

        i.save()
        return i

