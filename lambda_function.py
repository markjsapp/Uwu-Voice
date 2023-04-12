import json
import re

def uwu_converter(text):
    text = re.sub(r'(r|l)', 'w', text)
    text = re.sub(r'(R|L)', 'W', text)
    text = re.sub(r'n([aeiou])', r'ny\1', text)
    text = re.sub(r'N([aeiou])', r'Ny\1', text)
    text = re.sub(r'N([AEIOU])', r'Ny\1', text)
    text = re.sub(r'ove', 'uv', text)
    return text

def lambda_handler(event, context):
    if event['request']['type'] == 'LaunchRequest':
        return launch_request(event)
    elif event['request']['type'] == 'IntentRequest':
        return intent_request(event)

def launch_request(event):
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Welcome to UWU Voice. Please tell me what you want me to say."
            },
            "shouldEndSession": False
        }
    }
    return response

def intent_request(event):
    intent_name = event['request']['intent']['name']

    if intent_name == 'UwuSpeechIntent':
        text = event['request']['intent']['slots']['text']['value']
        uwu_text = uwu_converter(text)
        
        response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": uwu_text
                },
                "shouldEndSession": True
            }
        }
        return response

    elif intent_name == 'AMAZON.CancelIntent' or intent_name == 'AMAZON.StopIntent':
        response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Okay, stopping UWU Voice. Have a great day!"
                },
                "shouldEndSession": True
            }
        }
        return response

    else:
        response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I'm not sure how to help with that. Please tell me what you want me to say."
                },
                "shouldEndSession": False
            }
        }
        return response
