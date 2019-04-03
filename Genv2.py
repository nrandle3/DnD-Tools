import random as rn
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def value_counts(arr):
    unique_elements, counts_elements = np.unique(arr, return_counts=True)
    return (np.asarray((unique_elements, counts_elements)))

def weightedChoice(d):
    typesWeighted = []
    
    for i,encType in enumerate(d.keys()):
            for j in range(d[encType]):
                typesWeighted = np.append(typesWeighted,encType)
    return rn.choice(typesWeighted)


test = []
df = pd.read_csv("./EncountersTransposed.csv")

        
while True:
    print("\n*__________________________________________________________________________________________________________*")
    
    danger = min(int(input("Threat Level: ")),5)
    
    hostile = {"Skill Check":danger,
                   "Hostile Social":danger,
                   "Combat (Non-committal)":danger,
                   "Combat (Aggressive)":(danger-1)*2
                }
    
    mund = {"Inventory Check":3,
                   "Find something mundane in inventory":1,
                   "Weather Check":5
                }
    
    flavor = {"Character Encounter":1,
                   "Discovery":1
                }
    
    
    
    phases = ["Dawn", 'Morning', 'Noon', 'Afternoon', 'Dusk', 'Night']
    
        
    for i in phases:
        print("\n------------------------------------------------\n\n" + 
              "*" + i + "*: ")
        random = [hostile]*(danger+1) + [mund]*abs(danger-8) + [flavor]*abs(danger-6)
        choice = weightedChoice(rn.choice(random))
        print(choice)
        if choice in df.columns:    
            print(df[choice].sample())





