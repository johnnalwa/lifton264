from appuser.Utils import constants

def response_session_ended():
    response = ''
    response = f'END This session has ended. \n'

    return response


def response_menu_landing(custom_text_two):
    # Level 1
    response = f'CON Welcome to {constants.APP_NAME} \n'
    response += "1. Accept terms and conditions \n"
    response += "2. Decline \n"
    
    
    return response

def response_decline_conditions(custom_text_two):
    response = f'END '
    response += "Thank you for using the E-Group system \n"
    return response

def response_menu_one(custom_text_two):
    # Level 1
    response = f'CON '
    response += "1. Savings \n"
    response += "2. Welfare \n"
    response += "3. Penalties \n"
    response += "3. Loans \n"
    response += "4. Inputs \n"
    response += "5. Market \n"
    

    return response


# Savings

def response_menu_savings(custom_text_two):
    response = f'CON '
    response += "1. Group Savings balance \n"
    response += "2. Your savings balance \n"
    response += "3. Do you want to save? \n"
    return response

def response_menu_group_savings(custom_text_two):
    response = f'END '
    response += "Group Savings balance is ksh 10,000 \n"
    return response

def response_menu_your_savings(custom_text_two):
    response = f'END '
    response += "Your Group Savings balance is ksh 3,000 \n"
    return response

def response_menu_want_to_save(custom_text_two):
    response = f'CON '
    response += "1. Yes \n"
    response += "2. No \n"
    return response

def response_menu_want_to_save_yes(custom_text_two):
    response = f'CON '
    response += "Enter the amount you want to save \n"
    return response

def response_menu_want_to_save_yes_amount(custom_text_two):
    response = f'END '
    response += "An STK push will be sent to your phone \n"
    return response

def response_menu_want_to_save_no(custom_text_two):
    response = f'END '
    response += "Thank you for using the E-Group system \n"
    return response

# end savings



# welfare

def response_menu_welfare(custom_text_two):
    response = f'CON '
    response += "1. View Welfare group balance \n"
    response += "2. View Your welfare total savings \n"
    response += "3. Pay for your welfare savings \n"
    return response


def response_menu_welfare_group_balance(custom_text_two):
    response = f'END '
    response += "Welfare group balance is ksh 10,000 \n"
    return response
def response_menu_welfare_total_savings(custom_text_two):
    response = f'END '
    response += "Your welfare total savings is ksh 10,000 \n"
    return response

def response_menu_pay_welfare_savings(custom_text_two):
    response = f'CON '
    response += "Enter the amount you want to save \n"
    return response

def response_menu_pay_welfare_savings_stk(custom_text_two):
    response = f'END '
    response += "An STK push will be sent to your phone \n"
    return response


# penalties

def response_menu_penalties(custom_text_two):
    response = f'CON '
    response += "1. View penalties\n"
    response += "2. Do you want to pay for penalties  \n"
    return response
def response_menu_view_penalties(custom_text_two):
    response = f'END '
    response += "Penalties is ksh 10,000 \n"
    return response


def response_menu_want_to_pay_penalties(custom_text_two):
    response = f'CON '
    response += "1. Yes \n"
    response += "2. No \n"
    return response

def response_menu_pay_penalties_yes(custom_text_two):
    response = f'CON '
    response += "Enter the amount you want to save \n"
    return response

def response_menu_pay_penalties_stk(custom_text_two):
    response = f'END '
    response += "An STK push will be sent to your phone \n"
    return response

def response_menu_pay_penalties_no(custom_text_two):
    response = f'END '
    response += "Thank you for using the E-Group system \n"
    return response

def response_main_with_text(text, custom_text, 
    phone_number, custom_text_two
    ):
    
    # print(f"phone_number2 is {phone_number}")

    level = len(custom_text)

    previous_value = ""
    print(f"level is {level}")
    # print(f" {custom_text[-2]}")
    

    if level == 0:
        print("is in level 0")
        return response_menu_landing(custom_text_two)

   
    if level == 1:
        print("is in level 1")
        if custom_text[-1] == '1':
            return response_menu_one(custom_text)
        elif custom_text[-1] == '2':
            return response_decline_conditions(custom_text)
    
    elif level == 2:
        print("levelis 2")
        if custom_text[-1] == '1':
            return response_menu_savings(custom_text)
        if custom_text[-1] == '2':
            return response_menu_welfare(custom_text)
        if custom_text[-1] == '3':
            return response_menu_penalties(custom_text)
        
    elif level == 3:
        if custom_text[-2] == '1':
            if custom_text[-1] == '1':
                return response_menu_group_savings(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_your_savings(custom_text)
            elif custom_text[-1] == '3':
                return response_menu_want_to_save(custom_text)
        elif custom_text[-2] == '2':
            if custom_text[-1] == '1':
                return response_menu_welfare_group_balance(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_welfare_total_savings(custom_text)
            elif custom_text[-1] == '3':
                return response_menu_pay_welfare_savings(custom_text)
        elif custom_text[-2] == '3':
            if custom_text[-1] == '1':
                return response_menu_view_penalties(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_want_to_pay_penalties(custom_text)
            
       
    
    elif level == 4:
        if custom_text[-3] == '1':
            if custom_text[-1] == '1':
                return response_menu_want_to_save_yes(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_want_to_save_no(custom_text)
        elif custom_text[-3] == '2':
            return response_menu_pay_welfare_savings_stk(custom_text)
        elif custom_text[-3] == '3':
            if custom_text[-1] == '1':
                return response_menu_pay_penalties_yes(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_pay_penalties_no(custom_text)
            # return response_menu_pay_welfare_savings_stk(custom_text)
                
       
    elif level == 5:
        if custom_text[-2] == '1':
            return response_menu_want_to_save_yes_amount(custom_text)
        elif custom_text[-2] == '2':
            return response_menu_pay_welfare_savings_stk(custom_text)
        elif custom_text[-2] == '3':
            return response_menu_pay_penalties_stk(custom_text)
            
            

        

   
   
    
        
