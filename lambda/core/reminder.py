# -*- coding: utf-8 -*-

class Reminder:
    __IDENTIFIER = 'identifier'
    __HOUR = 'hour'
    __MINUTE = 'minute'

    def __init__(self, identifier, hour, minute):
        self.identifier = identifier
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return ('{ ' + f'{self.identifier} {self.hour}:{self.minute}' + ' }')

    def to_dict(self):
        return {
                self.__IDENTIFIER: self.identifier,
                self.__HOUR: self.hour,
                self.__MINUTE: self.minute
            }

    @classmethod
    def from_dict(cls, item):
        return Reminder(identifier=item[cls.__IDENTIFIER],
                        hour=item[cls.__HOUR],
                        minute=item[cls.__MINUTE])

