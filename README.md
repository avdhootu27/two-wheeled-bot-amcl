# two-wheeled-bot-amcl

In this project I am navigating a two wheeled bot autonomously in a closed environment using AMCL in ros-noetic. The [simulation_gazebo](https://github.com/avdhootu27/two-wheeled-bot-autonomous-navigation/tree/master/simulation_gazebo) package used here is taken from [bitbucket](https://bitbucket.org/theconstructcore/simulation_gazebo/src/master/).

The URDF of the robot is created using Autodesk's Fusion360.

## Steps 
#### To run gazebo and rviz (run each command in different terminals)
```
roslaunch my2wbnew_description gazebo.launch
roslaunch my2wbnew_description display.launch
```
#### For gmapping
```
roslaunch my2wbnew_description gmapping.launch
```
#### For autonomous navigation
```
roslaunch my2wbnew_description navigation.launch
```
