# -*- coding: utf-8 -*-

import datetime
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler


class EditLastPressureIntentHandler(AbstractRequestHandler):
    """Handler for Edit Last Pressure Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("EditLastPressureIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = 'You haven\'t registered a pressure recently.'

        manager = handler_input.attributes_manager
        attributes = manager.persistent_attributes

        # Edit last pressure only if at least one pressure was recorded before.
        if 'can_edit_last_pressure' in manager.session_attributes:
            slots = handler_input.request_envelope.request.intent.slots

            print(f'Request slots: {slots}\n')

            systolic_number = int(slots['systolic_number'].value)
            diastolic_number = int(slots['diastolic_number'].value)
            pressure = {
                'systolic_number': systolic_number,
                'diastolic_number': diastolic_number,
                'timestamp': datetime.datetime.now().isoformat()
            }
            attributes['pressures'].pop()
            attributes['pressures'].append(pressure)
            manager.save_persistent_attributes()

            speak_output = f'Your last pressure was edited to {systolic_number} by {diastolic_number}.'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
