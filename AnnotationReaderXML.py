import os
import xml.etree.ElementTree as ET
import glob
from scipy.spatial import distance
from scipy.spatial import ConvexHull
import numpy as np


def annotation_finder(directory):
    os.chdir(directory)
    annotationfiles=glob.glob(directory + "\*.xml")
    print annotationfiles
    return annotationfiles

def annotation_parser (annotationfile):
    tree = ET.parse(annotationfile)
    root = tree.getroot()
    nodes = list(root.iter('node'))
    edges = list(root.iter('edge'))
    return nodes, edges

def node_location_finder(nodes,edges):
    node_location = [[node.attrib['id'], node.attrib['x'], node.attrib['y'], node.attrib['z']]for node in nodes]
    return node_location

def source_target(edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    source_target_dict = dict()


    for pair in combined_node_pairs:
        if pair[0] in source_target_dict:
            # append the new number to the existing array at this slot
            source_target_dict[pair[0]].append(pair[1])
        else:
            # create a new array in this slot
            source_target_dict[pair[0]] = [pair[1]]
    return source_target_dict

    # return source_target_dict.update(target_source_dict)

def path_finder(source_target_dict, start, end, path=[]):
    path = path + [start]
    # print path
    if start == end:
        return path
    if not source_target_dict.has_key(start):
        return None
    for node in source_target_dict[start]:
        if node not in path:
            newpath = path_finder(source_target_dict, node, end, path)
            if newpath: return newpath
    return None


#soma_size is biggest node
def soma_size(nodes,edges):
    radii_list=[node.attrib['radius'] for node in nodes]
    soma_diameter = max(radii_list)
    return soma_diameter


#tree_number is number of edges originating from the sources with the most edges (usually source '1')
def tree_number(nodes,edges):
    source_list = [edge.attrib['source'] for edge in edges]
    source_set = set(source_list)
    unique_sources=list(source_set)
    tree_count= max([source_list.count(source) for source in unique_sources])
    return tree_count

#branch_number is the count of duplicate sources
#NOTE: works regardless of directionality of path and how branch point is defined
def branch_number(nodes,edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    # print len(source_target_pairs)
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    # print len(target_source_pairs)
    combined_node_pairs = source_target_pairs + target_source_pairs
    # print combined_node_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    # print target_nodes
    source_nodes = [pair[1] for pair in combined_node_pairs]
    # print source_nodes
    combined_source_targets_flat = target_nodes + source_nodes
    # print combined_source_targets_flat
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)


    branch_node_count = [combined_source_targets_flat.count(node) if combined_source_targets_flat.count(node) > 5 else 0 for node in unique_nodes]
    branchpoint_number = sum([1 if node > 0 else 0 for node in branch_node_count])-1
    # print branchpoint_number
    # print branch_node_count
    connection_number_int = int(sum(branch_node_count))
    # print connection_number
    # print connection_number_int
    soma_connection_number = int(max(branch_node_count))
    # print soma_connection_number
    connections_soma_removed = connection_number_int-soma_connection_number
    # print connections_soma_removed
    tree_number = np.divide(soma_connection_number,2)
    # print tree_number
    non_soma_branches = np.divide(connections_soma_removed,2)-branchpoint_number
    branch_number = non_soma_branches + tree_number
    # print non_soma_branches

    return branch_number

#tip_number is the count of nodes/sources that have no targets
def tip_number(nodes,edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)
    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]

    return len(tip_list)

#path_length returns all the length of all paths for a neuron (path_lengths) and the average path length for a neuron (avg_path_length)
def path_length(source_target_dict, nodes, edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    # print combined_node_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    # print combined_source_targets_flat
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)

    node_id_list = [node.attrib['id'] for node in nodes]
    # node_id_set= set(node_id_list)
    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
    # print tip_list
    radii_list = [node.attrib['radius'] for node in nodes]
    soma_node = node_id_list[radii_list.index(max(radii_list))]
    path_list = [path_finder(source_target_dict, soma_node, tip) for tip in tip_list]
    # print 'path list'
    # print path_list
    node_location = node_location_finder(nodes, edges)
    # print 'node location'
    # print node_location

    # print "matches"
    path_lengths = []
    # print len(path_list)
    for path in range(0,len(path_list)):
        matches = [item for item in node_location if item[0] in path_list[path]]
        # print matches
        matches_nodes = [match[0] for match in matches]
        matches_index = [path_list[path].index(node) for node in matches_nodes]
        # print matches_index
        sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
        int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
        print sorted_matches
        # print int_matches

        interpoint_distance = 0
        for match in range(0,len(int_matches) - 1):
            interpoint_distance = interpoint_distance + distance.euclidean(int_matches[match][1:4], int_matches[match + 1][1:4])

        path_lengths.append(interpoint_distance)

    return path_lengths, np.mean(path_lengths)

#tortuosity is the ratio of the path_lengths to the euclidean distance between soma and path tip
def tortuosity(source_target_dict, nodes, edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)


    node_id_list= [node.attrib['id'] for node in nodes]
    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
    # print tip_list
    radii_list = [node.attrib['radius'] for node in nodes]
    soma_node = node_id_list[radii_list.index(max(radii_list))]
    path_list = [path_finder(source_target_dict, soma_node, tip) for tip in tip_list]
    node_location = node_location_finder(nodes, edges)

    path_lengths = []
    soma_to_tip = []
    for path in range(0,len(path_list)):
        matches = [item for item in node_location if item[0] in path_list[path]]
        # print matches
        matches_nodes = [match[0] for match in matches]
        matches_index = [path_list[path].index(node) for node in matches_nodes]
        # print matches_index
        sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
        int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
        # print int_matches

        interpoint_distance = 0
        for match in range(0,len(int_matches) - 1):
            interpoint_distance = interpoint_distance + distance.euclidean(int_matches[match][1:4], int_matches[match + 1][1:4])

        euc_distance = distance.euclidean(int_matches[0][1:4], int_matches[-1][1:4])
        #There is no (known) good reason that you have to use 1:4. by any indication it should be 1:3 but it IS NOT. DO NOT CHANGE IT
        # print int_matches[0][1:4]
        # print int_matches[-1][1:4]

        path_lengths.append(interpoint_distance)
        soma_to_tip.append(euc_distance)
        # print path_lengths
        # print soma_to_tip
    # print int_reordered_matches
    return np.divide(path_lengths, soma_to_tip), np.mean(np.divide(path_lengths, soma_to_tip))

#segment_length is the length of all segments (otherwise known as branches) returns all segment lengths and avg. segment length
def segment_length (source_target_dict, nodes, edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)

    branch_node_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) > 5]
    # print branch_node_list
    # print 'len(branch_node_list)'
    # print len(branch_node_list)


    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
    # print tip_list

    branch_node_tips = branch_node_list + tip_list

    segment_list = [path_finder(source_target_dict, node2, node)for node2 in branch_node_tips for node in branch_node_tips]
    segment_list = [segment for segment in segment_list if segment is not None]
    segment_list = [segment for segment in segment_list if len(segment) >1 ]
    # print segment_list
    # print len(segment_list)

    unique_segment_list1 = []
    for segment in segment_list:
        # print segment
        branch_node_tip_found = 0
        for node in branch_node_tips:
            if node in segment[1:-1]:
                branch_node_tip_found=1
        if branch_node_tip_found ==0:
            unique_segment_list1.append(segment)

    #
   # print unique_segment_list1
    unique_segment_list = set(frozenset(item) for item in unique_segment_list1)
    unique_segment_list = [list(item) for item in unique_segment_list]
    # print len(unique_segment_list)

    real_segments = []
    for match in unique_segment_list:
        segment_found = 0
        for segment in unique_segment_list1:
            if segment_found == 0:
                segment_set = set(segment)
                match_set = set(match)
                if segment_set == match_set:
                    real_segments.append(segment)
                    segment_found = 1
    unique_segment_list = real_segments

    node_location = node_location_finder(nodes, edges)
    segment_lengths = []
    for segment in range(0, len(unique_segment_list)):
        matches = [item for item in node_location if item[0] in unique_segment_list[segment]]
        # print matches
        if matches == []:
            segment_lengths.append(0)
        else:
            matches_nodes = [match[0] for match in matches]
            matches_index = [unique_segment_list[segment].index(node) for node in matches_nodes]
            sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
            int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
            # print sorted_matches


            interpoint_distance = 0
            for match in range(0, len(int_matches) - 1):
                interpoint_distance = interpoint_distance + distance.euclidean(int_matches[match][1:4], int_matches[match + 1][1:4])
            # print int_matches[match][1:4]
            segment_lengths.append(interpoint_distance)

    segment_lengths=set(segment_lengths)
    # print segment_lengths
    # print len(segment_lengths)
    segment_lengths=list(segment_lengths)


    return segment_lengths, np.mean(segment_lengths)


#arbor_length is the length of all segments added together
def arbor_length (source_target_dict, nodes, edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)

    branch_node_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) > 5]
    # print branch_node_list


    # node_id_list= [node.attrib['id'] for node in nodes]
    # node_id_set= set(node_id_list)
    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
    # print tip_list

    branch_node_tips = branch_node_list + tip_list

    segment_list = [path_finder(source_target_dict, node2, node) for node2 in branch_node_tips for node in
                    branch_node_tips]
    segment_list = [segment for segment in segment_list if segment is not None]
    segment_list = [segment for segment in segment_list if len(segment) > 1]
    # print segment_list
    # print len(segment_list)

    unique_segment_list1 = []
    for segment in segment_list:
        # print segment
        branch_node_tip_found = 0
        for node in branch_node_tips:
            if node in segment[1:-1]:
                branch_node_tip_found = 1
        if branch_node_tip_found == 0:
            unique_segment_list1.append(segment)
    # print unique_segment_list
    #
    unique_segment_list = set(frozenset(item) for item in unique_segment_list1)
    unique_segment_list = [list(item) for item in unique_segment_list]

    real_segments = []
    for match in unique_segment_list:
        segment_found = 0
        for segment in unique_segment_list1:
            if segment_found == 0:
                segment_set = set(segment)
                match_set = set(match)
                if segment_set == match_set:
                    real_segments.append(segment)
                    segment_found = 1
    unique_segment_list = real_segments


    node_location = node_location_finder(nodes, edges)
    segment_lengths = []
    for segment in range(0, len(unique_segment_list)):
        matches = [item for item in node_location if item[0] in unique_segment_list[segment]]
        if matches == []:
            segment_lengths.append(0)
        else:
            matches_nodes = [match[0] for match in matches]
            matches_index = [unique_segment_list[segment].index(node) for node in matches_nodes]
            # print matches_index
            sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
            int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
            # print int_matches
            # pri print int_matches


            interpoint_distance = 0
            for match in range(0, len(int_matches) - 1):
                interpoint_distance = interpoint_distance + distance.euclidean(int_matches[match][1:4], int_matches[match + 1][1:4])
                # print int_matches[match][1:4]

            segment_lengths.append(interpoint_distance)

    segment_lengths = set(segment_lengths)
    segment_lengths = list(segment_lengths)
    print segment_lengths

    return sum(segment_lengths)
#
# #Volume gives the 3D volume of space that each arbor fills within the tissue. It's a measure of how the cells
# #tile the cortical space in 3D
def volume(nodes, edges):

    node_locations = [[node.attrib['x'], node.attrib['y'], node.attrib['z']]for node in nodes]
    hull = ConvexHull(node_locations)
    area = hull.area

    print node_locations
    # print area
    return int(area)

def density(source_target_dict, nodes, edges):
    source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
    target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
    combined_node_pairs = source_target_pairs + target_source_pairs
    target_nodes = [pair[0] for pair in combined_node_pairs]
    source_nodes = [pair[1] for pair in combined_node_pairs]
    combined_source_targets_flat = target_nodes + source_nodes
    unique_nodes_set = set(combined_source_targets_flat)
    unique_nodes = list(unique_nodes_set)

    branch_node_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) > 5]
    # print branch_node_list


    # node_id_list= [node.attrib['id'] for node in nodes]
    # node_id_set= set(node_id_list)
    tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
    # print tip_list

    branch_node_tips = branch_node_list + tip_list

    segment_list = [path_finder(source_target_dict, node2, node) for node2 in branch_node_tips for node in
                    branch_node_tips]
    segment_list = [segment for segment in segment_list if segment is not None]
    segment_list = [segment for segment in segment_list if len(segment) > 1]
    # print segment_list
    # print len(segment_list)

    unique_segment_list1 = []
    for segment in segment_list:
        # print segment
        branch_node_tip_found = 0
        for node in branch_node_tips:
            if node in segment[1:-1]:
                branch_node_tip_found = 1
        if branch_node_tip_found == 0:
            unique_segment_list1.append(segment)
    # print unique_segment_list
    #
    unique_segment_list = set(frozenset(item) for item in unique_segment_list1)
    unique_segment_list = [list(item) for item in unique_segment_list]

    real_segments = []
    for match in unique_segment_list:
        segment_found = 0
        for segment in unique_segment_list1:
            if segment_found == 0:
                segment_set = set(segment)
                match_set = set(match)
                if segment_set == match_set:
                    real_segments.append(segment)
                    segment_found = 1
    unique_segment_list = real_segments

    node_location = node_location_finder(nodes, edges)
    segment_lengths = []
    for segment in range(0, len(unique_segment_list)):
        matches = [item for item in node_location if item[0] in unique_segment_list[segment]]
        if matches == []:
            segment_lengths.append(0)
        else:
            matches_nodes = [match[0] for match in matches]
            matches_index = [unique_segment_list[segment].index(node) for node in matches_nodes]
            # print matches_index
            sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
            int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
            # print int_matches
            # pri print int_matches


            interpoint_distance = 0
            for match in range(0, len(int_matches) - 1):
                interpoint_distance = interpoint_distance + distance.euclidean(int_matches[match][1:4],
                                                                               int_matches[match + 1][1:4])
                # print int_matches[match][1:4]

            segment_lengths.append(interpoint_distance)

    segment_lengths = set(segment_lengths)
    segment_lengths = list(segment_lengths)
    arbor_length = sum(segment_lengths)

    node_locations = [[node.attrib['x'], node.attrib['y'], node.attrib['z']] for node in nodes]
    hull = ConvexHull(node_locations)
    area = hull.area

    density = (arbor_length/area)

    # print density
    return density




#Sholl gives the number of intersections at given distances from the soma. Distances can be chosen as desired
def sholl(source_target_dict, nodes, edges):
   #This stuff is a direct copy from branch_lengths. All is necessary for Sholl, but we want it to be independent
   source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
   target_source_pairs = [[edge.attrib['target'], edge.attrib['source']] for edge in edges]
   combined_node_pairs = source_target_pairs + target_source_pairs
   target_nodes = [pair[0] for pair in combined_node_pairs]
   source_nodes = [pair[1] for pair in combined_node_pairs]
   combined_source_targets_flat = target_nodes + source_nodes
   unique_nodes_set = set(combined_source_targets_flat)
   unique_nodes = list(unique_nodes_set)

   branch_node_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) > 5]
   # print branch_node_list

   tip_list = [node for node in unique_nodes if combined_source_targets_flat.count(node) == 2]
   # print tip_list

   branch_node_tips = branch_node_list + tip_list

   segment_list = [path_finder(source_target_dict, node2, node) for node2 in branch_node_tips for node in
                   branch_node_tips]
   segment_list = [segment for segment in segment_list if segment is not None]
   segment_list = [segment for segment in segment_list if len(segment) > 1]
   # print segment_list
   # print len(segment_list)

   unique_segment_list1 = []
   for segment in segment_list:
       # print segment
       branch_node_tip_found = 0
       for node in branch_node_tips:
           if node in segment[1:-1]:
               branch_node_tip_found = 1
       if branch_node_tip_found == 0:
           unique_segment_list1.append(segment)

   unique_segment_list = set(frozenset(item) for item in unique_segment_list1)
   unique_segment_list = [list(item) for item in unique_segment_list]

   real_segments = []
   for match in unique_segment_list:
       segment_found = 0
       for segment in unique_segment_list1:
           if segment_found == 0:
               segment_set = set(segment)
               match_set = set(match)
               if segment_set == match_set:
                   real_segments.append(segment)
                   segment_found = 1
   unique_segment_list = real_segments


   node_location = node_location_finder(nodes, edges)
   node_id_list = [node.attrib['id'] for node in nodes]
   radii_list = [node.attrib['radius'] for node in nodes]
   soma_node = str((node_id_list[radii_list.index(max(radii_list))]))
   soma_node_index = radii_list.index(max(radii_list))
   soma_coords = node_location[soma_node_index]
   # print soma_coords
   soma_coords = [int(node) for node in soma_coords]

   soma_to_node_distances = []
   for segment in range(0, len(unique_segment_list)):
       matches = [item for item in node_location if item[0] in unique_segment_list[segment]]
       if matches == []:
           soma_to_node_distances.append(0)
       else:
           matches_nodes = [match[0] for match in matches]
           matches_index = [unique_segment_list[segment].index(node) for node in matches_nodes]
           # print matches_index
           sorted_matches = [x for _, x in sorted(zip(matches_index, matches))]
           int_matches = [[int(coordinate) for coordinate in match] for match in sorted_matches]
           # print int_matches
           int_matches = [[int(coordinate) for coordinate in match] for match in matches]
   #distance from soma to each node in each pair of nodes
       for match in range(0, len(int_matches) - 1):
           soma_to_node_pairs = []
           soma_to_node_pairs.append(distance.euclidean(soma_coords[1:4], int_matches[match][1:4]))
           soma_to_node_pairs.append(distance.euclidean(soma_coords[1:4],int_matches[match + 1][1:4]))
           soma_to_node_distances.append(soma_to_node_pairs)
    # return soma_to_node_distances
   # print len(soma_to_node_distances)
#Start original material here
# This bit specifies the radius of the "sholl circle" at which we're counting. We're starting with 0-300 in 10 pix steps
   radii_list = range(0,500,10)
   # print len(radii_list)
   sholl_intersections=[]
   for radius in radii_list:
       crosses = 0
       for pair in soma_to_node_distances:
           # print len(soma_to_node_distances)
           if sum([1 if radius - node_distance >= 0 else 0 for node_distance in pair]) == 1:
               crosses = crosses + 1
       sholl_intersections.append(crosses)
        # print crosses
   return list(np.divide(sholl_intersections,2))


