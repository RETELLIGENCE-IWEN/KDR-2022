
import setup_path
import airsim
import WP_Parser
import os
import sys

# Desired Speed in m/s
desired_speed  = 5

# WayPoints Data Path
docs = os.path.join(sys.path[0], "multirotor_example/WayPoints.txt")

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# TakeOff
print("Taking Off")
client.takeoffAsync().join()
print("Initializing")
way_points = []


# Create WayPoint Parser
WPP = WP_Parser.WP_Data(docs, None)

# If Found WayPoint Data
if WPP.IsFileOpen:
    print("GOGO")

    # LOOP
    con = 1
    while(1):

        # Ignore WaPoint #17
        if con == 17: con+=1

        # Get WayPoint Data index = con
        new = WPP.ReadData(con, "WP")

        # Proceed If Next WayPoint Exist
        if new:
            con += 1

            print(new.X)
            print(new.Y)
            print(new.Z)
            print(new.Xoff)
            print(new.Zoff)
            print(new.Yoff, "\n")

            way_points.append([int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1])
            client.moveToPositionAsync(int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1, 5).join()
            client.rotateToYawAsync(int(new.ZR)).join()

        else:
            break

    # Return To First WayPoint
    new = WPP.ReadData(1, "WP")
    way_points.append([int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1])
    client.moveToPositionAsync(int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1, 5).join()
   
else:
    print("Failed To open WayPoint File")
   
client.hoverAsync().join()
client.landAsync().join()