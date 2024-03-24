import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    ld = LaunchDescription()
    package_name = 'kloudkat'

    # Include robot state publisher node
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(package_name), 'launch', 'rsp.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include Gazebo launch with a specific world file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': '/home/mta/ros2_ws/src/kloudkat/worlds/new_farm.world'}.items(),
    )

    # Spawn kloudkat rover
    spawn_entity = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'kloudkat'],
        output='screen'
    )

    # Control node
    control_node = Node(
        package='kk_ctrl_station',  
        executable='control_rover',         
        output='screen',
    )  
    # Video feed node
    crop_cam = Node(
        package='kk_ctrl_station',  
        executable='crop_cam',         
        output='screen',
    )
    front_cam = Node(
        package='kk_ctrl_station',  
        executable='front_cam',         
        output='screen',
    )
    back_cam = Node(
        package='kk_ctrl_station',  
        executable='back_cam',         
        output='screen',
    )
    
    # Add all nodes to the launch description
    ld.add_action(rsp)
    ld.add_action(gazebo)
    ld.add_action(spawn_entity)
    ld.add_action(control_node)
    ld.add_action(crop_cam)
    ld.add_action(front_cam)
    ld.add_action(back_cam)

    return ld
