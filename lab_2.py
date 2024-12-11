import random

# Function to display the room
def display(room):
    for row in room:
        print(row)

# Initial room state, all rooms are dirty (represented by 1)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

print("All the rooms are dirty:")
display(room)

# Assign random dirt (0 for clean, 1 for dirty) to each room
x = 0
while x < 4:
    y = 0
    while y < 4:
        room[x][y] = random.choice([0, 1])  # Randomly make room dirty or clean
        y += 1
    x += 1

print("Before cleaning, the room has the following random dirt conditions:")
display(room)

# Reinitialize variables for cleaning process
x = 0
cleaned_rooms = 0  # To count the number of cleaned rooms

# Start cleaning process
while x < 4:
    y = 0
    while y < 4:
        if room[x][y] == 1:  # If the room is dirty
            print("Vacuum in this location now,", x, y)
            room[x][y] = 0  # Clean the room
            print("Cleaned room at", x, y)
            cleaned_rooms += 1  # Increment the count of cleaned rooms
        y += 1
    x += 1

# Display the cleaned room state
print("After cleaning the room:")
display(room)

# Calculate performance (percentage of clean rooms)
total_rooms = 16  # 4x4 grid, so 16 rooms
performance = (cleaned_rooms / total_rooms) * 100
print(f"Performance (cleaned rooms): {cleaned_rooms}/{total_rooms}")
print(f"Percentage of rooms cleaned: {performance}%")
