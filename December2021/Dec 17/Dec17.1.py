

target_x = range(128,161)
target_y = range(-142, -87)

x_speed_range = range(0,200)
y_speed_range = range(0,200)

max_height = 0

for i in x_speed_range:
    for j in y_speed_range:
        # Reset for each run
        y_height = 0
        probe_pos_x = 0
        probe_pos_y = 0
        x_speed = x_speed_range[i]
        y_speed = y_speed_range[j]
        while probe_pos_y > target_y[0]:

            # Adjust position
            probe_pos_x += x_speed
            probe_pos_y += y_speed

            # Check if hit a new height on this step
            if probe_pos_y > y_height:
                y_height = probe_pos_y

            # Change speed
            if x_speed > 0:
                x_speed -= 1
            elif x_speed < 0:
                x_speed += 1
            y_speed -= 1
        
            if (probe_pos_x in target_x) and (probe_pos_y in target_y):
                if y_height > max_height:
                    max_height = y_height
                    print(max_height, x_speed_range[i], y_speed_range[j])
                break
print(max_height)
# 10011, x_speed = 16, y_speed = 141