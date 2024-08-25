import sys
import many_drones_parent
import create_rviz_config
import create_simple_wps
import drone_config_generator
import create_controllers_launcher

def main():
    num = int(sys.argv[1])
    create_rviz_config.generate_file(num)
    many_drones_parent.generate_many_drones_parent(num)
    create_simple_wps.generate_drone_files(num)
    drone_config_generator.generate_drone_yaml_files(num)
    create_controllers_launcher.generate_launch_file(num)

if __name__ == "__main__":
    main()