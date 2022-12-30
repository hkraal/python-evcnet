import os

from dotenv import load_dotenv

from evcnet import Evcnet

load_dotenv()

e = Evcnet(
    url='https://evcompany.evc-net.com',
    username=os.environ.get('EVCNET_USERNAME'),
    password=os.environ.get('EVCNET_PASSWORD'),
)
data = e.total_usage()
print(data)
