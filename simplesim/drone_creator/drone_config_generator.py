import sys

def generate_drone_yaml_files(num):
    template = """
/drone_{0}:
  simulator:
    ros__parameters:
      max_speed: 20.0
      max_acc: 40.0
"""

    for i in range(num):
        content = template.format(i)
        filename = f"../config/drone_{i}.yaml"
        with open(filename, "w") as file:
            file.write(content)

if __name__ == '__main__':
    generate_drone_yaml_files(sys.argv[0])
