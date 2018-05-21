import os
import xml.etree.ElementTree as ET
import glob
from scipy.spatial import distance
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

# def source_target(edges):
#     source_target_pairs = [[edge.attrib['source'], edge.attrib['target']] for edge in edges]
#     source_target_dict = dict()
#
#     for pair in source_target_pairs:
#         if pair[0] in source_target_dict:
#             # append the new number to the existing array at this slot
#             source_target_dict[pair[0]].append(pair[1])
#         else:
#             # create a new array in this slot
#             source_target_dict[pair[0]] = [pair[1]]
#     return source_target_dict

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

def path_finder(source_target_dict, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not source_target_dict.has_key(start):
        return None
    for node in source_target_dict[start]:
        if node not in path:
            newpath = path_finder(source_target_dict, node, end, path)
            if newpath: return newpath
    return None

def broken_path_finder(source_target_dict, nodes, edges):
    source_list = [edge.attrib['source'] for edge in edges]
    source_set = set(source_list)
    node_id_list = [node.attrib['id'] for node in nodes]
    node_id_set = set(node_id_list)
    tip_list = list(node_id_set - source_set)
    # print tip_list
    radii_list = [node.attrib['radius'] for node in nodes]
    soma_node = node_id_list[radii_list.index(max(radii_list))]
    path_list = [path_finder(source_target_dict, soma_node, tip) for tip in tip_list]


    path_list = [path for path in path_list if path is not None]
    # print path_list
    broken_paths =[]
    # print path_list[0][-1]
    for path in path_list:
        if path[-1] in tip_list:
            broken_paths.append(path[-1])
        # print path[-1]
    # print broken_paths

    tip_set = set(tip_list)
    # print tip_set
    broken_paths_set = set(broken_paths)
    # print broken_paths_set
    broken_paths_set_unique = tip_set-broken_paths_set

    return broken_paths_set_unique


def multi_target_finder(nodes, edges):
    target_list = [edge.attrib['target'] for edge in edges]
    problematic_targets= [target for target in target_list if target_list.count(target)>1]
    print problematic_targets

