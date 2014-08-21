#!/usr/bin/env rosh
import random, math

for bump in topics.follower.events.bumper[:]:
    if bump.state:
        print 'Bump! Resetting.'

        follower = msg.gazebo_msgs.ModelState(model_name='follower')
        follower.pose.position.x = random.random()*10
        follower.pose.position.y = random.random()*10
        follower.pose.orientation.w = 1
        services.gazebo.set_model_state(follower)

        leader = msg.gazebo_msgs.ModelState(model_name='leader')
        leader.pose.position.x = random.random()*10
        leader.pose.position.y = random.random()*10
        leader.pose.orientation.w = 1
        services.gazebo.set_model_state(leader)