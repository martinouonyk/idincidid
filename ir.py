def calculate_centroid(points):
    x_sum = sum(point[0] for point in points)
    y_sum = sum(point[1] for point in points)
    num_points = len(points)

    centroid = (x_sum / num_points, y_sum / num_points)
    return centroid

# Example usage:
points = [(0, 0), (4, 0), (4, 3), (0, 3)]
centroid = calculate_centroid(points)
print(f"The centroid is at {centroid}")
