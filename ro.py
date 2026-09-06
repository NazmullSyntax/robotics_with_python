# pyright: reportMissingImports=false
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Obstacle Avoiding Robot")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 200, 0)

# Robot
robot_x = 100
robot_y = 300
robot_angle = 0
robot_speed = 2

# Obstacles
obstacles = [
    pygame.Rect(300, 150, 100, 200),
    pygame.Rect(550, 300, 150, 100),
    pygame.Rect(200, 450, 150, 50)
]

clock = pygame.time.Clock()
running = True


def distance_to_obstacle(x, y):
    """Check distance between robot and obstacles."""

    min_distance = 1000

    for obstacle in obstacles:
        closest_x = max(obstacle.left, min(x, obstacle.right))
        closest_y = max(obstacle.top, min(y, obstacle.bottom))

        distance = math.sqrt(
            (x - closest_x) ** 2 +
            (y - closest_y) ** 2
        )

        min_distance = min(min_distance, distance)

    return min_distance


while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Robot sensor
    sensor_distance = distance_to_obstacle(robot_x, robot_y)

    # Obstacle avoidance
    if sensor_distance < 70:
        robot_angle += 3

    else:
        robot_x += math.cos(math.radians(robot_angle)) * robot_speed
        robot_y += math.sin(math.radians(robot_angle)) * robot_speed

    # Keep robot inside screen
    robot_x = max(20, min(WIDTH - 20, robot_x))
    robot_y = max(20, min(HEIGHT - 20, robot_y))

    # Draw background
    screen.fill(WHITE)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Draw sensor line
    sensor_length = 70

    sensor_x = robot_x + math.cos(
        math.radians(robot_angle)
    ) * sensor_length

    sensor_y = robot_y + math.sin(
        math.radians(robot_angle)
    ) * sensor_length

    pygame.draw.line(
        screen,
        GREEN,
        (robot_x, robot_y),
        (sensor_x, sensor_y),
        3
    )

    # Draw robot
    pygame.draw.circle(
        screen,
        BLUE,
        (int(robot_x), int(robot_y)),
        20
    )

    # Robot direction
    direction_x = robot_x + math.cos(
        math.radians(robot_angle)
    ) * 25

    direction_y = robot_y + math.sin(
        math.radians(robot_angle)
    ) * 25

    pygame.draw.line(
        screen,
        BLACK,
        (robot_x, robot_y),
        (direction_x, direction_y),
        4
    )

    # Update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()