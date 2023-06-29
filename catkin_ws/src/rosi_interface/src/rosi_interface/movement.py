"""
Movement is hard.
This file aims to help with that.
"""

from data_topic import *

import std_msgs.msg
import rosi_defy.msg


# Node IDs for each wheel
TRACTION_UP_RIGHT = 1
TRACTION_DOWN_RIGHT = 2
TRACTION_UP_LEFT = 3
TRACTION_DOWN_LEFT = 4

def traction_speed_wrapper(velocity_up_right=None, velocity_up_left=None, velocity_down_right=None, velocity_down_left=None):
    """
    Abstracts over the creation of RosiMovementArray for wheel traction controls
    """
    # TODO: make this actually meaningful
    header = std_msgs.msg.Header()

    movements = []

    if velocity_up_right is not None:
        movements.append(rosi_defy.msg.RosiMovement(TRACTION_UP_RIGHT, velocity_up_right))

    if velocity_up_left is not None:
        movements.append(rosi_defy.msg.RosiMovement(TRACTION_UP_LEFT, velocity_up_left))

    if velocity_down_right is not None:
        movements.append(rosi_defy.msg.RosiMovement(TRACTION_DOWN_RIGHT, velocity_down_right))

    if velocity_down_left is not None:
        movements.append(rosi_defy.msg.RosiMovement(TRACTION_DOWN_LEFT, velocity_down_left))


    return rosi_defy.msg.RosiMovementArray(header, movements)


# Node IDs for each arm
ARM_UP_RIGHT = 1
ARM_DOWN_RIGHT = 2
ARM_UP_LEFT = 3
ARM_DOWN_LEFT = 4
    
def arms_speed_wrapper(velocity_up_right=None, velocity_up_left=None, velocity_down_right=None, velocity_down_left=None):
    """
    Abstracts over the creation of RosiMovementArray for arm controls
    """
    # TODO: make this actually meaningful
    header = std_msgs.msg.Header()

    movements = []

    if velocity_up_right is not None:
        movements.append(rosi_defy.msg.RosiMovement(ARM_UP_RIGHT, velocity_up_right))

    if velocity_up_left is not None:
        movements.append(rosi_defy.msg.RosiMovement(ARM_UP_LEFT, velocity_up_left))

    if velocity_down_right is not None:
        movements.append(rosi_defy.msg.RosiMovement(ARM_DOWN_RIGHT, velocity_down_right))

    if velocity_down_left is not None:
        movements.append(rosi_defy.msg.RosiMovement(ARM_DOWN_LEFT, velocity_down_left))


    return rosi_defy.msg.RosiMovementArray(header, movements)
