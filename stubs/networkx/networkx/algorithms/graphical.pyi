from collections.abc import Iterable

from networkx.utils.backends import _dispatchable

@_dispatchable
def is_graphical(sequence: Iterable, method="eg"): ...
@_dispatchable
def is_valid_degree_sequence_havel_hakimi(deg_sequence: Iterable): ...
@_dispatchable
def is_valid_degree_sequence_erdos_gallai(deg_sequence: Iterable): ...
@_dispatchable
def is_multigraphical(sequence: Iterable): ...
@_dispatchable
def is_pseudographical(sequence: Iterable): ...
@_dispatchable
def is_digraphical(in_sequence: Iterable, out_sequence: Iterable): ...
