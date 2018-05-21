from AnnotationReaderXML import *
file_location = raw_input("Input data path.")
os.chdir(file_location)
annotation_files = annotation_finder(file_location)

for annotation_file in annotation_files:
    nodes,edges = annotation_parser(annotation_file)

    # print edges
    #
    print 'node_location'
    node_locations =  node_location_finder(nodes, edges)
    # print node_locations

    print 'source_target'
    # print source_target(edges)
    source_target_dict=source_target(edges)
    print source_target_dict

    print 'path finder'
    print path_finder(source_target_dict, '1', '38')

    print 'soma size:'
    print soma_size(nodes,edges)

    print 'tree number:'
    print tree_number(nodes,edges)

    print 'branch number:'
    print branch_number(nodes,edges)

    print 'tip number:'
    print tip_number(nodes,edges)

    print 'path_length'
    print path_length(source_target_dict, nodes, edges)

    print 'tortuosity'
    print tortuosity(source_target_dict, nodes, edges)

    print 'segment length'
    print segment_length(source_target_dict, nodes, edges)

    print 'arbor length'
    print arbor_length(source_target_dict, nodes, edges)

    print 'volume'
    print volume(nodes,edges)

    print 'density'
    print density (source_target_dict, nodes, edges)

    print 'sholl'
    print sholl(source_target_dict, nodes, edges)
