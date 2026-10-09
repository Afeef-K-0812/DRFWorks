from django.core.mail import send_mail
from rest_framework import serializers
from movies.models import Movie

# class MovieSerializer(serializers.Serializer):
#     title=serializers.CharField()
#     director=serializers.CharField()
#     language=serializers.CharField()
#     year=serializers.IntegerField()
#     rating=serializers.FloatField()
#     runtime=serializers.IntegerField()
#
#     def create(self,validated_data):
#         m=Movie.objects.create(**validated_data)
#         return m
#
#     def update(self,instance,validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.director=validated_data.get('director',instance.director)
#         instance.language=validated_data.get('language',instance.language)
#         instance.year=validated_data.get('year',instance.year)
#         instance.rating=validated_data.get('rating',instance.rating)
#         instance.runtime=validated_data.get('runtime',instance.runtime)
#
#         instance.save()
#         return instance

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie

        fields='__all__'

        # or

        # fields=['title','director','language','year','rating','runtime']


from django.contrib.auth.models import User
from movies.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','email','first_name','last_name','phone','address']

# To Create User Account we use User.objects.create_user() instead of create() - To save passwords encrypted
    def create(self,validated_data):
        u=CustomUser.objects.create_user(**validated_data)
        u.save()
        send_mail('User Registration Confirmation Mail',
                  'Your Account Created Successfully',
                  'thelonsoul3399@gmail.com',
                  [u.email],fail_silently=True)
        return u

