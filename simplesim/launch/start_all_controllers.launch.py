import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    drone_0 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_0',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_1',
            'drone_wps': 'drone_1.yaml'
        }.items()
    )

    drone_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_2',
            'drone_wps': 'drone_2.yaml'
        }.items()
    )

    drone_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_3',
            'drone_wps': 'drone_3.yaml'
        }.items()
    )

    drone_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_4',
            'drone_wps': 'drone_4.yaml'
        }.items()
    )

    drone_5 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_5',
            'drone_wps': 'drone_5.yaml'
        }.items()
    )

    drone_6 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_6',
            'drone_wps': 'drone_6.yaml'
        }.items()
    )

    drone_7 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_7',
            'drone_wps': 'drone_7.yaml'
        }.items()
    )

    drone_8 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_8',
            'drone_wps': 'drone_8.yaml'
        }.items()
    )

    drone_9 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_9',
            'drone_wps': 'drone_9.yaml'
        }.items()
    )

    drone_10 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_10',
            'drone_wps': 'drone_10.yaml'
        }.items()
    )

    drone_11 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_11',
            'drone_wps': 'drone_11.yaml'
        }.items()
    )

    drone_12 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_12',
            'drone_wps': 'drone_12.yaml'
        }.items()
    )

    drone_13 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_13',
            'drone_wps': 'drone_13.yaml'
        }.items()
    )

    drone_14 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_14',
            'drone_wps': 'drone_14.yaml'
        }.items()
    )

    drone_15 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_15',
            'drone_wps': 'drone_15.yaml'
        }.items()
    )

    drone_16 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_16',
            'drone_wps': 'drone_16.yaml'
        }.items()
    )

    drone_17 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_17',
            'drone_wps': 'drone_17.yaml'
        }.items()
    )

    drone_18 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_18',
            'drone_wps': 'drone_18.yaml'
        }.items()
    )

    drone_19 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_19',
            'drone_wps': 'drone_19.yaml'
        }.items()
    )

    drone_20 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_20',
            'drone_wps': 'drone_20.yaml'
        }.items()
    )

    drone_21 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_21',
            'drone_wps': 'drone_21.yaml'
        }.items()
    )

    drone_22 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_22',
            'drone_wps': 'drone_22.yaml'
        }.items()
    )

    drone_23 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_23',
            'drone_wps': 'drone_23.yaml'
        }.items()
    )

    drone_24 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_24',
            'drone_wps': 'drone_24.yaml'
        }.items()
    )

    drone_25 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_25',
            'drone_wps': 'drone_25.yaml'
        }.items()
    )

    drone_26 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_26',
            'drone_wps': 'drone_26.yaml'
        }.items()
    )

    drone_27 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_27',
            'drone_wps': 'drone_27.yaml'
        }.items()
    )

    drone_28 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_28',
            'drone_wps': 'drone_28.yaml'
        }.items()
    )

    drone_29 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_29',
            'drone_wps': 'drone_29.yaml'
        }.items()
    )

    drone_30 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_30',
            'drone_wps': 'drone_30.yaml'
        }.items()
    )

    drone_31 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_31',
            'drone_wps': 'drone_31.yaml'
        }.items()
    )

    drone_32 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_32',
            'drone_wps': 'drone_32.yaml'
        }.items()
    )

    drone_33 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_controller.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_33',
            'drone_wps': 'drone_33.yaml'
        }.items()
    )

    return LaunchDescription([
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
