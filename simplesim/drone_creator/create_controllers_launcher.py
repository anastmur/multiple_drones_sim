def generate_launch_file(num):
    header = """import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
"""

    drone_template = """
    drone_{0} = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={{
            'drone_id': 'drone_{0}',
            'drone_wps': 'drone_{0}.yaml'
        }}.items()
    )
"""

    footer = """
    return LaunchDescription([
"""

    for i in range(num):
        footer += f"        drone_{i},\n"

    footer += """    ])
"""

    with open("../launch/start_all_controllers.launch.py", "w") as file:
        file.write(header)
        for i in range(num):
            file.write(drone_template.format(i))
        file.write(footer)

