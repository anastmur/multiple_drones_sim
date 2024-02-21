import launch
from launch import LaunchContext, LaunchDescriptionEntity
from launch.actions import DeclareLaunchArgument, OpaqueFunction, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory


# drone_config_str = 'drone_x.yaml'


def get_configuration_with_context(context: LaunchContext, drone_id):
    drone_config_str = context.perform_substitution(LaunchConfiguration('drone_config'))
    
    config = os.path.join(
        get_package_share_directory('simplesim'),
        'config',
        drone_config_str
    )

    return [launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='simulator',
        name='simulator',
        parameters=[config]
    )]

def generate_launch_description():
    drone_id = LaunchConfiguration('drone_id', default='drone_x')

    drone_id_launch_arg = DeclareLaunchArgument(
        'drone_id',
        default_value='drone_x'
    )

    drone_config_launch_arg = DeclareLaunchArgument(
        'drone_config',
        default_value='drone_x.yaml'
    )

    opaque_f = OpaqueFunction(function=get_configuration_with_context, args=[drone_id])

    fp = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='fp',
        name='fp'
    )
    
    wps = launch_ros.actions.Node(
        namespace=drone_id,
        package='simplesim',
        executable='wp_vis',
        name='wps'
    )

    return launch.LaunchDescription([
        drone_id_launch_arg,
        drone_config_launch_arg,
        fp,
        opaque_f,
        wps,
        #ExecuteProcess(cmd=['echo', str(drone_config_str)],
                       #output='screen'),
    ])