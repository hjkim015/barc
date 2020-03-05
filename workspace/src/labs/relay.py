#!/usr/bin/env python

import rospy
import time
from barc.msg import ECU
from labs.msg import Z_DynBkMdl 
from geometry_msgs.msg import Twist

	
# initialize state
x = 0
y = 0
v_x = 0
v_y = 0
	
# ecu command update
def measurements_callback(data):
 	print(data)
	 	
# Insert your PID longitudinal controller here: since you are asked to do longitudinal control,  the steering angle d_f can always be set to zero. Therefore, the control output of your controller is essentially longitudinal acceleration acc.
# ==========PID longitudinal controller=========#
	
# ==========end of the controller==============#
	
# controller node
def controller():
	# initialize node

	rospy.init_node('relay', anonymous=True)
	
	# topic subscriptions / publications
	rospy.Subscriber('cmd_vel', Twist, measurements_callback)
	state_pub = rospy.Publisher('ecu', ECU, queue_size = 10)
	
	# set node rate
	# loop_rate = 50
	# dt = 1.0 / loop_rate
	# rate = rospy.Rate(loop_rate)
	# t0 = time.time()
	
	# # set initial conditions 
	# d_f = 0
	# acc = 0
	
	# # reference speed 
	# v_ref = 8 # reference speed is 8 m/s
	
	# # Initialize the PID controller with your tuned gains
	
	
	while not rospy.is_shutdown():
		# acceleration calculated from PID controller.

	 
	 	# steering angle
	 	#d_f = 0.0
	
		# publish information
	 	#state_pub.publish( ECU(acc, d_f) )
	
		# wait
		rate.sleep()
	
if __name__ == '__main__':
	try:
		controller()
	except rospy.ROSInterruptException:
		pass
