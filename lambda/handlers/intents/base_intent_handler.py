# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.dispatch_components import AbstractRequestHandler

from core import SessionAttributes, Slot, Pressure, PersistentAttributes


class BaseIntentHandler(AbstractRequestHandler):
    def __init__(self, intent_name):
        self.intent_name = intent_name
        self.handler_input = None

    def can_handle(self, handler_input):
        self.handler_input = handler_input

        slots = handler_input.request_envelope.request.intent.slots
        print(f'Request slots: {slots}\n')

        return ask_utils.is_intent_name(self.intent_name)(handler_input)

    def add_pressure(self, pressure):
        manager = self.handler_input.attributes_manager
        attributes = manager.persistent_attributes

        if not PersistentAttributes.pressures in attributes:
            attributes[PersistentAttributes.pressures] = []

        attributes[PersistentAttributes.pressures].append(pressure.to_dict())
        manager.save_persistent_attributes()

    def slot(self, slot):
        slots = self.handler_input.request_envelope.request.intent.slots
        print(f'Check slot {slot} in {slots}')
        if slot in slots:
            return slots[slot].value
        return None

    def set_session_value(self, key, value):
        manager = self.handler_input.attributes_manager
        manager.session_attributes[key] = value

    def get_session_value(self, key):
        manager = self.handler_input.attributes_manager
        return manager.session_attributes[key]

    def can_edit_last_pressure(self):
        return self.get_session_value(SessionAttributes.can_edit_last_pressure)

    def set_can_edit_last_pressure(self, can_edit):
        self.set_session_value(SessionAttributes.can_edit_last_pressure, can_edit)

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
