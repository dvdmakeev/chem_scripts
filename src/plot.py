import matplotlib.pyplot as plt

def plot_intersections(intersections: dict):
    times = sorted(intersections.keys())
    intersection_counts = [len(intersections[time]) for time in times]

    plt.figure(figsize=(15, 8))
    plt.plot(times, intersection_counts, marker='o', color='b', linestyle='-')
    plt.title("Molecule Intersections Over Time")
    plt.xlabel("Time")
    plt.ylabel("Number of Intersections")
    plt.grid(True)
    plt.show()