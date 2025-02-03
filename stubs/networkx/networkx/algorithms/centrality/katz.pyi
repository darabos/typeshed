from _typeshed import SupportsGetItem

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def katz_centrality(
    G: Graph[_Node],
    alpha: float | None = 0.1,
    beta: float | SupportsGetItem | None = 1.0,
    max_iter: int | None = 1000,
    tol: float | None = 1e-06,
    nstart: SupportsGetItem | None = None,
    normalized: bool | None = True,
    weight: str | None = None,
): ...
@_dispatchable
def katz_centrality_numpy(
    G: Graph[_Node],
    alpha: float = 0.1,
    beta: float | SupportsGetItem | None = 1.0,
    normalized: bool = True,
    weight: str | None = None,
): ...
