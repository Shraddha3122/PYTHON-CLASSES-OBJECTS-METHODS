# Implement a class Robot with methods to move in a 2D grid. 
#Include functionality to reset position and display the current location.

class Robot:
    def __init__(self, x=0, y=0):
        """Initialize the robot's position at (x, y)."""
        self.x = x
        self.y = y

    def move_up(self):
        """Move the robot up by one unit."""
        self.y += 1

    def move_down(self):
        """Move the robot down by one unit."""
        self.y -= 1

    def move_left(self):
        """Move the robot left by one unit."""
        self.x -= 1

    def move_right(self):
        """Move the robot right by one unit."""
        self.x += 1

    def reset_position(self):
        """Reset the robot's position to the origin (0, 0)."""
        self.x = 0
        self.y = 0

    def display_position(self):
        """Display the current position of the robot."""
        return f"Current position: ({self.x}, {self.y})"

# Example usage:
if __name__ == "__main__":
    robot = Robot()
    print(robot.display_position())  # Output: Current position: (0, 0)

    robot.move_up()
    robot.move_right()
    print(robot.display_position())  # Output: Current position: (1, 1)

    robot.move_down()
    robot.move_left()
    print(robot.display_position())  # Output: Current position: (0, 0)

    robot.reset_position()
    print(robot.display_position())  # Output: Current position: (0, 0)