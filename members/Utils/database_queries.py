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
        
        group_rep_id_plus_id.append({"rep_id": idx+1, "id": group_db_id})
        
        group_rep_id.append(idx+1)
        
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
        return f"0.00"
  
def get_member_savings(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    savings = Saving.objects.filter(group_id=group_id).filter(member_id=member_id)
    savings_serializer = SavingsSerializer(savings,many=True).data
    
    # print(savings_serializer)
    # print(SumMemberSavings(savings_serializer))
    
    return SumMemberSavings(savings_serializer)

def get_group_savings(custom_text,member_id):
    group_selected = custom_text[1]
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    
    savings = Saving.objects.filter(group_id=group_id)
    savings_serializer = SavingsSerializer(savings,many=True).data
    
    # print(savings_serializer)
    # print(SumMemberSavings(savings_serializer))
    
    return SumMemberSavings(savings_serializer)
  
def member_save_to_group(custom_text,member_id):
    
    group_selected = custom_text[1]
    amount = custom_text[-1]
    
    
    member_groups_string = Put_Groups_to_String(member_id=member_id)


    member_id_rep_plus_id = member_groups_string["rep_id_plus_id"]

    group_id  = getRealIDForRepID(array=member_id_rep_plus_id,rep_id=group_selected)
    
    group_id_object = Group.objects.get(id=group_id)
    member_id_object = Member.objects.get(id=member_id)
    
    savings = Saving(member_id=member_id_object,group_id=group_id_object,amount=amount)
    savings.save()
    
    print("group_id query ")
    print(member_groups_string)
    print(group_selected)
    print(member_id_object)
    
    
    