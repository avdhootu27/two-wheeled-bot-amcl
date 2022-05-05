#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

cmd_pub = rospy.Publisher('cmd_vel_new', Twist, queue_size=1)

def callback(cmd):
	x = cmd.linear.x
	z = cmd.angular.z
	if(abs(cmd.angular.z) > 0.2):
		x = 0

	vel = Twist()
	vel.linear.x = x
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = z

	cmd_pub.publish(vel)
	print("------")
	print(x)
	print(z)


def listener():
    rospy.init_node('cmd_publisher')
    print('Initialized')
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()