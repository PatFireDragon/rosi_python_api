from .movement import traction_speed_wrapper, arms_speed_wrapper

import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg
import rosi_defy.msg

identity = lambda x: x

class Iota:
    def __init__(self):
        self.n = None

    def __call__(self, start=None):
        if start is not None:
            self.n = start
        else:
            self.n += 1

        return self.n
    
iota = Iota()

CALLBACK_ARMS_JOINTS_POSITION = iota(0)
CALLBACK_KINECT_JOINT = iota()
CALLBACK_GPS = iota()
CALLBACK_IMU = iota()
CALLBACK_KINECT_DEPTH = iota()
CALLBACK_KINECT_RGB = iota()
CALLBACK_KINECT_INFO = iota()
CALLBACK_VELODYNE = iota()
CALLBACK_HOKUYO = iota()
CALLBACK_UR5_TOOL_CAM = iota()
CALLBACK_TIME = iota()
CALLBACK_JOINTS_POSITION_CURRENT_STATE = iota()
CALLBACK_FORCE_TORQUE_SENSOR_OUTPUT = iota()

PUBLISH_ARMS_SPEED = iota()
PUBLISH_TRACTION_SPEED = iota()
PUBLISH_KINECT_JOINT = iota()
PUBLISH_UR5_JOINTS_POS_TARGET = iota()

RELATION_CALLBACK = iota(0)
RELATION_PUBLISH = iota()


class RosiDataTopic:
    """
    Class that contains a basic abstraction over the robot's interactable properties over subscribable/publishable topics.

    Arguments:
    topic -- the topic that is used to access the data in ROS;
    type -- the type of data that is used in the topic;
    relation -- either CALLBACK or PUBLISH, indicating the type of interaction with the topic;
    wrapper -- possible preprocessing in transmitting the data (ex.: converting ros images to opencv format).
    """
    def __init__(self, topic, type, relation, wrapper=identity):
        self.topic = topic
        self.type = type
        self.relation = relation
        self.wrapper = wrapper


# RosiDataTopics used by the robot
rosi_data_topics = {
    CALLBACK_ARMS_JOINTS_POSITION: RosiDataTopic('/rosi/arms_joints_position', rosi_defy.msg.RosiMovementArray, RELATION_CALLBACK),
    CALLBACK_KINECT_JOINT : RosiDataTopic('/rosi/kinect_joint', std_msgs.msg.Float32, RELATION_CALLBACK),
    CALLBACK_GPS: RosiDataTopic('/sensor/gps', sensor_msgs.msg.NavSatFix, RELATION_CALLBACK),
    CALLBACK_IMU: RosiDataTopic('/sensor/imu', sensor_msgs.msg.Imu, RELATION_CALLBACK),
    CALLBACK_KINECT_DEPTH: RosiDataTopic('/sensor/kinect_depth', sensor_msgs.msg.Image, RELATION_CALLBACK),
    CALLBACK_KINECT_RGB : RosiDataTopic('/sensor/kinect_rgb', sensor_msgs.msg.Image, RELATION_CALLBACK),
    CALLBACK_KINECT_INFO: RosiDataTopic('/sensor/kinect_info', sensor_msgs.msg.CameraInfo, RELATION_CALLBACK),
    CALLBACK_VELODYNE: RosiDataTopic('/sensor/velodyne', sensor_msgs.msg.PointCloud2, RELATION_CALLBACK),
    CALLBACK_HOKUYO : RosiDataTopic('/sensor/hokuyo', rosi_defy.msg.HokuyoReading, RELATION_CALLBACK),
    CALLBACK_UR5_TOOL_CAM: RosiDataTopic('/sensor/ur5toolCam', sensor_msgs.msg.Image, RELATION_CALLBACK),
    CALLBACK_TIME: RosiDataTopic('/simulation/time', std_msgs.msg.Float32, RELATION_CALLBACK),
    CALLBACK_JOINTS_POSITION_CURRENT_STATE: RosiDataTopic('/ur5/jointsPositionCurrentState', rosi_defy.msg.ManipulatorJoints, RELATION_CALLBACK),
    CALLBACK_FORCE_TORQUE_SENSOR_OUTPUT : RosiDataTopic('/ur5/forceTorqueSensorOutput', geometry_msgs.msg.TwistStamped, RELATION_CALLBACK),

    PUBLISH_ARMS_SPEED: RosiDataTopic('/rosi/command_arms_speed', rosi_defy.msg.RosiMovementArray, RELATION_PUBLISH, arms_speed_wrapper),
    PUBLISH_TRACTION_SPEED: RosiDataTopic('/rosi/command_traction_speed', rosi_defy.msg.RosiMovementArray, RELATION_PUBLISH, traction_speed_wrapper),
    PUBLISH_KINECT_JOINT: RosiDataTopic('/rosi/command_kinect_joint', std_msgs.msg.Float32, RELATION_PUBLISH),
    PUBLISH_UR5_JOINTS_POS_TARGET: RosiDataTopic('/ur5/jointsPosTargetCommand', rosi_defy.msg.ManipulatorJoints, RELATION_PUBLISH)
}