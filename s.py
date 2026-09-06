# # # distance = 15

# # # if distance < 20:
# # #     print("Obstacle detected!")
# # #     print("Robot: Turn Left")
# # # else:
# # #     print("Path is clear")
# # #     print("Robot: Move Forward")

# # distance = 50

# # if distance > 30:
# #     print("Robot is moving forward")
# # else:
# #     print("Robot stopped")

# front = 10
# left = 50
# right = 30

# if front < 20:
#     if left > right:
#         print("Turn Left")
#     else:
#         print("Turn Right")
# else:
#     print("Move Forward")

light = "red"

if light == "red":
    print("Robot: STOP")

elif light == "yellow":
    print("Robot: Slow Down")

elif light == "green":
    print("Robot: GO")