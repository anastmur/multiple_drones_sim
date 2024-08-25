import os
import launch_ros
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config_file = 'mult_config.rviz'
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
        'drone_config': 'drone_0.yaml',
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
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
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_34 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_34',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_35 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_35',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_36 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_36',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_37 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_37',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_38 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_38',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_39 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_39',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_40 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_40',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_41 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_41',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_42 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_42',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_43 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_43',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_44 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_44',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_45 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_45',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_46 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_46',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_47 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_47',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_48 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_48',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )

    drone_49 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('simplesim'),
                'launch',
                'start_drone.launch.py'
            ])
        ]),
        launch_arguments={
            'drone_id': 'drone_49',
            'drone_config': 'drone_0.yaml',
            'drone_wps': 'drone_0.yaml'
        }.items()
    )


    return LaunchDescription([
            rviz_node,
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
            # drone_30,
            # drone_31,
            # drone_32,
            # drone_33,
            # drone_34,
            # drone_35,
            # drone_36,
            # drone_37,
            # drone_38,
            # drone_39,
            # drone_40,
            # drone_41,
            # drone_42,
            # drone_43,
            # drone_44,
            # drone_45,
            # drone_46,
            # drone_47,
            # drone_48,
            # drone_49,
        ])