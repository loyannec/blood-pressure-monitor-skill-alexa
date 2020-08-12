# -*- coding: utf-8 -*-

import datetime
import dateutil.parser

from .pressure_status import PressureStatus


class Pressure:
    __SYSTOLIC_NUMBER = 'systolic_number'
    __DIASTOLIC_NUMBER = 'diastolic_number'
    __TIMESTAMP = 'timestamp'

    def __init__(self, systolic_number, diastolic_number, timestamp = datetime.datetime.now()):
        self.systolic_number = systolic_number
        self.diastolic_number = diastolic_number
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, item):
        return Pressure(systolic_number=item[cls.__SYSTOLIC_NUMBER],
                        diastolic_number=item[cls.__DIASTOLIC_NUMBER],
                        timestamp=dateutil.parser.parse(item[cls.__TIMESTAMP]))

    def to_dict(self):
        return {
                self.__SYSTOLIC_NUMBER: self.systolic_number,
                self.__DIASTOLIC_NUMBER: self.diastolic_number,
                self.__TIMESTAMP: self.timestamp.isoformat()
            }

    def status(self):
        systolic_number = self.systolic_number
        diastolic_number = self.diastolic_number

        if systolic_number in range(120, 129) and diastolic_number in range(80, 84):
            return PressureStatus.NORMAL
        elif systolic_number in range(130, 139) and diastolic_number in range(85, 89):
            return PressureStatus.HIGH_NORMAL
        elif systolic_number in range(140, 159) and diastolic_number in range(90, 99):
            return PressureStatus.GRADE_I_HYPERTENSION
        elif systolic_number in range(160, 179) and diastolic_number in range(100, 109):
            return PressureStatus.GRADE_II_HYPERTENSION
        elif systolic_number >= 180 and diastolic_number >= 110:
            return PressureStatus.GRADE_III_HYPERTENSION
        elif systolic_number >= 140 and diastolic_number < 90:
            return PressureStatus.ISOLATED_SYSTOLIC_HYPERTENSION
        elif systolic_number < 100 and diastolic_number < 60:
            return PressureStatus.HYPOTENSION

        return PressureStatus.OPTIMAL
