import launch
from launch import LaunchContext, LaunchDescriptionEntity
from launch.actions import DeclareLaunchArgument, OpaqueFunction, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory

def get_wps_with_context(context: LaunchContext, drone_id):
    drone_wps_str = context.perform_substitution(LaunchConfiguration('drone_wps'))

    wps = os.path.join(
        get_package_share_directory('simplesim'),
        'waypoints',
        drone_wps_str
    )

    return [launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='controller',
        name='controller',
        parameters=[wps]
    )]


def generate_launch_description():
    drone_id = LaunchConfiguration('drone_id', default='drone_x')

    drone_id_launch_arg = DeclareLaunchArgument(
        'drone_id',
        default_value='drone_x'
    )
    drone_wps_launch_arg = DeclareLaunchArgument(
        'drone_wps',
        default_value='drone_x.yaml'
    )
        
    opaque_f_wps = OpaqueFunction(function=get_wps_with_context, args=[drone_id])

    return launch.LaunchDescription([
        drone_id_launch_arg,
        drone_wps_launch_arg,
        opaque_f_wps
    ])