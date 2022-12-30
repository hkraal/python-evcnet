import os

from evcnet import Evcnet


def test_total_usage():
    e = Evcnet(
        url='https://evcompany.evc-net.com',
        username=os.environ.get('EVCNET_USERNAME'),
        password=os.environ.get('EVCNET_PASSWORD'),
    )
    data = e.total_usage()
    assert 'totalUsage' in data.keys()
    assert 'totalProvided' in data.keys()
