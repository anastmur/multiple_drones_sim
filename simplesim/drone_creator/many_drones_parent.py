import sys

def generate_many_drones_parent(num):
    header = """import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_file = 'auto_many_drones_config.rviz'
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
"""

    drone_template = """
    drone_{0} = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={{
            'drone_id': 'drone_{0}',
            'drone_config':'drone_{0}.yaml',
            'drone_wps': 'drone_{0}.yaml'
        }}.items()
    )
"""

    footer = """
    return LaunchDescription([
        #rviz_node,
"""

    for i in range(num):
        footer += f"        drone_{i},\n"

    footer += """    ])
"""

    with open("../launch/many_drones_parent.launch.py", "w") as file:
        file.write(header)
        for i in range(num):
            file.write(drone_template.format(i))
        file.write(footer)

