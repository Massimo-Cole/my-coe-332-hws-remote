This directory contains homework 2 for coe332. This directory contains two scripts, generate_sites.py and calculate_trip.py.

generate_sites.py randomly generates latitude, longitude, and compositions for five meteorite landing sites on mars and stores the data of each site in a directory, and then makes a list of directories to store all 5 sites. It then writes that list of directories to a JSon file.

calculat_trip.py  reads in the meteorite site JSON file and calculates the time required for a rover to ke samples from the five sites in order.  

Run generate_sites.py using python3, then run calculate_trips.py using python3. calculate trips will then output on the command the time each trip between sites took to drive, and the time it took to sameple each site, and a summary of the total time the mission took. 