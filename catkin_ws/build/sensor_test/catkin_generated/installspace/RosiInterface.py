#!/usr/bin/env python2
import rospy
import std_msgs.msg as std_msg

class RosiInterface:
    def __init__(self):
        self.kinect_joint_callbacks = []
        self.kinect_joint_subscriber = rospy.Subscriber(
            '/rosi/kinect_joint',
            std_msg.Float32,
            callback = lambda msg: self._execute_array(self.kinect_joint_callbacks, msg))
        

    @staticmethod
    def _execute_array(arr, arg):
        for f in arr:
            f(arg)


    def kinect_joint(self, func):
        self.kinect_joint_callbacks.append(func)



if __name__ == '__main__':
    try:
        rospy.init_node('test_node', anonymous=True)

        rosi = RosiInterface()

        @rosi.kinect_joint
        def print_data(data):
            print(data)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass