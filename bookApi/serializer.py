from rest_framework import serializers
from bookApi.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    pageNum = serializers.IntegerField()
    publishDate= serializers.DateField()

    def create(self,validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
         instance.title = validated_data.get("title",instance.title)
         instance.pageNum = validated_data.get("pageNum",instance.pageNum)
         instance.publishDate = validated_data.get("publishDate",instance.publishDate)
         instance.save()
         return instance