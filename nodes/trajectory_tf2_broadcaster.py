#!/usr/bin/env python  
import rospy
import tf2_ros
import geometry_msgs.msg
import math
import numpy as np
from mth_class import calc_error
# import turtle_tf2_listener as listener
# from turtle_tf2_listener import Position

if __name__ == '__main__':
    
    rospy.init_node('dynamic_tf2_broadcaster')
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.frame_id = "turtle1"
    t.child_frame_id = "carrot1"

    i=0

    rate = rospy.Rate(10.0)

    trajecx = np.array([0,-3.5,-3.5, 1.5, 1.5, 3.5, 3.5,-2.5,-2.5, 1.5, 1.5,-1.0])
    trajecy = np.array([0, 0,   3.5, 3.5,-1.5,-1.5,-8.0,-8.0,-5.5,-5.5,-3.5,-3.5])   

    while not rospy.is_shutdown():
        # x = rospy.Time.now().to_sec() * math.pi
        # for i in range(0,len(trajecx)):
        # x_act = trajecx
        # if abs(trajecx(i)-listener.trans.transform.translation.x) <= trajecx*0.9:
        #        1.5+( 1.5     -        3.5)             =-2 <= 1.5*0.9    
        # if (listener.trans.transform.translation.x < 1*10^-2) and (listener.trans.transform.translation.y < 1*10^-2):
        #     i=i+1
        
        # print(Position.transformada)

        t.header.stamp = rospy.Time.now()
        t.transform.translation.x = trajecx[i]
        t.transform.translation.y = trajecy[i]
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        br.sendTransform(t)
        rate.sleep()