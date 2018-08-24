with open('dirtest/C.py', "r") as f:
    pass
import os
print os.getcwd()
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path
print os.path.realpath(__file__)
print __file__
print os.path.abspath('C.py')
cwd = os.getcwd()
os.chdir(os.path.dirname(__file__))
print os.path.abspath('C.py')
os.chdir(cwd)
print os.path.relpath('/Users/chensuim/17zuoye/learn/dirtest/C.py')
