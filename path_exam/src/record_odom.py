#! /usr/bin/env python

import rospy
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

class odom_reader():
    def __init__(self):
        self.sub=rospy.Subscriber('/drone/gt_pose',Pose ,self.callback)
        self.odomdata=Pose()
        rospy.sleep(2)
        rospy.loginfo("initiated!!")
    def callback(self,data):
        self.odomdata=data
    def get_data(self):
        return self.odomdata

if __name__=="__main__":
    rospy.init_node('odom_reader')
    z = odom_reader()
    z.get_data()