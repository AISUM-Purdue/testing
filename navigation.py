######## Fly in front door, explore, and out the back door - using MoveToPosition waypoints  ##############

import airsim
import pprint


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()
#state = client.getMultirotorState()
#print("state: %s" % pprint.pformat(state))


points = [[0, 30, -1],#middle
         [4, 31, -1],#outside room1 on the left
         [5.5, 27, -1],#enter room1 on left
	 [5, 31, -1],#exit room1 on left
	 [6, 29.8, -1],#outside room1 on right
	 [7, 34, -1],#enter room1 on right
	 [5.5, 31, -1],#exit room1 on right
	 [12,31,-1], #outside room2 on the left
	 [12.6,28, -1],#enter room2 on left
	 [18.5, 28 ,-1],#room2 mid
	 [18.5,31,-1], #exit room2 on left
	 [16, 31, -1],#outside room2 on the right
	 [15.2, 33,-1],#enter room2 on the right
	 [15.2, 31, -1],#exit room2 on the right
	 [18.5, 31, -1],#outside room3 on the right
	 [18.9, 33, -1],#enter room3 on the right
	 [20, 31, -1],#exit room3 on the right
	 [22.2,31,-1], #outside room4 on the left
	 [22, 27, -1], #enter room4 on the left
	 [22.5, 30, -1], #exit room4 on the left	
	 [24, 30.5, -1],
	 #[24, 31.1, -1],
	 [27,34.5,-1],
	 [26.5, 31, -1],	
         [0, 30.5, -1], #middle
	 [-3.5, 31, -1],#outside room1 on the right
	 [-3.5, 28, -1],#enter room1 on the right
	 [-4.9, 31, -1],#exit room1 on the right
	 [-9.5, 31, -1],#outside room1 on the left
	 [-9.5, 34, -1],#enter room1 on the left
	 [-10.5, 31, -1],#exit room1 on the left
	 [-12, 31, -1], #outside room2 on the right
	 [-12, 28, -1],#enter room2 on the right
	 [-12.1, 30, -1],#outside room2 on the right
	 [-12.9, 31 ,-1],#outside room2 on the left
	 [-12.9, 33, -1],#enter room2 on the left
	 [-12.65, 31, -1],#exit room2 on the left
	 [-14.5, 31, -1],#outside room3 on the left
	 [-14.5, 34, -1],#enter room3 on the left
	 [-17, 34, -1], #move inside room3 on the left
	 [-17, 31, -1], #exit room3 on the left
	 [-18, 31, -1], #outside room3 on the right
	 [-18, 27, -1], #enter room3 on the right
	 [-17, 31, -1], #outside room3 on the right
	 [-19.5, 31, -1],#outside room4 on the left
	 [-19.5, 34, -1],#enter room4 on the left
	 [-20, 31.5, -1],#exit room4 on the left
	 [-19.4, 31, -1], #outside room4 on the right
	 [-19.4, 28, -1],#enter room4 on the right
	 [-19.7, 30.5, -1],#exit room4 on the right
         [-22.7, 30.7, -1],
         [0, 30.5, -1],
         [-.35, 30, -1], #exiting the building
         [-.35, 37, -1],
         [-2, 37, -1],
         [-2.5, 39, -1],
         [-3, 45, -1],
         [2, 45, -1],
         [2.75, 46, -1],
         [3.5, 46, -1],
         [3.75, 48, -1],
         [4, 53, -1],
         [4, 56, -1],
         [4, 60, -1]]

x = 0 #index to keep track of when to send notional messeages to the log

for point in points:
    client.moveToPositionAsync(point[0], point[1], point[2],2).join()

    if x == 1:
        print("file cabinet")
        #client.writeLogMessage("Saw file cabinet")
    elif x == 2:
        print("Sofa")
        #client.writeLogMessage("Saw sofa")
    elif x == 4:
        print("bed")
        #client.writeLogMessage("Saw bed")

    x+=1

print("successful exit")
#client.writeLogMessage("Successful exit")

client.reset()
client.armDisarm(False)