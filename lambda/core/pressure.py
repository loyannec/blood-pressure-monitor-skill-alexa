# -*- coding: utf-8 -*-

import datetime


class Pressure:
    def __init__(self, systolic_number, diastolic_number, timestamp = datetime.datetime.now()):
        self.systolic_number = systolic_number
        self.diastolic_number = diastolic_number
        self.timestamp = timestamp

    def to_dict(self):
        return {
                'systolic_number': self.systolic_number,
                'diastolic_number': self.diastolic_number,
                'timestamp': self.timestamp.isoformat()
            }
