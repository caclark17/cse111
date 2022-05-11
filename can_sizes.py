# Compute and print the storage efficiency of 12 steel can sizes

import math

def main():
    # Get the radius and height of the can
    radius = float(input("Please enter the radius of the can: "))
    height = float(input("Please enter the height of the can: "))

    # Call the compute_volume function to compute the volume
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)

    # Compute the storage efficiency 
    storage_efficiency = volume / surface_area

    # Print the storage efficiency
    print(f"Storage Efficiency: {storage_efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area



main()