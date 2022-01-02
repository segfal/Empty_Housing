
import pandas as pd
import numpy as np
Asking_Rent = pd.read_csv('./rent_data/medianAskingRent_Studio.csv')


#print(Asking_Rent.head())

Rent_Keys = [i for i in Asking_Rent if '2021' in i]


Asking_Rent = Asking_Rent.drop(
    labels = range(0,5),
    axis = 0
)

town_labels = Asking_Rent['areaName']

rentals = {}
num = 5

for i in town_labels:
    rentals[i] = [int(Asking_Rent[i][num]) for i in Rent_Keys]
    rentals[i] = np.array(rentals[i])

totals = []
for i in range(len(Rent_Keys)):
    total = 0
    for keys in rentals:
        total += rentals[keys][i]
    totals.append(round(total/len(rentals),2))

#print(totals)

nyc_avg_price = {}
for i in range(len(Rent_Keys)):
    nyc_avg_price[Rent_Keys[i]] = totals[i]
