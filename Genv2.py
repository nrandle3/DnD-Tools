import random as rn
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("./EncountersTransposed.csv")

def value_counts(arr):
    unique_elements, counts_elements = np.unique(arr, return_counts=True)
    return (np.asarray((unique_elements, counts_elements)))

def hostileEnc(danger):
    danger = min(danger,5)

    weights = {
               "Skill Check":danger,
               "Hostile Social":danger,
               "Combat (Non-committal)":danger,
               "Combat (Aggressive)":(danger-1)*2,
               
            }
    typesWeighted = []
    
    for i,encType in enumerate(weights.keys()):
            for j in range(weights[encType]):
                typesWeighted = np.append(typesWeighted,encType)
    return rn.choice(typesWeighted)

def genMund():
    weights = {"Inventory Check":5,
               "Weather Check":6,
               
            }
    
    typesWeighted = []
    
    for i,encType in enumerate(weights.keys()):
            for j in range(weights[encType]):
                typesWeighted = np.append(typesWeighted,encType)
    return rn.choice(typesWeighted)


test = []
for i in range(1000):    
    test.append(hostileEnc(2))
print(value_counts(test))








