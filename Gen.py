# Change this list to add your own characters 
# (It chooses from this list entirely randomly for the "Character Encounters")

playerCharacters = ["Welkin","Franklin","Shifo","Ivon","Shaerif"]

"""
In order to add your possible events:
    First add them to the CSV, with the type and encounter
        Keep in mind the speelling is case sensitive
    If you use a heading 


"""



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

try:
         
    while True:
        print("\n*________________________________________________________________________________________*")
        
        danger = max(min(int(input("Threat Level: ")),5),1)
        
        # Here are the types of events that can be choosen. 
        
        # The idea for hostile events is that at higher threat levels, 
        # the more likely an aggressive event will occur
        # the others are just static because they dont matter as much
        
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
                  "*" + i + "*: ")          # here is where
            random = [hostile]*(danger+1) \
                    + [mund]*abs(danger-8) \
                    + [flavor]*abs(danger-6)
                    
            choice = weightedChoice(rn.choice(random))
            print(choice,end = "")
            if choice == "Character Encounter":
                print(": " + rn.choice(playerCharacters))
            else:
                print()
            if choice in df["Type"].unique(): 
                print(df[df["Type"]==choice].sample()["Encounter"].values[0])
except:
    print("ok")    
    
    
    
