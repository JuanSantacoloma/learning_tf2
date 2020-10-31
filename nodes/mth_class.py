#!/usr/bin/python

import rospy

class calc_error:

    def __init__(self):
        # Atributos
        # Para realizar un broadcast
        self.broadcts  = tf2_ros.TransformBroadcaster()
        self.transform = TransformStamped()

        # Para realizar la escucha "listener"
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

        # Subscribers
        rospy.Subscriber("/ar_pose_marker", numpy_msg(AlvarMarkers), self.Marker_Callback, queue_size=10 )

        