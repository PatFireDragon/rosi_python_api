from __future__ import print_function

import rospy

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg
import rosi_defy.msg


identity = lambda x: x

class RosiDataTopic:
    def __init__(self, topic, type, wrapper=identity):
        self.topic = topic
        self.type = type
        self.wrapper = wrapper


data_topics = {
    'arms_joints_position': RosiDataTopic('/rosi/arms_joints_position', rosi_defy.msg.RosiMovementArray),
    'kinect_joint': RosiDataTopic('/rosi/kinect_joint', std_msgs.msg.Float32),
    'gps': RosiDataTopic('/sensor/gps', sensor_msgs.msg.NavSatFix),
    'imu': RosiDataTopic('/sensor/imu', sensor_msgs.msg.Imu),
    'kinect_depth': RosiDataTopic('/sensor/kinect_depth', sensor_msgs.msg.Image),
    'kinect_rgb': RosiDataTopic('/sensor/kinect_rgb', sensor_msgs.msg.Image),
    'kinect_info': RosiDataTopic('/sensor/kinect_info', sensor_msgs.msg.CameraInfo),
    'velodyne': RosiDataTopic('/sensor/velodyne', sensor_msgs.msg.PointCloud2),
    'hokuyo': RosiDataTopic('/sensor/hokuyo', rosi_defy.msg.HokuyoReading),
    'ur5toolCam': RosiDataTopic('/sensor/ur5toolCam', sensor_msgs.msg.Image),
    'time': RosiDataTopic('/simulation/time', std_msgs.msg.Float32),
    'jointsPositionCurrentState': RosiDataTopic('/ur5/jointsPositionCurrentState', rosi_defy.msg.ManipulatorJoints),
    'forceTorqueSensorOutput': RosiDataTopic('/ur5/forceTorqueSensorOutput', geometry_msgs.msg.TwistStamped)
}
        

class RosiCallbackInterface:
    def __init__(self):
        self.subscribers_callbacks = {
            name: [] for name in data_topics.keys()
        }

        self.subscribers = {
            name: rospy.Subscriber(
                data_topic.topic,
                data_topic.type, 
                lambda data, name : self._call_callbacks(name, data),
                callback_args=name
            ) for name, data_topic in zip(data_topics.keys(), data_topics.values())
        }


    def data(self, name):
        def data_decorator(func):
            self.subscribers_callbacks[name].append(func)
            return func
        return data_decorator
    

    def _call_callbacks(self, name, *args):
        for f in self.subscribers_callbacks[name]:
            f(*args)

    