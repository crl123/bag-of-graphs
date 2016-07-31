import numpy as np
import json

def load_graph_from_json(file_name):
    """
        loads a graph from a json file
    """
    with open(file_name) as data_file:
        data = json.load(data_file)
    return data

def get_list_nodes(G):
    """
        returns list of nodes for graph G
    """
    return [node['id'] for node in G['nodes']]

def get_list_adj_nodes(G, node):
    """
        returns the list of adjacent nodes in G for node
    """
    return [edge['target'] for edge in G['edges'] if edge['source'] == node]

def create_graph(text, save_json=False, path_json=None):
    """
    """
    return None

def gen_matrix(G1, G2):
    return None

def calc_distance(M):
    """
    """
    return None



"""
SAMPLE:
-------

import graph_utils

G = graph_utils.read_graph_from_json('sample.json')
print graph_utils.get_list_nodes(G)
print graph_utils.get_adj_nodes(G, 'casa')

"""
