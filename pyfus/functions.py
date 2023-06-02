# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:28:52 2023

@author: Senzt
"""

import numpy as np
import matplotlib.pyplot as plt


def epochs_single(PD, start, stop):
    print("epoch test")
    
    # Assuming PD.bloodflow is your y-values
    y = PD.bloodflow
    
    # Generate x-values, from 0 to the length of y
    x = np.arange(len(y))
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y)
    ax.fill_between(x, y, where=(y > start) & (y < stop), color='gray', alpha=0.5)
    ax.axvline(x=start, color='r', linestyle='--')
    ax.axvline(x=stop, color='r', linestyle='--')

    plt.xlabel('Time point')
    plt.ylabel('Blood flow')
    plt.show()
    
    
def epochs(obj, start, stop):
    cbv_dict = obj.mean_dict
    subset_dict = {}

    for key, data in cbv_dict.items():
        mean_data = np.mean(data, axis=0)
        min_data = np.min(data, axis=0)
        max_data = np.max(data, axis=0)

        # Subset the data within start and stop
        subset_dict[key] = data[:, start:stop]

        time_points = np.arange(mean_data.shape[0])  # Changed this to numpy array
        plt.plot(time_points, mean_data, label=key)
        plt.fill_between(time_points, min_data, max_data, alpha=0.1)

    # Draw vertical lines and fill area before start and after stop
    plt.axvline(x=start, color='r', linestyle='--')
    plt.axvline(x=stop, color='r', linestyle='--')
    plt.fill_between(time_points, plt.ylim()[0], plt.ylim()[1], where=(time_points<start) | (time_points>=stop), color='grey', alpha=0.5)

    plt.xlabel('Time point')
    plt.ylabel('CBV %')  
    plt.xlim(time_points[0], time_points[-1])  # Set x-axis limits to match range of data
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  
    plt.show()  

    return subset_dict
    
    