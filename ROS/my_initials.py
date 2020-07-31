#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pow, sqrt
PI = 3.1415926535897

def move(speedx, distancex, isForwardx):
    
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()


    if(isForwardx):
    	vel_msg.linear.x = abs(speedx)
    else:
    	vel_msg.linear.x = -abs(speedx)

	vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        while(current_distance <= distancex):
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance= speedx*(t1-t0)
        
        if current_distance > distancex:
        	break
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

def rotate(angle, clockwise):
    
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 60

    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
       

if __name__ == '__main__':
	try:
		move(1, 1, 1)
		move(1, 2, 0)
		rotate(60, 0)
		move(1, 2, 1)
		rotate(120, 1)
		move(1, 4, 1)
		move(1, 4, 0)
		rotate(60, 1)
		move(1, 3, 1)
	except rospy.ROSInterruptException:
		pass

