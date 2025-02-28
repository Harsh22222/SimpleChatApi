from rest_framework import serializers

from core.models import ConversationPost
from user.models import Member


class UserGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, min_value=1)


class ConversationGetSerializer(serializers.Serializer):
    loadFrom = serializers.IntegerField(required=False, min_value=1)
    loadTo = serializers.IntegerField(required=False, min_value=1)
    lastUpdate = serializers.IntegerField(required=True)


class ConversationSendSerializer(serializers.Serializer):
    content = serializers.CharField(required=True, max_length=500)


class MemberModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='member_id', read_only=True)
    username = serializers.CharField(source='name', read_only=True)
    avatar = serializers.CharField(source='pp_main_photo', read_only=True)

    class Meta:
        model = Member
        fields = ('id', 'username', 'avatar', 'last_visit', 'last_activity')
        read_only_fields = ('last_visit', 'last_activity')


class ConversationPostModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='chat_id', read_only=True)
    content = serializers.CharField(source='chat_content', read_only=True)
    sender = MemberModelSerializer(source='chat_member_id', read_only=True)

    class Meta:
        model = ConversationPost
        fields = ('id', 'chat_time', 'content', 'sender', 'chat_sys')
        read_only_fields = ('chat_time', 'chat_sys')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=255)
    password = serializers.CharField(required=True, max_length=255)


class LogoutSerializer(serializers.Serializer):
    allDevices = serializers.BooleanField(required=False)
