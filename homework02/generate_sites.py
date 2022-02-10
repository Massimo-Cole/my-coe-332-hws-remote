import json
import random

#generate 5 random latitudes and longitudes between 16-18 and 82-84 degrees respectivly
min_lat = 16.0
max_lat = 18.0
min_long = 82.0
max_long = 84.0
composition_list = ["stoney", "iron", "stoney-iron"]

data = {
    "sites": [
        {
            "site_id": 1,
            "latitude": random.uniform(min_lat, max_lat),
            "longitude": random.uniform(min_long, max_long),
            "composition": random.choice(composition_list)
        },
        {
            "site_id": 2,
            "latitude": random.uniform(min_lat, max_lat),
            "longitude": random.uniform(min_long, max_long),
            "composition": random.choice(composition_list)
        },
        {
            "site_id": 3,
            "latitude": random.uniform(min_lat, max_lat),
            "longitude": random.uniform(min_long, max_long),
            "composition": random.choice(composition_list)
        },
        {
            "site_id": 4,
            "latitude": random.uniform(min_lat, max_lat),
            "longitude": random.uniform(min_long, max_long),
            "composition": random.choice(composition_list)
        },
        {
            "site_id": 5,
            "latitude": random.uniform(min_lat, max_lat),
            "longitude": random.uniform(min_long, max_long),
            "composition": random.choice(composition_list)
        },
    ]
}

#save as a json file
with open('impact_sites.json', 'w') as out:
    json.dump(data, out, indent=2)
