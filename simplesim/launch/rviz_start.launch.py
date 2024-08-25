import os
import launch_ros
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_file = 'zoomed_orbit.rviz'
    config = os.path.join(
        get_package_share_directory('simplesim'),
        'rviz',
        config_file
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2', 
        name='rviz2',
        output='screen',
        arguments=['-d' + config]
    )

    return LaunchDescription([
    rviz_node,
    ])