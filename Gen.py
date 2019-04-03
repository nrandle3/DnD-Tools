import random as rn
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv("file:///D:/Personal/Media/Documents/python/Encounter generator/Encounters.csv")


phases = ["Dawn", 'Morning', 'Noon', 'Afternoon', 'Dusk', 'Night']

encTypes = ["Character Encounter",
           "Friendly Social",
           "Skill Check",
           "Hostile Social",
           "Combat (Non-committal)",
           "Combat (Aggressive)"
        ]
non_encounter = ["Talk about the weather",
                 "Character encounter: ",
                 "Check over your inventories"
                 ]


chars = ["Welkin","Franklin","Shifo","Ivon","Shaerif"]
try:
        #ok yea I want to rewrite all this shit so I can easily add columns and it'll b ez
    while True:
        print("\n*__________________________________________________________________________________________________________*")
        
        danger = min(int(input("Threat Level: ")),5)
        for i in range(6): 
            enc = rn.randint(1,6)
            print("\n------------------------------------------------\n\n" + 
                  "*" + phases[i] + "*: ")
            
            if enc <= int(danger):
                encType = rn.randint(0,5)
                print(encTypes[encType],end="")
                if encType < 4:
                    if encType == 0:
                        print(": " + rn.choice(chars),end="")
                    encounter = df[encTypes[encType]].dropna().sample().values[0]
                    print("\n" + encounter)
                else:
                    print()
            else:
                non_encounter[1] =  "Character Encounter(easy): " + rn.choice(chars) + "\n" + df["Character Encounter"].dropna().sample().values[0]
                nonE = rn.choice(non_encounter) 
                print("(NONE)" + nonE)
except:
    print("ok")    
                