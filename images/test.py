import matplotlib.pyplot as plt 
import networkx as nx
import pandas as pd 

from pgmpy.utils import get_example_model
from pgmpy.inference import BeliefPropagation

from IPython.display import display, Image

asia_model = get_example_model('asia')

edges = asia_model.edges()
nodes = asia_model.nodes()

G = nx.DiGraph()
G.add_edges_from(edges)

asia_model.