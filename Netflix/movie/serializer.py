from .models import *
from rest_framework import serializers

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=['id','name','birth_date','gender']
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id','title','genre','date','actors']

