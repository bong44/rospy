#!/usr/bin/env python

from shutil import move
import sys
import keyboard
import time

from example_svc.srv import *
import rospy

def move_client(str):
    rospy.wait_for_service('move')
    print("send key request to server <<%s>>"%str)
    try:
        move=rospy.ServiceProxy('move',Move)
        resp = move(str)
        return resp.str
    except rospy.ServiceException:
        print("Service call failed")

if __name__=='__main__':
    while not rospy.is_shutdown():
        if keyboard.is_pressed("w"):
            time.sleep(0.1)
            move_client("w")
        if keyboard.is_pressed("a"):
            time.sleep(0.1)
            move_client("a")
        if keyboard.is_pressed("s"):
            time.sleep(0.1)
            move_client("s")
        if keyboard.is_pressed("d"):
            time.sleep(0.1)
            move_client("d")
