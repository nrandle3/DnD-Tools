import random as rn
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("./EncountersTransposed.csv")
def genEnc(danger):
        
    danger = 4
    
    types = df["Type"].unique()
    
    weights = { "Character Encounter":1,
               "Friendly Social":1*int(danger/2),
               "Skill Check":1*danger,
               "Hostile Social":1*danger,
               "Combat (Non-committal)":1*(danger),
               "Combat (Aggressive)":1*(danger-1)
            
            }
    
    for i,encType in enumerate(types):
        if encType in weights:
            for j in range(weights[encType]):
                types = np.append(types,encType)
            
    return rn.choice(types)

print(genEnc(1))