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
        return ask_utils.is_intent_name(self.intent_name)(handler_input)

    def add_pressure(self, pressure):
        manager = self.handler_input.attributes_manager
        attributes = manager.persistent_attributes
        pressures_key = PersistentAttributes.PRESSURES.value

        if not pressures_key in attributes:
            attributes[pressures_key] = []

        attributes[pressures_key].append(pressure.to_dict())
        manager.save_persistent_attributes()

    def all_pressures(self):
        attributes = self.handler_input.attributes_manager.persistent_attributes
        pressures_key = PersistentAttributes.PRESSURES.value

        if pressures_key in attributes:
            return map(lambda item: Pressure.from_dict(item), attributes[pressures_key])
        return []

    def slot(self, slot):
        slots = self.handler_input.request_envelope.request.intent.slots
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
        return self.get_session_value(SessionAttributes.CAN_EDIT_LAST_PRESSURE.value)

    def set_can_edit_last_pressure(self, can_edit):
        self.set_session_value(SessionAttributes.CAN_EDIT_LAST_PRESSURE.value, can_edit)

    def systolic_number(self):
        value = self.slot(Slot.SYSTOLIC_NUMBER.value)
        if value is not None:
            return int(value)
        return None

    def diastolic_number(self):
        value = self.slot(Slot.DIASTOLIC_NUMBER.value)
        if value is not None:
            return int(value)
        return None
