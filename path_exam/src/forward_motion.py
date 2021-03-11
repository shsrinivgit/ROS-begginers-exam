#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

class drone_forward():
    def __init__(self):
        self.pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.pub2 = rospy.Publisher('drone/takeoff', Empty, queue_size=1 )
        self.pub3 = rospy.Publisher('drone/land', Empty, queue_size=1)
        self.takeoff = Empty()
        self.move = Twist()
        self.land = Empty()
        rospy.sleep(0.5)

    def move_drone(self):
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


if __name__ == '__main__':
    rospy.init_node("drone_motion")
    rate = rospy.Rate(1)
    z = drone_forward()
    z.move_drone()
    
