#!/usr/bin/env python3

#imports
import json
from typing import List
import math
import logging

#global varibles/constants

#class deffinitions

#function definitions

def turbidity_calc(a_list_of_dicts: List[dict], a0: str, I90: str) -> float:
    """
    This function calculates turbidity from nephelometer readings.
    
    Args:
        a0 (str): key reffering to a calibration constant from the detector
        I90 (str): a key reffering to 90 degree current, the output of the detector
   
    Returns:
        T (float): Turbidity in NTU Units (0-40)
    """
    T = 0 #intialize varible
    for sample in a_list_of_dicts[-6:-1]:
        T += (float(sample[a0]) * float(sample[I90]))

    return(T / 5)  #calculate averae T from the last 5 samples


def time_till_safe(Ts: float, T0: float, d: float):
    """
    This function calculates the minimum time it will take for the water 
    to reach safe turbidity levels

    Args:
        Ts (float): Turbidity threshold for safe water in NTU units (0-40)
        T0 (float): ccurrent torbidity level in NTU units (0-40)
        d (float): decay factor per hour (0-1)

    Returns:
        b (float): minimum hours until water reaches safe threshold. 
    """
    b = (math.log(Ts/T0))/(math.log(1-d))
    return b



def main():
    with open('turbidity_data.json', 'r') as f:
        t_data = json.load(f)

    T0 = turbidity_calc(t_data['turbidity_data'], 'calibration_constant', 'detector_current')
       
    b = time_till_safe(1.0, T0, 0.02)

    print('Average turbidity based on most recent five measurements = ', T0, ' NTU')
    
    if T0 > 1:
        logging.basicConfig()
        logging.warning('Turbidity is above treshold for safe use')
    else:
        b = 0

    print('Minimum time required to return below a safe treshold = ', b, ' hours')


if __name__ == '__main__':
    main() 
    
