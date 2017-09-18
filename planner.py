#!/usr/bin/env python
"""This module contains a class that represents a financial planner.
The module maintains the state and performs operations on the planner
given expenses for the week.

"""


class Planner(object):
    """This class maintains and updates info regarding the state of the
    financial planner.

    """
    def __init__(self):
        # Try to open the file with existing data
        try:
            file = open("data.dat", "r+")
            self._init_attrbs(file)
            file.close()
        except:
            file = open("data.dat", "w+")
            self.weeks_left = 0.0
            self.total_groceries = 0.0
            self.total_investing = 0.0
            self.total_leisure = 0.0
            file.close()

    def _init_attrbs(self, file):
        """File format: weeks_left, total_groceries,
        total_investing, total_leisure

        """
        line = file.read()
        elements = line.split(",")
        self.weeks_left = elements[0]
        self.total_groceries = elements[1]
        self.total_investing = elements[2]
        self.total_leisure = elements[3]


if __name__ == '__main__':
    Planner()
