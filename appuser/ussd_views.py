from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from appuser.Utils.constants import LEVEL_ONE_OPTIONS_META_DATA, LEVEL_TWO_OPTIONS_META_DATA
from appuser.Utils.menus import response_main_with_text

from appuser.Utils.utils import goToBack, goToMain, removeUnwantedTexts, replaceCommaSpace, replaceEstericWithSpace, replaceSpaceFromText, saveSessionsToDatabase
# Create your views here.






class App_USSD(APIView):
    def post(self, request, format=None):
        response = ""
        # convert request data to JSON, use this outside Africa's talking
        data = JSONParser().parse(request)

        data = request.data

        # get params from data, use this with Africa's talking
        session_id = data.get("SESSION_ID", None)
        serviceCode = data.get("SERVICE_CODE", None)
        phone_number = data.get("MSISDN", None)
        text = data.get("USSD_STRING", None)
        
        if text == None:
            text = data.get("text", "default")
        
        # networkCode = data.get("networkCode", None)

        # uncomment this when using Africa's talking
        # session_id = data["sessionId"]
        # serviceCode = data["serviceCode"]
        # phone_number = data["phoneNumber"]
        # text = data["text"]
        
        print(f"phone_number is {phone_number}")

        # handle back_texts
        text = goToBack(text)

        # removing go to main response
        text = goToMain(text)

        custom_text_two = text

        text = removeUnwantedTexts(
            array=LEVEL_ONE_OPTIONS_META_DATA["options"], text=text, position_in_text=LEVEL_ONE_OPTIONS_META_DATA["position_in_array"])
        text = removeUnwantedTexts(
            array=LEVEL_TWO_OPTIONS_META_DATA["options"], text=text, position_in_text=LEVEL_TWO_OPTIONS_META_DATA["position_in_array"])

     


      
     
            
        #Clean the text
        custom_text = replaceSpaceFromText(text)
        custom_text = replaceEstericWithSpace(custom_text)
        custom_text = replaceCommaSpace(custom_text)

        custom_text_two = replaceSpaceFromText(custom_text_two)
        custom_text_two = replaceEstericWithSpace(custom_text_two)

        custom_text_two = replaceCommaSpace(custom_text_two)

        custom_text = custom_text.split()
        custom_text_two = custom_text_two.split()

      
        if text == '' or len(custom_text) == 0:
            # level 1
            response = response_main_with_text(
               text=text, custom_text=custom_text, phone_number=phone_number,
                custom_text_two=custom_text_two)
        else:
            # when the text is not empty
            response = response_main_with_text(
                text=text, custom_text=custom_text, phone_number=phone_number,
                custom_text_two=custom_text_two
            )

        # Save session here

        # saveSessionsToDatabase(
        #     phoneNumber=phone_number, text=text, sessionNumber=session_id, response=response)

        return HttpResponse(response)
