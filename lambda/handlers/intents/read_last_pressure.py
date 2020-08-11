# -*- coding: utf-8 -*-

from .base_intent_handler import BaseIntentHandler


class ReadLastPressureIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('ReadLastPressureIntent')

    def handle(self, handler_input):
        pressures = self.all_pressures()
        speak_output = 'There is no blood pressure recorded yet.'

        if len(pressures) > 0:
            last_pressure = pressures[-1]
            print(f'last_pressure: {last_pressure.to_dict()}\n')
            speak_output = f'Your last pressure was {last_pressure.systolic_number} by {last_pressure.diastolic_number}.'

        print(f'ReadLastPressureIntent: {speak_output}\n')

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
