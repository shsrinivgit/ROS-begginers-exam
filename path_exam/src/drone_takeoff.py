#! /usr/bin/env python
import rospy
from std_msgs.msg import Empty

class drone_move():
    def __init__(self):
        self.pub2 = rospy.Publisher('drone/takeoff', Empty, queue_size=1 )
        self.takeoff = Empty()
        rospy.sleep(1)

    def move_it(self):
        self.pub2.publish(self.takeoff)
        rospy.sleep(5)
if __name__=='__main__':
    rospy.init_node('drone_move')
    x = drone_move()
    x.move_it()
