# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler


class ReadLastPressureIntentHandler(AbstractRequestHandler):
    """Handler for Read Last Pressure Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ReadLastPressureIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = 'There is no blood pressure recorded yet.'
        attributes = handler_input.attributes_manager.persistent_attributes

        if attributes and 'pressures' in attributes:
            last_pressure = attributes['pressures'][-1]
            print(f'last_pressure: {last_pressure}\n')
            systolic_number = last_pressure['systolic_number']
            diastolic_number = last_pressure['diastolic_number']
            speak_output = f'Your last pressure was {systolic_number} by {diastolic_number}.'

        print(f'ReadLastPressureIntent: {speak_output}\n')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
