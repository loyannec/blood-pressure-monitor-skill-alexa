# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler

from .slots import Slot


class BaseIntentHandler(AbstractRequestHandler):
    def __init__(self, intent_name):
        self.intent_name = intent_name
        self.handler_input = None

    def can_handle(self, handler_input):
        self.handler_input = handler_input
        return ask_utils.is_intent_name(self.intent_name)(handler_input)

    # def add_pressure(self, pressure):
    #     manager = self.handler_input.attributes_manager
    #     attributes = manager.persistent_attributes

    def slot(self, slot):
        slots = self.handler_input.request_envelope.request.intent.slots
        if slot in slots:
            return slots[slot].value
        return None


    def systolic_number(self):
        value = self.slot(Slot.systolic_number)
        if value is not None:
            return int(value)
        return None

    def diastolic_number(self):
        value = self.slot(Slot.diastolic_number)
        if value is not None:
            return int(value)
        return None