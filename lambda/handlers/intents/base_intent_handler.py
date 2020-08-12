# -*- coding: utf-8 -*-

import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler

from core import SessionAttributes, Slot, Pressure, PersistentAttributes, Reminder


class BaseIntentHandler(AbstractRequestHandler):
    def __init__(self, intent_name):
        self.intent_name = intent_name
        self.handler_input = None

    def __get_list(self, key):
        attributes = self.handler_input.attributes_manager.persistent_attributes
        if key in attributes:
            return attributes[key]
        return []

    def __set_list(self, key, value):
        if not isinstance(value, list):
            pass

        manager = self.handler_input.attributes_manager
        manager.persistent_attributes[key] = value
        manager.save_persistent_attributes()

    def __pressures_list(self):
        return self.__get_list(PersistentAttributes.PRESSURES.value)

    def __set_pressures_list(self, value):
        self.__set_list(PersistentAttributes.PRESSURES.value, value)

    def __reminders_list(self):
        return self.__get_list(PersistentAttributes.REMINDERS.value)

    def __set_reminders_list(self, value):
        self.__set_list(PersistentAttributes.REMINDERS.value, value)

    def _log(self, message):
        print(f'{self.intent_name} -> {message}')

    def can_handle(self, handler_input):
        self.handler_input = handler_input
        return ask_utils.is_intent_name(self.intent_name)(handler_input)

    def add_pressure(self, pressure):
        self.__set_pressures_list(self.__pressures_list() + [pressure.to_dict()])

    def all_pressures(self):
        return list(map(lambda item: Pressure.from_dict(item), self.__pressures_list()))

    def all_reminders(self):
        return list(map(lambda item: Reminder.from_dict(item), self.__reminders_list()))

    def update_pressure_at_index(self, index, pressure):
        pressures = self.__pressures_list()

        if index < 0 or index >= len(pressures):
            pass

        pressures[index] = pressure.to_dict()
        self.__set_pressures_list(pressures)

    def update_last_pressure(self, pressure):
        self.update_pressure_at_index(-1, pressure)

    def pressures_size(self):
        return len(self.__pressures_list())

    def pop_last_pressure(self):
        pressures = self.__pressures_list()

        if len(pressures) == 0:
            return None

        last = pressures.pop()
        self.__set_pressures_list(pressures)
        return Pressure.from_dict(last)

    def add_reminder(self, reminder):
        self.__set_reminders_list(self.__reminders_list() + [reminder.to_dict()])

    def remove_reminder_by_id(self, identifier):
        all_reminders = list(filter(lambda r: r.identifier != identifier, self.all_reminders()))
        self.__set_reminders_list(list(map(lambda r: r.to_dict(), all_reminders)))

    def reminder_at_time(self):
        all_reminders = self.all_reminders()
        hour = self.hour()
        minute = self.minute()

        for reminder in all_reminders:
            if hour == reminder.hour and minute == reminder.minute:
                return reminder
        return None

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

    def time(self):
        time = self.slot(Slot.TIME.value)
        if time == 'EV':
            time = '18:00'
        elif time == 'NI':
            time = '20:00'
        elif time == 'MO':
            time = '06:00'
        elif time == 'AF':
            time = '14:00'
        return time

    def hour(self):
        return self.time().split(':')[0]

    def minute(self):
        return self.time().split(':')[1]
