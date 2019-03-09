import sys

def animate(speed, init):
    future_positions = {}
    size = len(init)
    max_time = 0
    for index in range(0, len(init)):
        particle = init[index]
        if particle == '.':
            continue
        future_pos = index
        time = 0
        while future_pos < size and future_pos >= 0:
            if time > max_time:
                max_time = time
            if time == 0:            
                distance = 0
            else:
                distance = speed
            if particle == 'R':
                future_pos = future_pos + distance
                if future_pos >= size:
                    # create empty chamber
                    if time not in future_positions:
                        positions = []
                        empty_range = range(0, size)
                        for tmp in empty_range:
                            positions.append('.')
                        future_positions[time] = positions
                    break
            elif particle == 'L':
                future_pos = future_pos - distance
                if future_pos < 0:
                    # create empty chamber
                    if time not in future_positions:
                        positions = []
                        empty_range = range(0, size)
                        for tmp in empty_range:
                            positions.append('.')
                        future_positions[time] = positions
                    break
            # build string with necessary size
            if time not in future_positions:
                positions = []
                empty_range = range(0, future_pos)
                for tmp in empty_range:
                    positions.append('.')
                positions.append('X')
                empty_range = range(future_pos + 1, size)
                for tmp in empty_range:
                    positions.append('.')
                future_positions[time] = positions                
            # string already built, just set X at current position
            else:
                position_list = future_positions[time]
                position_list[future_pos] = 'X'
            time = time + 1
    
    for time_unit in range(0, max_time + 1):
        if max_time == 0:
            print(init)
        else:
            position_list = future_positions[time_unit]
            position_str = ''.join(position_list)
            print(position_str)

def run():
    speed = int(sys.argv[1])
    init = sys.argv[2]
    animate(speed, init)

run()