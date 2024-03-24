
## How To Run

1. Build the package with colcon.
2. Launch the `robot_state_publisher` launch file with `ros2 launch stormfield rsp.launch.py` or `ros2 launch stormfield rsp_sim.launch.py`.
3. Launch `joint_state_publisher_gui` with `ros2 run joint_state_publisher_gui joint_state_publisher_gui`. You may need to install it if you don't have it already.
4. Launch RViz with `rviz2`
5. launch gazebo using `ros2 launch gazebo_ros gazebo.launch.py`
6. spawn robot using `ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity cloudkat_v1`

To replicate the RViz display shown in the video you will want to
- Set your fixed frame to `world`
- Add a `RobotModel` display, with the topic set to `/robot_description`, and alpha set to 0.8
- Add a `TF` display with names enabled.