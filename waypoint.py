# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()

client.moveToPositionAsync(0, 22, -1, 5).join()
client.moveToPositionAsync(25, 24, -1, 5).join()
client.moveToPositionAsync(0, 24, -1, 5).join()
client.moveToPositionAsync(-20, 24, -1, 5).join()
