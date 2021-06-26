# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class clientinfo(Action):

    def name(self) -> Text:
        return "action_client_info_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        
        return["name", "organisation", "email"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot('name')
        org = tracker.get_slot('organisation')
        email = tracker.get_slot('email')

        dispatcher.utter_message(text="Thank you, {name} for providing us with your contact info.")

        return []