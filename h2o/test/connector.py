import h2o
from os import getenv

h2o.connect(url=f"http://{getenv('H2O_HOST', 'h2o')}:54321", verbose=True)
assert h2o.models() == []
