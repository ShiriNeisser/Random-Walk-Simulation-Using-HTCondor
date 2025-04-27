import matplotlib.pyplot as plt
from collections import Counter
import os
def read_coordinates(file_path):
    """
    Reads coordinates from a given text file. Each line in the file should contain one coordinate.
    Coordinates are assumed to be numeric values, either integers or floats.
    
    Args:
    file_path (str): The path to the text file containing the coordinates.
    
    Returns:
    list: A list of coordinates read from the file.
    """
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each coordinate is a simple numeric value, either int or float
            # Modify the parsing logic here if the format is different (e.g., tuples)
            coord = line.strip()
            try:
                # Convert to integer or float if possible
                if '.' in coord:
                    coordinates.append(float(coord))
                else:
                    coordinates.append(int(coord))
            except ValueError:
                continue  # Skip lines that cannot be converted to a number
    return coordinates
def plot_histogram(coordinates):
    """
    Plots a histogram of the coordinates based on their frequency of appearance.
    
    Args:
    coordinates (list): A list of coordinates.
    """
    # Count frequency of each coordinate
    frequency = Counter(coordinates)  
    # Prepare data for histogram
    values = list(frequency.keys())
    counts = list(frequency.values())  
    # Create histogram
    plt.figure(figsize=(10, 5))
    plt.bar(values, counts, color='blue')
    plt.xlabel('Coordinate Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Coordinate Frequencies')
    plt.grid(True)
    plt.show()
def main():
    # The path to the file should be input by the user or set here.
    file_path = input("Please enter the path to the text file with coordinates: ")
    if not os.path.exists(file_path):
        print("File does not exist. Please check the path and try again.")
        return
    
    # Read coordinates from file
    coordinates = read_coordinates(file_path)
    
    # Plot histogram
    plot_histogram(coordinates)

main()
