#!/usr/bin/env  python
# license removed for brevity

import rospy
import numpy as np
from beginner_tutorials.msg import quat
from beginner_tutorials.msg import rollpitchyaw 

rpy = rollpitchyaw

def callback(data):
	val = data
	sinr_cosp = 2*(val.x * val.y + val.z * val.w)
	cosr_cosp = 1-2*(val.y**2 + val.z**2)
	rpy.roll = np.arctan2(sinr_cosp, cosr_cosp)

	sinp = 2 * (val.x * val.z - val.w * val.y)
	rpy.pitch = np.where(np.abs(sinp) >= 1,
					np.sign(sinp) * np.pi / 2,
					np.arcsin(sinp))

	siny_cosp = 2 * (val.x * val.w + val.y * val.z)
	cosy_cosp = 1 - 2 * (val.z**2 + val.w**2)
	rpy.yaw = np.arctan2(siny_cosp, cosy_cosp)

	while not rospy.is_shutdown():
		pub = rospy.Publisher('topic2', rollpitchyaw, queue_size=10)
		pub.Publish(rpy)
		rate.sleep()

	


rospy.init_node('Converter', anonymous=True)
rate = rospy.Rate(10)
rospy.Subscriber('topic1', quat, callback)

rsopy.spin()
