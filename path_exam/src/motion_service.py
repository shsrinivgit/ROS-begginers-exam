#! /usr/bin/env python

import rospy
from std_msgs.msg import Empty as Emp
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

class drone_service():
    def __init__(self):
        self.srv1 = rospy.Service('/my_service',Empty, self.srv_callback)
        self.pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pub2 = rospy.Publisher('drone/takeoff', Emp, queue_size=1)
        self.pub3 = rospy.Publisher('drone/land', Emp, queue_size=1)
        self.takeoff = Emp()
        self.move = Twist()
        self.land = Emp()
        rospy.sleep(0.5)

    def srv_callback(self,request):
        my_resp  =EmptyResponse()
        self.pub2.publish(self.takeoff)
        rospy.sleep(2)
        self.move.linear.x = 1
        self.pub1.publish(self.move)
        rospy.sleep(5)
        self.move.linear.x = 0
        self.move.angular.z = 0
        self.pub1.publish(self.move)
        rospy.sleep(1.5)
        self.pub3.publish(self.land)
        return my_resp

if __name__=='__main__':
    rospy.init_node('start_drone_service')
    drone_service()
    rospy.spin()


