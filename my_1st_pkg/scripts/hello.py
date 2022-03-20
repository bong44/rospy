#!/usr/bin/env python

import rospy
import keyboard

from std_msgs.msg import String

if __name__=='__main__':

	try:
		rospy.init_node('hello_ros')
		p = rospy.Publisher('hello',String,queue_size=1)
		r = rospy.Rate(1)
		flag = False

		while not rospy.is_shutdown():
			if keyboard.is_pressed("w"):
				msg = "you pressed~ %s" % "w"
			if keyboard.is_pressed("a"):
				msg = "you pressed~ %s" % "a"
			if keyboard.is_pressed("s"):
				msg = "you pressed~ %s" % "s"
			if keyboard.is_pressed("d"):
				msg = "you pressed~ %s" % "d"
			if flag:
				print(msg)
				p.publish(msg)
			r.sleep()
	except rospy.ROSInterruptException:
		pass
