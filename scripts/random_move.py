#!/usr/bin/env rosh
import random

def rand_cmd_vel():
    vel_msg = msg.geometry_msgs.Twist()
    vel_msg.linear.x = 1-2*random.random()
    vel_msg.angular.z = 1-2*random.random()
    return vel_msg

r = Rate(10)
last_change = 0
vel = rand_cmd_vel()
while ok():
    # pick a new velocity every 5 seconds
    t = int(now().to_sec())
    if (t % 5 == 0) and last_change != t:
        vel = rand_cmd_vel()
        last_change = t
        print vel
    topics.leader.commands.velocity(vel)
    r.sleep()
