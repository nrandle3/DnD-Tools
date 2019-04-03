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

def genEnc(danger):
    danger = min(danger,5)
    
    
    types = df["Type"].unique()

    weights = { "Character Encounter":1+ (5-danger),
               "Friendly Social":1 + (5-danger),
               "Skill Check":danger,
               "Hostile Social":danger,
               "Combat (Non-committal)":danger,
               "Combat (Aggressive)":max(1,(danger-2))**2
            
            }
    typesWeighted = []
    
    for i,encType in enumerate(types):
        if encType in weights:
            for j in range(weights[encType]):
                
                typesWeighted = np.append(typesWeighted,encType)
    return rn.choice(typesWeighted)


