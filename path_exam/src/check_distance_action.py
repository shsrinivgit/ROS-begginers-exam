#! /usr/bin/env python

import rospy
import actionlib
from path_exam.msg import RecordOdomAction, RecordOdomResult, RecordOdomGoal
from record_odom import odom_reader

class act_server():
    _result = RecordOdomResult()
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/rec_pose_as', RecordOdomAction, self.result_callback, False)
        self._as.start()
        self.list = RecordOdomResult()
        self.success = True

    def result_callback(self, goal):
        self.odo = odom_reader()
        self.odom_read = self.odo.get_data()
        count = 0
        while count <20:
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                self._as.set_preempted()
                self.success = False
                break
            self.list.result_odom_array.append(self.odom_read)
            rospy.loginfo(count)
            self.odom_read = self.odo.get_data()
            rospy.sleep(1)
            count+=1
        if self.success:
            self._result.result_odom_array = self.list.result_odom_array
            print(self._result)
            self._as.set_succeeded(self._result)
            # print("Last Pose:")
            # print(self._result.result_odom_array[-1])

if __name__=='__main__':
    rospy.init_node('call_act_server')
    act_server()
    rospy.spin()