# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
# import weather_api
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

basic_info_flag = False

# write some logic that if the slot is not filled, ask question from the question_queue

# in some ways the bots job is to fill slots until it can provide a response


class DetermineNextQuestion(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "get_next_question"

    def run(self, dispatcher, tracker, domain):
        # what your action should do

        # for i in question queue that is also in slots filled, skip, else, ask question

        if basic_info_flag == False:  # check slots
            if tracker.get_slot('name') != None:
                # do something
                next_question = "Would you mind repeating your name?"
                dispatcher.utter_message(next_question)
                return
            elif tracker.get_slot('address') != None:
                # do something
                next_question = "Would you mind repeating your address?"
                dispatcher.utter_message(next_question)
                return
            elif tracker.get_slot('zipcode') != None:
                # do something
                next_question = "Would you mind repeating your zipcode?"
                dispatcher.utter_message(next_question)
                return
            elif tracker.get_slot('city') != None:
                # do something
                next_question = "Would you mind repeating your city?"
                dispatcher.utter_message(next_question)
                return
            elif tracker.get_slot('state') != None:
                # do something
                next_question = "Would you mind repeating your state?"
                dispatcher.utter_message(next_question)
                return
            exit_message = "basic information complete"
            dispatcher.utter_message(exit_message)
            basic_info_flag = True
            return
        elif basic_info_flag == True:
            return
            # todo add change of context here (next flag operation)
