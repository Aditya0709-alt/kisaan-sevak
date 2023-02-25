import pandas as pd
import numpy as np
import csv
from typing import Text, Dict, List, Any
import datetime as dt
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# Actions 

# df = pd.read_csv('kcc_qna.csv')
# print(df.head())
# print(df.tail())

class ActionQuerySerch(Action):

    def name(self) -> Text:
        return "action_query_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        crop = tracker.get_slot("crop_type")
        question = tracker.get_slot("question")

        f = csv.reader(open('KisanCallCenter.csv', 'r'), delimiter=",")
        for row in f:
            if crop == row[0] and question == row[1]:
                answer = row[2]
        
        dispatcher.utter_message(f"The answer to your query is \n The recommended solution for your crop {crop} is {answer} .")
        # return [SlotSet("answer", answer)]

class ActionReturnTime:
    def name(self) -> Text:
            return "action_return_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = dt.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        dispatcher.utter_message(text="Today's Date and time" +str(dt_string))

        return []
