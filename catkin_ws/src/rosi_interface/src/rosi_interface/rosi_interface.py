from .data_topic import *

import rospy
        
callback_data_topics = {key:value for key, value in rosi_data_topics.items() if value.relation is RELATION_CALLBACK}
publish_data_topics = {key:value for key, value in rosi_data_topics.items() if value.relation is RELATION_PUBLISH}

class RosiInterface:
    """
    Main class for interaction with the robot.
    For each RosiDataTopic defined, separates between those that should be acessed via callbacks and published to.
    A decorator is provided for easy creation of callbacks and a publish function for publishing.
    Acts as a middleware for applying wrappers defined in each RosiDataTopic.
    Abstracts the creation of rospy publishers and subscribers.
    Should be initialized at the start of the program.

    Ex.:

    rosi = RosiInterface()
    """
    def __init__(self):
        self.subscribers_callbacks = {
            name: [] for name in callback_data_topics.keys()
        }

        self.subscribers = {
            name: rospy.Subscriber(
                data_topic.topic,
                data_topic.type, 
                lambda data, name : self._call_callbacks(name, data),
                callback_args=name
            ) for name, data_topic in callback_data_topics.items()
        }

        self.publishers = {
            name: rospy.Publisher(
                data_topic.topic,
                data_topic.type,
                queue_size=1
            ) for name, data_topic in publish_data_topics.items()
        }


    def callback(self, name):
        """
        Decorator for creating callbacks.

        Ex.:

        rosi = RosiInterface()
        
        @rosi.callback(CALLBACK_TIME)
        def print_time(time):
            print time
        
        """
        def callback_decorator(func):
            self.subscribers_callbacks[name].append(func)
            return func
        return callback_decorator
    
    def publish(self, name, *data):
        """
        Function for publishing to topics.

        Ex.:

        rosi = RosiInteface()

        rosi.publish(PUBLISH_KINECT_JOINT, 10)
        """
        self.publishers[name].publish(publish_data_topics[name].wrapper(*data))


    def _call_callbacks(self, name, data):
        for f in self.subscribers_callbacks[name]:
            f(callback_data_topics[name].wrapper(data))

    