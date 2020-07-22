from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField('get_username_from')


    class Meta:
        model=Task
        fields='__all__'

    def get_username_from(self,todo_post):
        username=todo_post.user.username
        return username