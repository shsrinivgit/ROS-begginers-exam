#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest
import actionlib
from path_exam.msg import RecordOdomAction, RecordOdomGoal, RecordOdomResult
class main_program():
    def __init__(self):
        print('initiated')
    
    def call_everything(self):
        act = self.action_cli()
        self.serv_client()
        print(act)
        # print("Last Pose:")
        # print(self._result.result_odom_array[-1])

    def serv_client(self):
        rospy.wait_for_service('/my_service')
        my_drone_service = rospy.ServiceProxy('/my_service', Trigger)
        my_drone_object = TriggerRequest()
        result = my_drone_service(my_drone_object)
        return result

    def action_cli(self):
        self.client = actionlib.SimpleActionClient('/rec_pose_as', RecordOdomAction)
        # # waits until the action server is up and running
        rospy.loginfo('Waiting for action Server')
        self.client.wait_for_server()
        goal = RecordOdomGoal()
        self.client.send_goal(goal,done_cb= self.results_callback)
        #self.client.wait_for_result()
        return self.client.get_result()
    
    def results_callback(self, status,result):
        print("Last Pose:")
        print(result[-1])
        
if __name__=="__main__":
    rospy.init_node('main_program_node')
    xy = main_program()
    xy.call_everything()
    