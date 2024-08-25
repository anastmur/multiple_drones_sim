import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
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

    poses = os.path.join(
        get_package_share_directory('simplesim'),
        'waypoints',
        'crazyflies_2_2_3.yaml'
    )

    replicator = launch_ros.actions.Node(
        namespace='drone_0',
        package='simplesim',
        executable='replicator',
        name='replicator',
        parameters=[poses]
    )

    return launch.LaunchDescription([
        # rviz_node,
        replicator
    ])
