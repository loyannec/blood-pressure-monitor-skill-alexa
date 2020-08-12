# -*- coding: utf-8 -*-
from ask_sdk_model.ui import StandardCard
from ask_sdk_model.ui.image import Image

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class ReportLatestPressuresIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('ReportLatestPressuresIntent')

    def handle(self, handler_input):
        latest_number = 5
        all_pressures = self.all_pressures()
        latest_pressures = all_pressures[-min(latest_number, len(all_pressures)):]
        card_title = f'Your latest {latest_number} pressures'
        card_text = ''
        card_image = Image(
            'https://drive.google.com/file/d/1NGt5K8C5gH92Xlfm6d_paCWfotAP-fRb/view?usp=sharing',
            'https://drive.google.com/file/d/1wDiddNjJMhjkWhcKChH-Tt5BO06fmayU/view?usp=sharing'
        )
        speak_output = 'Your report was sent to your account. You can check it on the portal or the mobile app.'

        self._log(f'latest pressures: {latest_pressures}')

        for pressure in latest_pressures:
            card_text += f'-> {pressure.systolic_number} by {pressure.diastolic_number} as {pressure.status().description()}\n'

        card = StandardCard(card_title, card_text, card_image)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(card)
                .response
        )

# pressure.timestamp.strftime('%d %b %Y %H:%M')
