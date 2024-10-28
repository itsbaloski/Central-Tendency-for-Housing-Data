# Import packages
import numpy as np
import pandas as pd
from scipy import stats

#housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = np.array(brooklyn_one_bed['rent'])

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

#mean calculations below 
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = np.array(brooklyn_one_bed['rent'])
brooklyn_mean = np.mean(brooklyn_price)

anhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = np.array(manhattan_one_bed['rent'])
manhattan_mean = np.mean(manhattan_price)

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = np.array(queens_one_bed['rent'])
queens_mean = np.mean(queens_price)

#median calculations below
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = np.array(brooklyn_one_bed['rent'])
brooklyn_median = np.median(brooklyn_price)

anhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = np.array(manhattan_one_bed['rent'])
manhattan_median = np.median(manhattan_price)

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = np.array(queens_one_bed['rent'])
queens_median = np.median(queens_price)

#mode calculations below

brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = np.array(brooklyn_one_bed['rent'])
brooklyn_mode = stats.mode(brooklyn_price)

anhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = np.array(manhattan_one_bed['rent'])
manhattan_mode = stats.mode(manhattan_price)

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = np.array(queens_one_bed['rent'])
queens_mode = stats.mode(queens_price)







# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")





