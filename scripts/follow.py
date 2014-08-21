#!/usr/bin/env rosh
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from tf_conversions import posemath
from math import atan2, pi
load('rosh_geometry', globals())
sleep(3)
r = Rate(10)

while ok():
    # Get the transform between the follower and leader
    to_leader = transforms.follower('leader')

    # Calculate the angle to the leader
    angle_to = atan2(to_leader.pose.position.y, to_leader.pose.position.x)

    # Fill out a Twist message, and scale velocities by distance
    vel_msg = msg.geometry_msgs.Twist()
    vel_msg.linear.x = (pi - abs(angle_to))/pi
    vel_msg.angular.z = angle_to*0.5

    # Publish the twist message
    topics.follower.commands.velocity(vel_msg)
    r.sleep()