import pandas as pd
import numpy as np

Rental_Inventory = pd.read_csv('./rent_data/rentalInventory_Studio.csv')


#print(Rental_Inventory.head())


Rent_Keys = [i for i in Rental_Inventory.keys() if '2021' in i]
#print(Rent_Keys)


Rental_Inventory = Rental_Inventory.drop(
    labels = range(0,5),
    axis = 0
)

#print(Rental_Inventory.head())

town_labels = Rental_Inventory['areaName']

#print(town_labels)
#print(town_labels)


#print(Rental_Inventory[Rent_Keys[0]])


#data_strip = {town_labels[5] : Rental_Inventory[Rent_Keys[0]][5]}

num = 5
#data_strip = {town_labels[num] : np.array([int(Rental_Inventory[i][num]) for i in Rent_Keys])}

#print(data_strip)
#print(len(town_labels))

rentals = {}

for i in town_labels:
    rentals[i] = [int(Rental_Inventory[i][num]) for i in Rent_Keys]
    rentals[i] = np.array(rentals[i])
#print(rentals['Astoria'])
total = 0
'''
for keys in rentals:
    total += rentals[keys][0] 

print(total)
'''

#print(Rent_Keys[len(Rent_Keys)-1])
totals = []
for i in range(len(Rent_Keys)):
    total = 0
    for keys in rentals:
        total += rentals[keys][i]
    totals.append(total)

#print(total)
#print(totals)


'''
    key :   value
    month : how many vacant apartments

'''
nyc_totals = {}
for i in range(len(Rent_Keys)):
    nyc_totals[Rent_Keys[i]] = totals[i]

#print(nyc_totals)


