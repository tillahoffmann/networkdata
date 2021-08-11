import pytest
import networkx as nx


@pytest.fixture(params=range(1, 85), scope='session')
def graph(request):
    return nx.read_graphml(f'addhealth/data/community_{request.param}.xml')


def test_addhealth_attributes(graph):
    # Validate all the attributes.
    for node in graph:
        attributes = graph.nodes[node]
        assert attributes['sex'] in {'male', 'female', 'unknown'}
        assert attributes['race'] in {'white', 'black', 'asian', 'hispanic', 'mixed/other',
                                      'unknown'}
        assert attributes.get('school', None) in {0, 1, None}
        assert attributes['grade'] in {0, 6, 7, 8, 9, 10, 11, 12}
