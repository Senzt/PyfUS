# -*- coding: utf-8 -*-
"""
Created on Wed May 31 22:28:52 2023

@author: Senzt
"""

def epochs(PD, start, stop):
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