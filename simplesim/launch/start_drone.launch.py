import launch
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    drone_id = LaunchConfiguration('drone_id', default='drone_x')

    drone_id_launch_arg = DeclareLaunchArgument(
        'drone_id',
        default_value='drone_x'
    )
    fp = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='fp',
        name='fp'
    )
    simulator = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='simulator',
        name='simulator'
    )
    wps = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='wp_vis',
        name='wps'
    )

    return launch.LaunchDescription([
        drone_id_launch_arg,
        fp,
        simulator,
        wps
    ])