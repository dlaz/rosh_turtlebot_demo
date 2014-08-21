#!/usr/bin/env rosh

for model_state in topics.gazebo.model_states[:]:
    for name, pose, twist in zip(model_state.name, model_state.pose, model_state.twist):
        odom = msg.nav_msgs.Odometry(
            pose=msg.geometry_msgs.PoseWithCovariance(pose=pose),
            twist=msg.geometry_msgs.TwistWithCovariance(twist=twist)
        )
        odom.child_frame_id = 'base_footprint'
        odom.header.frame_id = '/odom'
        odom.header.stamp = now()
        topics['/%s/odom' % name](odom)
