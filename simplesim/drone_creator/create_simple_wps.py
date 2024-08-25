import sys

def generate_drone_files(num):
    base_waypoints = [
        '0.0;0.0;0.0',
        '40.0;20.0;0.0',
        '80.0;-20.0;0.0',
        '120.0;0.0;0.0',
        '160.0;20.0;0.0',
        '200.0;-20.0;0.0',
        '240.0;0.0;0.0',
        # '280.0;20.0;0.0',
        # '320.0;-20.0;0.0',
        # '360.0;0.0;0.0',
        # '400.0;20.0;0.0',
        # '440.0;-20.0;0.0'
        # '480.0;0.0;0.0',
        # '520.0;20.0;0.0',
        # '560.0;-20.0;0.0',
        # '600.0;0.0;0.0',
        # '640.0;20.0;0.0',
        # '680.0;-20.0;0.0',
        # '720.0;0.0;0.0',
        # '760.0;20.0;0.0',
        # '800.0;-20.0;0.0',
        # '840.0;0.0;0.0',
        # '880.0;20.0;0.0',
        # '920.0;-20.0;0.0',
        # '960.0;0.0;0.0',
        # '1000.0;20.0;0.0',
        # '1040.0;-20.0;0.0',
    ]

    for i in range(num):
        drone_name = f"drone_{i}"
        waypoints = []
        
        increment = i * 20.0
        for waypoint in base_waypoints:
            parts = waypoint.split(';')
            parts[-1] = str(float(parts[-1]) + increment)
            waypoints.append(';'.join(parts))

        content = f"""
/{drone_name}:
  controller:
    ros__parameters:
      waypoints: {waypoints}
"""

        filename = f"../waypoints/{drone_name}.yaml"
        with open(filename, "w") as file:
            file.write(content)
