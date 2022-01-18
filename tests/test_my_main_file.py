import sys
import os
from unittest import mock

sys.path.append(os.path.join(__file__, "..", ".."))

from my_main_file import suma

def test_suma():
    x = 1
    y = 3
    res = suma(x, y)
    assert res == 4