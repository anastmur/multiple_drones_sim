import os
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

    drone_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_0',
            'drone_config':'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_1',
            'drone_config':'drone_1.yaml',
            'drone_wps': 'drone_1.yaml'
        }.items()
    )

    drone_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_2',
            'drone_config':'drone_2.yaml',
            'drone_wps': 'drone_2.yaml'
        }.items()
    )

    drone_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_3',
            'drone_config':'drone_3.yaml',
            'drone_wps': 'drone_3.yaml'
        }.items()
    )

    drone_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_4',
            'drone_config':'drone_4.yaml',
            'drone_wps': 'drone_4.yaml'
        }.items()
    )

    drone_5 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_5',
            'drone_config':'drone_5.yaml',
            'drone_wps': 'drone_5.yaml'
        }.items()
    )

    drone_6 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_6',
            'drone_config':'drone_6.yaml',
            'drone_wps': 'drone_6.yaml'
        }.items()
    )

    drone_7 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_7',
            'drone_config':'drone_7.yaml',
            'drone_wps': 'drone_7.yaml'
        }.items()
    )

    drone_8 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_8',
            'drone_config':'drone_8.yaml',
            'drone_wps': 'drone_8.yaml'
        }.items()
    )

    drone_9 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_9',
            'drone_config':'drone_9.yaml',
            'drone_wps': 'drone_9.yaml'
        }.items()
    )

    drone_10 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_10',
            'drone_config':'drone_10.yaml',
            'drone_wps': 'drone_10.yaml'
        }.items()
    )

    drone_11 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_11',
            'drone_config':'drone_11.yaml',
            'drone_wps': 'drone_11.yaml'
        }.items()
    )

    drone_12 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_12',
            'drone_config':'drone_12.yaml',
            'drone_wps': 'drone_12.yaml'
        }.items()
    )

    drone_13 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_13',
            'drone_config':'drone_13.yaml',
            'drone_wps': 'drone_13.yaml'
        }.items()
    )

    drone_14 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_14',
            'drone_config':'drone_14.yaml',
            'drone_wps': 'drone_14.yaml'
        }.items()
    )

    drone_15 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_15',
            'drone_config':'drone_15.yaml',
            'drone_wps': 'drone_15.yaml'
        }.items()
    )

    drone_16 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_16',
            'drone_config':'drone_16.yaml',
            'drone_wps': 'drone_16.yaml'
        }.items()
    )

    drone_17 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_17',
            'drone_config':'drone_17.yaml',
            'drone_wps': 'drone_17.yaml'
        }.items()
    )

    drone_18 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_18',
            'drone_config':'drone_18.yaml',
            'drone_wps': 'drone_18.yaml'
        }.items()
    )

    drone_19 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_19',
            'drone_config':'drone_19.yaml',
            'drone_wps': 'drone_19.yaml'
        }.items()
    )

    drone_20 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_20',
            'drone_config':'drone_20.yaml',
            'drone_wps': 'drone_20.yaml'
        }.items()
    )

    drone_21 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_21',
            'drone_config':'drone_21.yaml',
            'drone_wps': 'drone_21.yaml'
        }.items()
    )

    drone_22 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_22',
            'drone_config':'drone_22.yaml',
            'drone_wps': 'drone_22.yaml'
        }.items()
    )

    drone_23 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_23',
            'drone_config':'drone_23.yaml',
            'drone_wps': 'drone_23.yaml'
        }.items()
    )

    drone_24 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_24',
            'drone_config':'drone_24.yaml',
            'drone_wps': 'drone_24.yaml'
        }.items()
    )

    drone_25 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_25',
            'drone_config':'drone_25.yaml',
            'drone_wps': 'drone_25.yaml'
        }.items()
    )

    drone_26 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_26',
            'drone_config':'drone_26.yaml',
            'drone_wps': 'drone_26.yaml'
        }.items()
    )

    drone_27 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_27',
            'drone_config':'drone_27.yaml',
            'drone_wps': 'drone_27.yaml'
        }.items()
    )

    drone_28 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_28',
            'drone_config':'drone_28.yaml',
            'drone_wps': 'drone_28.yaml'
        }.items()
    )

    drone_29 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_29',
            'drone_config':'drone_29.yaml',
            'drone_wps': 'drone_29.yaml'
        }.items()
    )

    drone_30 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_30',
            'drone_config':'drone_30.yaml',
            'drone_wps': 'drone_30.yaml'
        }.items()
    )

    drone_31 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_31',
            'drone_config':'drone_31.yaml',
            'drone_wps': 'drone_31.yaml'
        }.items()
    )

    drone_32 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_32',
            'drone_config':'drone_32.yaml',
            'drone_wps': 'drone_32.yaml'
        }.items()
    )

    drone_33 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_33',
            'drone_config':'drone_33.yaml',
            'drone_wps': 'drone_33.yaml'
        }.items()
    )

    return LaunchDescription([
        #rviz_node,
        drone_0,
        drone_1,
        drone_2,
        drone_3,
        drone_4,
        drone_5,
        drone_6,
        drone_7,
        drone_8,
        drone_9,
        drone_10,
        drone_11,
        drone_12,
        drone_13,
        drone_14,
        drone_15,
        drone_16,
        drone_17,
        drone_18,
        drone_19,
        drone_20,
        drone_21,
        drone_22,
        drone_23,
        drone_24,
        drone_25,
        drone_26,
        drone_27,
        drone_28,
        drone_29,
        drone_30,
        drone_31,
        drone_32,
        drone_33,
    ])
