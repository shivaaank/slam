import matplotlib.pyplot as plt
import numpy as np

def plot_trajectory(landmarks, mu0, u, dt):

    # Initialize the state
    x, y, theta = mu0[0], mu0[1], mu0[2]
    trajectory = [(x, y)]  # Store the trajectory

    # Simulate the motion
    for v, w in u:
        if w != 0:
            # Update state using velocity model
            x += -v / w * np.sin(theta) + v / w * np.sin(theta + w * dt)
            y += v / w * np.cos(theta) - v / w * np.cos(theta + w * dt)
            theta += w * dt
        else:
            # Handle straight-line motion (w = 0)
            x += v * dt * np.cos(theta)
            y += v * dt * np.sin(theta)
        
        trajectory.append((x, y))

    # Extract x and y coordinates for plotting
    x_coords, y_coords = zip(*trajectory)

    # Plot the trajectory
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, marker='o', label='Robot Trajectory')
    plt.scatter(x_coords[0], y_coords[0], color='green', label='Start', zorder=5)
    plt.scatter(x_coords[-1], y_coords[-1], color='red', label='End', zorder=5)
    plt.scatter(landmarks[:,0], landmarks[:,1], color='purple')
    plt.title('Robot Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.axis('equal')
    plt.show()