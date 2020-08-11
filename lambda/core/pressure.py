# -*- coding: utf-8 -*-

import datetime
import dateutil.parser


class Pressure:
    __SYSTOLIC_NUMBER = 'systolic_number'
    __DIASTOLIC_NUMBER = 'diastolic_number'
    __TIMESTAMP = 'timestamp'

    def __init__(self, systolic_number, diastolic_number, timestamp = datetime.datetime.now()):
        self.systolic_number = systolic_number
        self.diastolic_number = diastolic_number
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, dict):
        return Pressure(systolic_number=dict[cls.__SYSTOLIC_NUMBER],
                        diastolic_number=dict[cls.__DIASTOLIC_NUMBER],
                        timestamp=dateutil.parser.parse(dict[cls.__TIMESTAMP]))

    def to_dict(self):
        return {
                self.__SYSTOLIC_NUMBER: self.systolic_number,
                self.__DIASTOLIC_NUMBER: self.diastolic_number,
                self.__TIMESTAMP: self.timestamp.isoformat()
            }
