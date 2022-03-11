from rest_framework import serializers
from tasks.models import Task, LANGUAGE_CHOICES, STYLE_CHOICES

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description']
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # description = serializers.CharField(required=False, allow_blank=True, max_length=300)

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance