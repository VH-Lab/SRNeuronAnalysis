from AnnotationReaderXML import *
file_location = raw_input("Input data path.")
os.chdir(file_location)
annotation_files = annotation_finder(file_location)

for annotation_file in annotation_files:
    nodes,edges = annotation_parser(annotation_file)

    print 'soma size:'
    print soma_size(nodes,edges)

    print 'tree number:'
    print tree_number(nodes,edges)

    print 'branch number:'
    print branch_number(edges)

    print 'tip number:'
    print tip_number(nodes,edges)
