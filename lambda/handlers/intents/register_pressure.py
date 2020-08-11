# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler


class RegisterPressureIntentHandler(AbstractRequestHandler):
    """Handler for Register Pressure Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("RegisterPressureIntent")(handler_input)

    def handle(self, handler_input):
        slots = handler_input.request_envelope.request.intent.slots

        print(f'Request slots: {slots}\n')

        systolic_number = slots['systolic_number'].value
        diastolic_number = slots['diastolic_number'].value
        manager = handler_input.attributes_manager

        speak_output = f'Your pressure {systolic_number} by {diastolic_number} is normal.'

        print(f'RegisterPressureIntent: {speak_output}\n')

        if not 'pressures' in manager.persistent_attributes:
            manager.persistent_attributes['pressures'] = []

        manager.persistent_attributes['pressures'].append({
            'systolic_number':  int(systolic_number),
            'diastolic_number': int(diastolic_number),
            'timestamp': datetime.datetime.now().isoformat()
        })
        manager.save_persistent_attributes()
        manager.session_attributes['can_edit_last_pressure'] = True

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
