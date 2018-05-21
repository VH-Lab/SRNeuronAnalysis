import os
import sqlite3
import AnnotationReaderXML

connection=sqlite3.connect('C:\Users\Sarah\PycharmProjects\SRNeuronAnalysis\Dendrite_Analysis.db')
# cursor = connection.execute("select * from Neurons")
# # for row in cursor:
# #     print row
# # cursor = connection.execute("select * from Neurons")
# # cursor = connection.execute("select avg(soma_radius) from Neurons")
# #
# #
# for row in cursor:
#      print row
#      print 'animal_id', row[0]
#      print 'neuron_id =', row[1]
#      print 'soma_size =', row[2]
#      print 'tree_number=', row[3]
#      print 'mean_branch_number=', row[5]


connection.execute('drop table RFTdt_Neurons')
#connection.execute('''create table Neurons(animal_id text, neuron_id text primary key,soma_radius real,tree_number int, mean_branch_length real, branch_lengths text, branch_number int, path_lengths text, mean_path_length real,tip_number int);''')
connection.execute('''create table RFTdt_Neurons(animal_id text, neuron_id text primary key,soma_radius real, tree_number int, mean_branch_length real, branch_lengths text,branch_number int, path_lengths text, mean_path_length real, tip_number int, arbor_length real, tortuosity text, mean_tortuosity real, volume int, density real, sholl text);''')

file_location = raw_input("Input data path.")
os.chdir(file_location)
annotation_files = AnnotationReaderXML.annotation_finder(file_location)

for annotation_file in annotation_files:

    nodes,edges = AnnotationReaderXML.annotation_parser(annotation_file)
    source_target_dict = AnnotationReaderXML.source_target(edges)

    animal_id = annotation_file[-30:-22]
    print animal_id

    neuron_id = annotation_file[-30:-16]
    print neuron_id
    soma_radius = AnnotationReaderXML.soma_size(nodes,edges)

    tree_num = AnnotationReaderXML.tree_number(nodes,edges)

    branch_num = AnnotationReaderXML.branch_number(nodes,edges)

    tip_num = AnnotationReaderXML.tip_number(nodes,edges)

    branch_lengths, mean_branch_length = AnnotationReaderXML.segment_length(source_target_dict, nodes, edges)
    branch_lengths = str(branch_lengths).strip('[]')

    arbor_length = AnnotationReaderXML.arbor_length(source_target_dict, nodes, edges)

    path_lengths, mean_path_length = AnnotationReaderXML.path_length(source_target_dict, nodes, edges)
    path_lengths = str(path_lengths).strip('[]')
    mean_path_length = mean_path_length

    tortuosity, mean_tortuosity = AnnotationReaderXML.tortuosity(source_target_dict, nodes, edges)
    tortuosity = str(tortuosity).strip('[]')

    volume = AnnotationReaderXML.volume(nodes, edges)

    density = AnnotationReaderXML.density(source_target_dict, nodes, edges)

    sholl = AnnotationReaderXML.sholl(source_target_dict, nodes, edges)
    sholl = str(sholl).strip('[]')

    #connection.execute("insert into Neurons (animal_id,neuron_id,soma_radius,tree_number,mean_branch_length,branch_lengths, branch_number, path_lengths,mean_path_length, tip_number) values(?,?,?,?,?,?,?,?,?,?);",(animal_id,neuron_id,soma_radius, tree_num,mean_branch_length,branch_lengths, branch_num, path_lengths, mean_path_length,tip_num))
    connection.execute("insert into RFTdt_Neurons (animal_id,neuron_id,soma_radius, tree_number, mean_branch_length, branch_lengths, branch_number, path_lengths, mean_path_length, tip_number, arbor_length, tortuosity, mean_tortuosity, volume, density, sholl) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(animal_id,neuron_id,soma_radius, tree_num, mean_branch_length, branch_lengths, branch_num, path_lengths, mean_path_length, tip_num, arbor_length, tortuosity, mean_tortuosity, volume, density, sholl))

connection.commit()