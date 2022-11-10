import unittest
#from app import inc
from ..test.src.app import inc

class app_test(unittest.TestCase):
  def test_index(self):
    #self.assert inc(3) == 4
    self.assertEqual(inc(3), 4)
    