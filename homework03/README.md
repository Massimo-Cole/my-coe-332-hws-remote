##  Martian Water Analysis

### Summary 
This program simulates a robot on mars taking samples of water and checking its turbididty. The rover needs the water 
to be below a certain turbidity in order to analyze rock samples it has collected.

### Installation 
This program requires dowloading a json data file which contains the turbidity data. Download the turbitity jason file 
by using the wget command on the following link.  

~~~
wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
~~~


### Code
This program contains 2 python scripts, water_analyzer and test_water_analyzer.

water_analyzer.py: A script that reads in the water quality data set, and prints to screen: (1) the current water 
turbidity (taken as the average of the most recent five data points), (2) whether that turbidity is below a safe 
threshold, and (3) the minimum time required for turbidity to fall below the safe threshold (if it is already below 
the safe threshold, the script would report 0 hours).

test_water_analyzer.py: A script containing 10 unit tests, five tests associated with each function in water_analyser, 
using pytest. (was not finished due to time constraints)

### How to Run
After downloading the file, run the water_analyzer.py script with python3

~~
python3 water_analyzer.py
~~
The program will then out put into the command line the current turbity level of the water, a warning if the current
turbity level exceeds the safe treshold, and a time estimation for when the water will settle to a safe turbidity
level.

~~
Average turbidity based on most recent five measurements = 1.1992 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 8.99 hours
~~
