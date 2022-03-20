#!/usr/bin/env python

from example_svc.srv import Move,MoveResponse
import rospy

def svc_cb(req):
    print("Returning pressed key %s"%(req.str))
    return MoveResponse(req.str)

def move_svr():
    rospy.init_node('move_server')
    s = rospy.Service('move',Move,svc_cb)
    print("Ready to listen key press")
    rospy.spin()

if __name__ == "__main__":
    move_svr()