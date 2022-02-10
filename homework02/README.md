This directory contains homework 2 for coe332. This directory contains two scripts, generate_sites.py and calculate_trip.py. Run generate_sites, then run calculate_trip.

generate_sites.py randomly generates latitude, longitude, and compositions for five meteorite landing sites on mars and stores the data of each site in a directory, and then makes a list of directories to store all 5 sites. It then writes that list of directories to a JSon file.

calculat_trip.py  reads in the meteorite site JSON file and calculates the time required to visit and take samples from the five sites in order.  