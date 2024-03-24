import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():
    # Specify the name of the package and path to the URDF file within the package
    pkg_name = 'stormfield'
    urdf_file_subpath = 'description/cloudkat_v1.urdf'

    # Declare a launch argument to specify whether to use simulated time
    use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )

    # Use the LaunchConfiguration to read the value of the 'use_sim_time' argument
    use_sim_time_flag = LaunchConfiguration('use_sim_time')

    # Configure the node to publish the robot state
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        namespace='',  # Use an empty namespace to publish all joints
        parameters=[{'use_sim_time': use_sim_time_flag}],
        remappings=[('/tf', '/tf'), ('/tf_static', '/tf_static')],
        arguments=[urdf_file_subpath]  # Specify the URDF file as an argument
    )

    # Add a condition to the robot_state_publisher node so that it only runs when use_sim_time is set to true
    robot_state_publisher_condition = IfCondition(use_sim_time_flag)

    # Define the launch description
    return LaunchDescription([
        use_sim_time,
        LogInfo(
            condition=robot_state_publisher_condition,
            msg="Running robot_state_publisher with sim_time."
        ),
        node_robot_state_publisher
    ])
