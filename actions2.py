from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionGreet(Action):

	def name(self):
		return "action_greeting"

	def run(self, dispatcher, tracker, domain):
		
		person_name = next(tracker.get_latest_entity_values('person_name'), None)
		dispatcher.utter_message("Nice to meet you "+ person_name+ " How can I help you ?")
		
		return [SlotSet("person_name", person_name)]

class ActionBye(Action):

	def name(self):
		return "action_bye"

	def run(self, dispatcher, tracker, domain):
		person_name = tracker.get_slot('person_name')
		dispatcher.utter_message("See you soon "+ person_name)
		
		return []

class GetTodaysHoroscope(Action):

    def name(self):
        return "get_todays_horoscope"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = base_url.format(**{'day': "today", 'sign': user_horoscope_sign})
        #http://horoscope-api.herokuapp.com/horoscope/today/capricorn
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Your today's horoscope:\n{}".format(todays_horoscope)

        dispatcher.utter_message(response)
        return [SlotSet("horoscope_sign", user_horoscope_sign)]

    
class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
       
        subscribe = tracker.get_slot('subscribe')
        if subscribe == "True":
            response = "You're successfully subscribed"
        if subscribe == "False":
            response = "You're successfully unsubscribed"

        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]
    
    
    
