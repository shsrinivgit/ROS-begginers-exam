#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from forward_motion import drone_forward
from record_odom import odom_reader

class my_drone_service():
    def __init__(self):
        self.srv1 = rospy.Service('/my_service',Trigger, self.srv_callback)
        self.topic_move = drone_forward()
        self.odom = odom_reader()
        self.odo = self.odom.get_data()
        self.first_pos = self.odo.position.x

    def srv_callback(self,request):
        my_resp = TriggerResponse()
        self.topic_move.move_drone()
        rospy.sleep(1)
        self.odom = odom_reader()
        self.odo = self.odom.get_data()
        self.last_pos = self.odo.position.x
        self.dist = self.last_pos - self.first_pos
        my_resp.success = True
        my_resp.message = "The drone has moved {} meters.".format(self.dist)
        return my_resp

if __name__=='__main__':
    rospy.init_node('start_drone_service')
    y = my_drone_service()
    rospy.spin()