# -*- coding: utf-8 -*-

from enum import Enum

class PressureStatus(Enum):
    OPTIMAL = 2
    NORMAL = 1
    HIGH_NORMAL = 0
    GRADE_I_HYPERTENSION = -1
    GRADE_II_HYPERTENSION = -2
    GRADE_III_HYPERTENSION = -3
    ISOLATED_SYSTOLIC_HYPERTENSION = -4

    def description(self):
        descriptions = {
            PressureStatus.OPTIMAL.value: 'Optimal',
            PressureStatus.NORMAL.value: 'Normal',
            PressureStatus.HIGH_NORMAL.value: 'High normal',
            PressureStatus.GRADE_I_HYPERTENSION.value: 'Grade I hypertension',
            PressureStatus.GRADE_II_HYPERTENSION.value: 'Grade 2 hypertension',
            PressureStatus.GRADE_III_HYPERTENSION.value: 'Grade 3 hypertension',
            PressureStatus.ISOLATED_SYSTOLIC_HYPERTENSION.value: 'Isolated systolic hypertension'
        }
        return descriptions[self.value]
