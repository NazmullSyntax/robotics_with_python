# Simple Robot Obstacle Detection

distance = 25  # distance from obstacle in cm

print("🤖 Robot started...")
print("Obstacle distance:", distance, "cm")

if distance < 20:
    print("⚠️ Obstacle is very close!")
    print("↩️ Robot is turning left")

elif distance < 50:
    print("⚠️ Obstacle detected")
    print("🐢 Robot is slowing down")

else:
    print("✅ Path is clear")
    print("➡️ Robot is moving forward")