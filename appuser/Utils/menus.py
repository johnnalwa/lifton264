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
    response += "4. Loans \n"
    response += "5. Inputs \n"
    response += "6. Market \n"
    

    return response


# Savings

def response_menu_savings(custom_text_two):
    response = f'CON Savings\n'
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
    response = f'CON Welfare\n'
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
    response = f'CON Penalties\n'
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


# loan

# View group no of loans outstanding  (output-> 4 members)
# -View your loan amount outstanding 
# -Apply for input loan(receive message for with voucher code once loan approved )***Only applicable if the member doesn’t have any ousstanding bal,max 3 times savings *** 

def response_menu_loan(custom_text_two):
    response = f'CON Loan\n'
    response += "1. View group no of loans outstanding\n"
    response += "2. View your loan amount outstanding   \n"
    response += "3. Apply for input loan   \n"
    
    return response

def response_menu_group_loan(custom_text_two):
    response = f'END '
    response += "Group loan is ksh 10,000 \n"
    return response

def response_menu_my_loan(custom_text_two):
    response = f'END '
    response += "Your loan is ksh 10,000 \n"
    return response
def response_menu_apply_input_loan(custom_text_two):
    response = f'END '
    response += "You will receive an SMS message with voucher code once loan approved \n"
    return response



# input


# Inputs
# -Make order from inputs (normal order,or using voucher order ) 
# 1.Normal Order
# 2.Voucher
# -If normal order
# 1.	Select product
# 2.	Select vendor
# 3.	Pay
# If voucher
# 1.	Indicate id no.(generate the voucher no)
# 2.	Select vendor
# 3.	Accept redeeming the voucher

def response_menu_inputs(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Make normal order\n"
    response += "2. Make order with voucher\n"    
    return response

# If normal order
def response_menu_inputs_normal_order(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Select product\n"
    response += "2. Select vendor\n" 
    response += "3. Pay\n"    
       
    return response


def response_menu_inputs_normal_select_product(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Product 1\n"
    response += "2. Product 2\n"    
    response += "3. Product 3\n"    
    
    return response

def response_menu_inputs_normal_select_vendor(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Vendor 1\n"
    response += "2. Vendor 2\n"    
    response += "3. Vendor 3\n"    
    
    return response

# If voucher

def response_menu_inputs_voucher_order(custom_text_two):
    response = f'CON Make order from inputs\n'
    response += "1. Indicate ID number\n"
    response += "2. Select vendor\n" 
    response += "3. Accept redeeming the voucher\n"  
    return response
    

def response_menu_inputs_voucher_select_indicate_id_number(custom_text_two):
    response = f'CON Enter your ID number\n'
    
    return response

def response_menu_inputs_voucher_generate_voucher(custom_text_two):
    response = f'END You will receive an SMS message with voucher code\n'
    
    return response
def response_menu_inputs_voucher_accept_voucher(custom_text_two):
    response = f'END Voucher accepted\n'
    
    return response


# end inputs





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
        if custom_text[-1] == '4':
            return response_menu_loan(custom_text)
        if custom_text[-1] == '5':
            return response_menu_inputs(custom_text)
        
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
        elif custom_text[-2] == '4':
            if custom_text[-1] == '1':
                return response_menu_group_loan(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_my_loan(custom_text)
            elif custom_text[-1] == '3':
                return response_menu_apply_input_loan(custom_text)
        elif custom_text[-2] == '5':
            if custom_text[-1] == '1':
                return response_menu_inputs_normal_order(custom_text)
            elif custom_text[-1] == '2':
                return response_menu_inputs_voucher_order(custom_text)
           
            
       
    
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
            
        elif custom_text[-3] == '5':
            if custom_text[-2] == '1':
                if custom_text[-1] == '1':
                    return response_menu_inputs_normal_select_product(custom_text)
                elif custom_text[-1] == '2':
                    return response_menu_inputs_normal_select_vendor(custom_text)
            elif custom_text[-2] == '2':
                if custom_text[-1] == '1':
                    return response_menu_inputs_voucher_select_indicate_id_number(custom_text)
                elif custom_text[-1] == '2':
                    return response_menu_inputs_normal_select_vendor(custom_text) 
                elif custom_text[-1] == '3':
                    return response_menu_inputs_voucher_accept_voucher(custom_text) 
            else:
                pass
            
            # return response_menu_pay_welfare_savings_stk(custom_text)
                
       
    elif level == 5:
        if custom_text[-2] == '1':
            return response_menu_want_to_save_yes_amount(custom_text)
        elif custom_text[-2] == '2':
            return response_menu_pay_welfare_savings_stk(custom_text)
        elif custom_text[-2] == '3':
            return response_menu_pay_penalties_stk(custom_text)
            
            

        

   
   
    
        
