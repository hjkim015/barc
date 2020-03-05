#!/usr/bin/env python

import rospy

def helloworld():

	#initialize node with a default name
	rospy.init_node('default_node_name', anonymous=True)

	#Prints to INFO log
	rospy.loginfo("HELLOOOOO WOOOOORLD")

if __name__ == '__main__':
	try: 
		helloworld()
	except rospy.ROSInterruptException:
		pass


		