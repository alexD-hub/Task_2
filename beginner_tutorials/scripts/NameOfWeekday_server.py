#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import GetNameOfWeek, GetNameOfWeekResponse
import rospy
import random
from datetime import date


def get_name_of_week_result(req):
    print("date- ", req.day)
    print("month- ", req.month)

    name_week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

    if ((req.day > 1 and req.day < 31) or (req.month > 1 and req.month < 12)):
	result = date(2020, req.month, req.day).isocalendar()[2]
        response = name_week[result]
    else:
        response = 'Day or month out of range'

    return GetNameOfWeekResponse(response)


def name_of_week_server():
    rospy.init_node('name_of_week_server')
    s = rospy.Service('name_week', GetNameOfWeek, get_name_of_week_result)
    print("Ready to name day of week.")
    rospy.spin()


if __name__ == "__main__":
    name_of_week_server()
