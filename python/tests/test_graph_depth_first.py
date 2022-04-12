import pytest
from code_challenges.graph.graph import Graph


def test_zero_size():
    graph = Graph()
    assert graph.size() == 0


def test_empty_graph():
    graph = Graph()
    assert graph.get_nodes() == []


def test_add_node():
    graph = Graph()
    A = graph.add_node("A")
    expected = [A]
    actual = graph.get_nodes()

    assert expected == actual


def test_add_edge():
    graph = Graph()
    A = graph.add_node("A")
    B = graph.add_node("B")
    graph.add_edge(A, B, 3)


def test_retrieve_nodes():
    graph = Graph()
    A = graph.add_node("A")
    B = graph.add_node("B")
    C = graph.add_node("C")
    D = graph.add_node("D")

    actual = graph.get_nodes()
    expected = [A, B, C, D]
    assert expected == actual


def test_proper_size_of_nodes():
    graph = Graph()
    A = graph.add_node("A")
    B = graph.add_node("B")
    C = graph.add_node("C")
    D = graph.add_node("D")

    actual = len(graph.get_nodes())
    expected = 4
    assert expected == actual
