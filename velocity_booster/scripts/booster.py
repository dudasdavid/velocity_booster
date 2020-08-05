#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

pub = None
multiplier = 1

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    data.linear.x *= multiplier
    pub.publish(data)
    
def listener():
    global pub
    global multiplier
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    pub = rospy.Publisher('cmd_vel_boost', Twist, queue_size=10)
    rospy.init_node('booster', anonymous=True)

    multiplier = float(rospy.get_param('~boost', 2.0))

    rospy.Subscriber("cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()