#!/usr/bin/env  python
# license removed for brevity

import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float64 

roll=0
pitch=0
yaw=0

def callback(data):
	sinr_cosp = 2*(data.data[0] * data.data[1] + data.data[2] * data.data[3])
	cosr_cosp = 1-2*(data.data[1]**2 + data.data[2]**2)
	roll = np.arctan2(sinr_cosp, cosr_cosp)

	sinp = 2 * (data.data[0] * data.data[2] - data.data[3] * data.data[1])
	pitch = np.where(np.abs(sinp) >= 1,
					np.sign(sinp) * np.pi / 2,
					np.arcsin(sinp))

	siny_cosp = 2 * (data.data[0] * data.data[3] + data.data[1] * data.data[2])
	cosy_cosp = 1 - 2 * (data.data[2]**2 + data.data[3]**2)
	yaw = np.arctan2(siny_cosp, cosy_cosp)

def nav():
	rospy.init_node('Converter', anonymous=True)
	
	rospy.Subscriber("topic1", Float64, callback)

	rospy.spin()

	pub = rospy.Publisher('topic2', Float64, queue_size=10)
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		euler_angles = [roll, pitch, yaw]
		rospy.loginfo(euler_angles)
		pub.Publish(euler_angles)
		rate.sleep()


if __name__ == '__main__':
    try:
        nav()
    except rospy.ROSInterruptException:
        pass
	

