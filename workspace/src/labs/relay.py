#!/usr/bin/env python

import rospy
import time
from barc.msg import ECU
from labs.msg import Z_DynBkMdl 
from geometry_msgs.msg import Twist

		
# ecu command update
def measurements_callback(data):
	global relay
	d_f = data.angular.z
	acc = data.linear.x
	relay.publish( ECU(acc, d_f))
	print(data)
	
# controller node
def controller():
	global relay
	relay = rospy.Publisher('ecu', ECU, queue_size = 10)
	# initialize node
	rospy.init_node('relay', anonymous=True)
	# topic subscriptions / publications
	rospy.Subscriber('cmd_vel', Twist, measurements_callback)
	loop_rate = 50
	rate = rospy.Rate(loop_rate)

	while not rospy.is_shutdown():
		
		# wait
		rate.sleep()
	
	
	
if __name__ == '__main__':
	try:
		controller()
	except rospy.ROSInterruptException:
		pass
