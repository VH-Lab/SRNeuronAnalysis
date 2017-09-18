import sqlite3
from AnnotationReaderXML import *
connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
cursor = connection.execute("select count(*) from Neurons")
for row in cursor:
    print row
cursor = connection.execute("select * from Neurons")
# cursor = connection.execute("select avg(soma_size) from Neurons")


for row in cursor:
     print row
     print 'animal_id', row[0]
     print 'neuron_id =', row[1]
     print 'soma_size =', row[2]
     print 'tree_number=', row[3]
     print 'branch_number=', row[5]

# connection.execute('drop table Neurons')
# connection.execute('''create table Neurons(animal_id text, neuron_id text primary key,soma_size real, tree_number int, branch_length real,
#     branch_number int, path_length real, tip_number int, arbor_length real, tortuosity real, sholl int, branch_order int,
#     polarity real);''')
#
# file_location = raw_input("Input data path.")
# os.chdir(file_location)
# annotation_files = annotation_finder(file_location)
#
# for annotation_file in annotation_files:
#
#     nodes,edges = annotation_parser(annotation_file)
#
#     animal_id = annotation_file[-29:-23]
#
#     neuron_id = annotation_file[-29:-16]
#
#     soma_diameter = soma_size(nodes,edges)
#
#     tree_num = tree_number(nodes,edges)
#
#     branch_num = branch_number(edges)
#
#     tip_num = tip_number(nodes,edges)
#
#     connection.execute("insert into Neurons (animal_id,neuron_id,soma_size, tree_number, branch_number,tip_number) values(?,?,?,?,?,?);",(animal_id,neuron_id, soma_diameter,tree_num,branch_num,tip_num))
#
# connection.commit()