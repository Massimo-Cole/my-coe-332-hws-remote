import json
import math

def compute_time(a_list_of_dicts, key_string_1, key_string_2, key_string_3):
    #driving time
    lat0 = math.radians(16.0)
    long0 = math.radians(82.0)
    count = 1
    total_time = 0

    for site in a_list_of_dicts:
        lat1 = math.radians(float(site[key_string_1]))
        long1 = math.radians(float(site[key_string_2]))
        central_angle = math.acos( (math.sin(lat0) * math.sin(lat1)) + (math.cos(lat0) * math.cos(lat1) * math.cos(abs(long1-long0))))
        distance = 3389.5 * central_angle #distance in kilometers on surface of mars
        drive_time = distance/10 # time in hours, speed 10 km/hr
        
        #sample time
        if (site[key_string_3] == "stoney"):
            sample_time = 1
        if (site[key_string_3] == "iron"):
            sample_time =2
        if (site[key_string_3] == "stoney-iron"):
            sample_time = 3

        #print output
        print("leg ", count, ", travel time =", drive_time, "hr, sample time = ", sample_time, "hr")

        lat0 = lat1
        long0 = long1
        total_time += (drive_time + sample_time)
        count +=1
    print("summary, total time = ", total_time, "hr")
    return

#def compute_sample_time():


def main():

    with open('impact_sites.json', 'r') as f:
        is_data = json.load(f)
        
    compute_time(is_data['sites'], 'latitude', 'longitude', 'composition')

if __name__ == '__main__':
    main()
