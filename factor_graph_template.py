import numpy as np
from pgmpy.models import FactorGraph
from pgmpy.factors.discrete import DiscreteFactor
import json

class FactorGraphEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DiscreteFactor):
            return {
                "__class__": "DiscreteFactor",
                "__value__": {
                    "variables": [str(variable) for variable in obj.variables],
                    "cardinality": [int(card) for card in obj.cardinality],
                    "values": obj.values.tolist()
                }
            }
        return super().default(obj)

G = FactorGraph()
G.add_nodes_from(['a', 'b', 'c'])
phi1 = DiscreteFactor(['a', 'b'], [2, 3], np.random.rand(6))
phi2 = DiscreteFactor(['b', 'c'], [2, 4], np.random.rand(8))
G.add_factors(phi1, phi2)
G.add_nodes_from([phi1, phi2])
G.add_edges_from([('a', phi1), ('b', phi1),
                  ('b', phi2), ('c', phi2)])

# Serialize the data using the custom encoder
data = {
    "nodes": list(G.nodes()),
    "factors": G.get_factors(),
    "edges": list(G.edges())
}

with open('factor_graph.json', 'w') as json_file:
    json.dump(data, json_file, cls=FactorGraphEncoder, indent=4)