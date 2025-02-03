from collections.abc import Generator, Iterable, Iterator
from typing import overload

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def enumerate_all_cliques(G: Graph[_Node]) -> Generator[list[_Node], None, None]: ...
@_dispatchable
def find_cliques(G: Graph[_Node], nodes: Iterable | None = None) -> Generator[list[_Node], None, None]: ...
@_dispatchable
def find_cliques_recursive(G: Graph[_Node], nodes: Iterable | None = None) -> Iterator[list[_Node]]: ...
@_dispatchable
def make_max_clique_graph(G: Graph[_Node], create_using: Graph[_Node] | None = None) -> Graph[_Node]: ...
@_dispatchable
def make_clique_bipartite(
    G: Graph[_Node], fpos: bool = None, create_using: Graph[_Node] | None = None, name=None
) -> Graph[_Node]: ...
@overload
def node_clique_number(
    G: Graph[_Node], nodes=None, cliques: Iterable | None = None, separate_nodes=False
) -> dict[_Node, int]: ...
@overload
def node_clique_number(G: Graph[_Node], nodes=None, cliques: Iterable | None = None, separate_nodes=False) -> int: ...
