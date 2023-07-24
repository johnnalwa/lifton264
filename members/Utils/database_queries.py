from members.models import *
from members.serializer import *
from appuser.Utils.utils import getRealIDForRepID
import json

def get_member_details_from_phone(phone_number="254791836987"):
    try:
        member = Member.objects.get(primary_phone_number=phone_number)
        try:
            serializer_member = MemberSerializer(member).data
            # print(serializer_member)
        except:
            print("error!")
        
        return {"dict":member,"json":serializer_member}
    except:
        return None
        print("user not found")

def get_member_groups(member_id):
    try:
        groups = GroupMembers.objects.filter(member_id=member_id)
        serializer_groups = GroupMembersSerializer(groups,many=True).data
        
        return serializer_groups
    except:
        print("groups not found")
        return None
        
def Put_Groups_to_String(member_id):
    
    
    print(f" member_id is {member_id}")
    groups = get_member_groups(member_id=member_id)
    
    if groups == None:
        return None
    
    print(f" groups is {groups}")
    

    group_rep_id_plus_id = []
    group_rep_id = []

    # groups = json.loads(groups)

    response = ""

    for idx, val in enumerate(groups):
        group_db_id = val['id']
        group_code=val['group_code']
        group_name=val['group_name']
        
        group_rep_id_plus_id.append({"rep_id": group_code, "id": group_db_id})
        group_rep_id.append(group_code)
        
        response_to_be_added = f'{idx+1}' + ". " +  group_code + "\n"
        response += response_to_be_added
        

    print(f"rep_id {group_rep_id}")

    return {"response": response, "rep_id_plus_id": group_rep_id_plus_id,
            "rep_id": group_rep_id}


def get_group_savings(member_id):
    pass


def SumMemberSavings(array):
    
    if len(array) != 0:
        savings_sum = 0
        for x in array:
            saving = x['amount']
            savings_sum += saving
        return savings_sum
    else:
        return "no data"
    
def member_save_to_group(member_id,custom_text):
    
    group_selected = custom_text[1]
    pass

    member_id_rep_plus_id = Put_Groups_to_String(member_id=member_id)["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    print("group_id query ")
    print(group_id)
    