import os
import xml.etree.ElementTree as ET
import glob

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
def branch_number(edges):
    source_list = [edge.attrib['source'] for edge in edges]
    source_set = set(source_list)
    unique_sources = list(source_set)
    source_count = [source_list.count(source) if source_list.count(source) > 1 else 0 for source in unique_sources]
    return sum(source_count)

#tip_number is the count of nodes/sources that have no targets
def tip_number(nodes,edges):
    source_list = [edge.attrib['source'] for edge in edges]
    source_set = set(source_list)
    node_id_list= [node.attrib['id'] for node in nodes]
    node_id_set= set(node_id_list)
    tip_set = node_id_set-source_set
    tip_count=len(tip_set)
    return tip_count








