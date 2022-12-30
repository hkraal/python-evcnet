from evcnet import Evcnet


def test_total_usage():
    e = Evcnet(
        url='https://evcompany.evc-net.com',
        username='h.kraal@exonet.nl',
        password='secret',
    )
    data = e.total_usage()
    assert 'totalUsage' in data.keys()
    assert 'totalProvided' in data.keys()
