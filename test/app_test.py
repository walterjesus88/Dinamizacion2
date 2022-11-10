import unittest
import os
import path
print(os.path.normpath(os.getcwd() + os.sep + os.pardir))

print(os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), "src"))
new_path = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), "src")
# importing sys
import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, new_path)
  
# importing the hello
from app import inc
  

class app_test(unittest.TestCase):
  def test_index(self):
    #self.assert inc(3) == 4
    self.assertEqual(inc(3), 4)