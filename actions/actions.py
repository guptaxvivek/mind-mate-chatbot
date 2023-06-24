# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionRecieveName(Action):

    def name(self) -> Text:
        return "action_receive_named"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"That's a nice name {text}!")
        return [SlotSet("name", text)]


class ActionRecieveDelight(Action):

    def name(self) -> Text:
        return "action_receive_delight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f"Great!")
        return [SlotSet("user_delight", tracker.latest_message['text'])]


class ActionRecieveFeedback(Action):

    def name(self) -> Text:
        return "action_receive_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_submit")
        return [SlotSet("journal", tracker.latest_message['text'])]


class ActionGetData(Action):
    def name(self) -> Text:
        return "action_get_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        GetData(tracker.get_slot("name"), tracker.get_slot("journal"))
        dispatcher.utter_message('Thanks for the feedback!')
        return []
