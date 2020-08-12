# -*- coding: utf-8 -*-
from ask_sdk_model.ui import StandardCard
from ask_sdk_model.ui.image import Image

from .base_intent_handler import BaseIntentHandler
from core import Pressure, PressureStatus


class ReportLatestPressuresIntentHandler(BaseIntentHandler):
    def __init__(self):
        super().__init__('ReportLatestPressuresIntent')

    def handle(self, handler_input):
        latest_number = 21
        all_pressures = self.all_pressures()
        latest_pressures = all_pressures[-min(latest_number, len(all_pressures)):]
        card_title = f'Your latest {latest_number} pressures'
        card_text = ''
        card_image = Image(
            'https://pressure-monitor-logo.s3-eu-west-1.amazonaws.com/pressure_monitor_medium.png',
            'https://pressure-monitor-logo.s3-eu-west-1.amazonaws.com/pressure_monitor_large.png'
        )
        speak_output = 'Your report was sent to your account. You can check it on the portal or the mobile app.'

        self._log(f'latest pressures: {latest_pressures}')

        for pressure in latest_pressures:
            date = pressure.timestamp.strftime('%d %b %Y %H:%M')
            card_text += f'❤️ {pressure.systolic_number} by {pressure.diastolic_number} as {pressure.status().description()} at {date}\n'

        card = StandardCard(card_title, card_text, card_image)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(card)
                .response
        )

