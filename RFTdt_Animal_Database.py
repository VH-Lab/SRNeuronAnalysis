import sqlite3
connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
# cursor = connection.execute("select * from RFTdt_Animals")
# for row in cursor:
#     print row
# cursor = connection.execute("select animals.animal_id,genotype, age, sex, condition, avg(branch_number) from RFTdt_Neurons left join RFTdt_Animals on neurons.animal_id = animals.animal_id where age = 'P16' group by genotype, condition, sex")
# # cursor = connection.execute("select * from Neurons left join Animals on neurons.animal_id = animals.animal_id where age='P16' group by animal_id, genotype, condition, sex")
# for row in cursor:
#     print row


connection.execute('drop table RFTdt_Animals')
connection.execute('''create table RFTdt_Animals(animal_id text primary key, dpi text, condition text, genotype text,
    sex text, number_of_cells text);''')

import os
os.chdir("C:\Users\Sarah\Desktop\AnimalInfo")
import csv

animal_id=[]
dpi=[]
condition=[]
genotype=[]
sex=[]
number_of_cells=[]

with open('RFTdt_AnimalInfo.csv','rb') as csvfile:
    animal_info = csv.reader(csvfile, delimiter= ',')
    for row in animal_info:
        animal_id.append(row[0])
        dpi.append(row[1])
        condition.append(row[2])
        genotype.append(row[3])
        sex.append(row[4])
        number_of_cells.append(row[5])

for index,animal in enumerate(animal_id):
    connection.execute("insert into RFTdt_Animals (animal_id, dpi, condition, genotype, sex, number_of_cells) values(?,?,?,?,?,?);",(animal_id[index], dpi[index], condition[index], genotype[index], sex[index], number_of_cells[index]))

connection.commit()