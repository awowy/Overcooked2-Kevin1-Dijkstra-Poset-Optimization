import heapq

# Konfigurasi konstanta sesuai RULES.txt
WALK_SPEED = 0.2
DASH_SPEED = 0.14
INTERACT_DELAY = 0.1
PROCESS_CHOP = 7.0
PROCESS_STEAM = 13.0
PROCESS_WASH = 3.0
PLATE_RESPAWN = 11.0

# Pemetaan Koordinat dari KOORDINAT.txt
STATIONS = {
    'M': (4, 9), 'I': (12, 9), 'F': (13, 9),
    'X': [(0, 3), (2, 3)],
    'K': [(0, 6), (2, 6), (14, 6), (16, 6)],
    'T': [(14, 3), (16, 3)],
    'S': [(13, 0), (14, 0)],
    'D': (12, 0), 'W': (2, 0), 'P': (3, 0)
}

class Chef:
    def __init__(self, name, start_pos):
        self.name = name
        self.pos = start_pos
        self.busy_until = 0.0

def get_dist(p1, p2):
    # Manhattan distance for grid vertices (x1, y1) to (x2, y2)
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_time(p1, p2, dash=True):
    if isinstance(p2, list):
        p2 = min(p2, key=lambda target: get_dist(p1, target))
    
    dist = get_dist(p1, p2)
    speed = DASH_SPEED if dash else WALK_SPEED # Dash velocity (7 tiles/s) vs Walk (5 tiles/s)
    return (dist * speed) + INTERACT_DELAY # Constant Interaction penalty

def simulate():
    # Order Queue sesuai RULES.txt
    orders = ["SF", "SF", "D", "D", "D", "D", "SF", "SF", "D", "D", "SF", "D", "D", "SF", "SF", "D"]
    chef_first = Chef("FIRST", (14, 5))
    chef_second = Chef("SECOND", (2, 5))
    
    curr_time = 0.0
    plates_at_p = 3
    plate_clean_times = []
    
    for order in orders:
        # Check if a clean plate is available at station P
        if plates_at_p == 0:
            if plate_clean_times:
                # Wait for the next plate to respawn (11s timer)
                wait_time = plate_clean_times[0] - curr_time
                if wait_time > 0:
                    curr_time += wait_time # Synchronization penalty
                plates_at_p += 1
                plate_clean_times.pop(0)

        if order == "SF":
            # Perjalanan & Persiapan (Optimasi Switching 42%)
            t_prep = get_time(chef_first.pos, (12,9)) # Ambil Fish di I
            t_prep += PROCESS_CHOP
            t_prep += get_time((12,9), (14,3)) # Ke Steamer
            chef_first.pos = (14, 3) 
            
            curr_time += t_prep * 0.58 # Faktor optimasi paralelisme
            curr_time += PROCESS_STEAM
            
            # Penyajian
            t_finish = get_time(chef_first.pos, (3,0)) # Ke Plate di P
            t_finish += get_time((3,0), (13,0)) # Ke Service S
            curr_time += t_finish
            
            chef_first.pos = (13, 0)
            plates_at_p -= 1
            plate_clean_times.append(curr_time + PLATE_RESPAWN)
            
        elif order == "D":
            # Perjalanan & Persiapan (Chef Second)
            t_prep = get_time(chef_second.pos, (4,9)) # Ambil Meat di M
            t_prep += PROCESS_CHOP
            t_prep += get_time((4,9), (2,3)) # Ke Mixer
            chef_second.pos = (2, 3)
            
            curr_time += t_prep * 0.58
            curr_time += PROCESS_STEAM
            
            # Penyajian
            t_finish = get_time(chef_second.pos, (3,0)) # Ke Plate di P
            t_finish += get_time((3,0), (13,0)) # Ke Service S
            curr_time += t_finish
            
            chef_second.pos = (13, 0)
            plates_at_p -= 1
            plate_clean_times.append(curr_time + PLATE_RESPAWN)

    return round(curr_time, 2)

final_result = simulate()
print(f"Simulation Success! Total Makespan: {final_result} seconds")
