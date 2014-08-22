rosh_turtlebot_demo
===================

rosh demo for ROSCON 2014. The demo contains launch files and code to run two simulated turtlebots, and have them play tag. One turtlebot moves around randomly, and the other one tries to bump into it. When a bump occurs, both robots are teleported to random locations and the game resumes.

Presentation slides: http://bit.ly/1llIKDj

## Files
### Launch
* one_robot.launch: Spawns a single turtlebot in gazebo. Also starts up the cmd vel mux.
* robots.launch: Starts up gazebo with an empty world, spawns two turtlebots (leader and follower), and starts up nodes to publish odometry/tf (since gazebo doesn't do it properly with multiple robots), random_move.py, follow.py, and reset.py (described below).

### Scripts
* publish_odom.py: Uses data from gazebo/model_states to publish odom and tf for the robots since gazebo doesn't do it properly.
* random_move.py (rosh): periodically changes leader's cmd_vel to random values
* follow.py (rosh): directs follower to move towards leader
* reset.py (rosh): waits for changes in the bumper state and teleports both robots to random locations when a bump happens

## Running
    roslaunch rosh_turtlebot_demo robots.launch 
