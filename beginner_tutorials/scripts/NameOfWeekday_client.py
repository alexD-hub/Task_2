#!/usr/bin/env python

from __future__ import print_function

import rospy
import string
import random
import datetime
from beginner_tutorials.srv import *


def day_client(day, month):
    rospy.wait_for_service('name_week')
    try:
        name_week = rospy.ServiceProxy('name_week', GetNameOfWeek)
        resp1 = name_week(day, month)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == "__main__":
    rospy.init_node('client', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():

        day_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        month_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        random.shuffle((day_list) and (month_list))
        name = (day_list[0] and month_list[0])

        day = random.randrange(1, 31)
        month = random.randrange(1, 12)
        print(day_client(day, month))
        rate.sleep()
