#!/usr/bin/env python
import tf
import rospy
from geometry_msgs.msg import PoseWithCovariance, TwistWithCovariance
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import ModelStates

br = None
pubs = None

def model_states_cb(model_state):
    for name, pose, twist in zip(model_state.name, model_state.pose, model_state.twist):
        odom = Odometry(
            pose=PoseWithCovariance(pose=pose),
            twist=TwistWithCovariance(twist=twist)
        )
        odom.child_frame_id = name
        odom.header.frame_id = '/odom'
        odom.header.stamp = rospy.Time.now()
        pubs[name].publish(odom)
        br.sendTransform(
            (pose.position.x, pose.position.y, pose.position.z),
            (pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w),
            rospy.Time.now(),
            name,
            '/odom'
        )

if __name__ == '__main__':
    rospy.init_node('publish_odom')
    br = tf.TransformBroadcaster()
    rospy.Subscriber('gazebo/model_states', ModelStates, model_states_cb)
    pubs = {
        'ground_plane'  : rospy.Publisher('ground_plane/odom', Odometry),
        'leader'        : rospy.Publisher('leader/odom', Odometry),
        'follower'      : rospy.Publisher('follower/odom', Odometry)
    }
    rospy.spin()