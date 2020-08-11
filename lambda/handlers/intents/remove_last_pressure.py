# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler


class RemoveLastPressureIntentHandler(AbstractRequestHandler):
    """Handler for Remove Last Pressure Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RemoveLastPressureIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = 'There is no blood pressure recorded yet.'

        manager = handler_input.attributes_manager
        attributes = manager.persistent_attributes

        # Deletes and updates the list of pressures only if at least one pressure was recorded before.
        if attributes and 'pressures' in attributes and len(attributes['pressures']) > 0:
            pressures = attributes['pressures']
            last_pressure = pressures[-1]
            systolic_number = last_pressure['systolic_number']
            diastolic_number = last_pressure['diastolic_number']

            pressures.pop()
            manager.persistent_attributes['pressures'] = pressures
            manager.save_persistent_attributes()

            print(f'RemoveLastPressureIntent: {len(pressures)} (current size)')

            speak_output = f'Your last pressure {systolic_number} by {diastolic_number} was removed.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
