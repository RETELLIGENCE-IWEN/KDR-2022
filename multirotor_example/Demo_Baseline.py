
import setup_path
import airsim
import WP_Parser

import os
import sys




# m/s
desired_speed  = 5












docs = os.path.join(sys.path[0], "multirotor_example/WayPoints.txt")


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# wind = airsim.Vector3r(-1,0,0)
# client.simSetWind(wind)

print("Taking Off")
client.takeoffAsync().join()
print("Initializing")
# client.moveToPositionAsync(22, -10, -25, 5).join()


way_points = []









# client.moveByVelocityAsync(0, 0, 5, 10).join()


# """
WPP = WP_Parser.WP_Data(docs, None)
if WPP.IsFileOpen:
    print("GOGO")

    con = 1
    while(1):
        if con == 17: con+=1
        new = WPP.ReadData(con, "WP")
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
            # client.rotateToYawAsync().join
            client.rotateToYawAsync(int(new.ZR)).join()


        else:
            break

    new = WPP.ReadData(1, "WP")
    way_points.append([int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1])

    client.moveToPositionAsync(int(new.Xoff), int(new.Yoff), int(new.Zoff)*-1, 5).join()
   
else:
    print("Failed To open WayPoint File")
   
   
   
   
   
    # client.hoverAsync().join()
    
    # client.landAsync().join()

    # """


client.hoverAsync().join()

client.landAsync().join()



# client.armDisarm(False)
# client.enableApiControl(False)


# airsim.wait_key('Press any key to takeoff')

# client.takeoffAsync().join()
# client.moveToPositionAsync(22, -10, -25, 5).join()

# state = client.getMultirotorState()
# print("state: %s" % pprint.pformat(state))
