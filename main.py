from evcnet import Evcnet

e = Evcnet(
    url='https://evcompany.evc-net.com',
    username='h.kraal@exonet.nl',
    password='secret',
)
data = e.total_usage()
