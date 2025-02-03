from _typeshed import SupportsGetItem

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def min_cost_flow_cost(G: Graph[_Node], demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
@_dispatchable
def min_cost_flow(G: Graph[_Node], demand: str = "demand", capacity: str = "capacity", weight: str = "weight"): ...
@_dispatchable
def cost_of_flow(G: Graph[_Node], flowDict: SupportsGetItem, weight: str = "weight"): ...
@_dispatchable
def max_flow_min_cost(G: Graph[_Node], s: str, t: str, capacity: str = "capacity", weight: str = "weight"): ...
