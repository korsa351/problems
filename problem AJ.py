import csv

prim_type = {}
with open("Crimes.csv") as crime:
    crimes = csv.reader(crime)
    id_prim_type = next(crimes).index("Primary Type")
    for crime_ in crimes:
        if crime_[5] in prim_type:
            prim_type[crime_[5]] += 1
        else:
            prim_type[crime_[5]] = 0
most_freq_prim_type = ["", 0]
for prim, total in prim_type.items():
    if total > most_freq_prim_type[1]:
        most_freq_prim_type[0], most_freq_prim_type[1] = prim, total
print(most_freq_prim_type)