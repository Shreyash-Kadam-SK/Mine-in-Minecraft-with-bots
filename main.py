# Function to get coordinates from the user
def get_coordinates(point_name):
    x = int(input(f"Enter the x-coordinate for the {point_name} point: "))
    z = int(input(f"Enter the z-coordinate for the {point_name} point: "))
    return x, z

# Get starting and ending points
start_x, start_z = get_coordinates("starting")
end_x, end_z = get_coordinates("ending")
common_y = int(input("Enter the common y-coordinate for both points: "))

# Ensure the starting point is the bottom-left and the ending point is the top-right
min_x, max_x = min(start_x, end_x), max(start_x, end_x)
min_z, max_z = min(start_z, end_z), max(start_z, end_z)

# Store all coordinates inside the box in a list
coordinates_list = [(x, common_y, z) for x in range(min_x, max_x + 1) for z in range(min_z, max_z + 1)]

# Print the list of coordinates
print("Coordinates inside the box:")
print(coordinates_list)

# Get the number of bots
botnumber = int(input("Enter how many bots:"))

# Generate commands for bots
for i in range(0, len(coordinates_list), botnumber):
    # Print the first command for each bot
    for j in range(botnumber):
        if i + j < len(coordinates_list):
            x, y, z = coordinates_list[i + j]
            print(f'/player minebot{j} spawn at {x} {y} {z}')

    # Print the second command for each bot
    for j in range(botnumber):
        if i + j < len(coordinates_list):
            print(f'/player minebot{j} kill')













