from members.models import *
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ('id',"first_name","last_name",)
        

class GroupMembersSerializer(serializers.ModelSerializer):
    member_name = serializers.ReadOnlyField(
        source='member_id.name')
    group_name = serializers.ReadOnlyField(
        source='group_id.name')
    group_code = serializers.ReadOnlyField(
        source='group_id.special_code')
    
    class Meta:
        model = GroupMembers
        fields = ('id',"member_id","group_id","group_name","member_name","group_code",)