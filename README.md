# LoCoAn
#### Implementation of Lowest Common Ancestor in a Binary Tree.
This python based project implements one of the many possible solutions to finding the Lowest Common Ancestor in a Binary Tree structure. 

## Prerequesites
Have Python 2.7 or later installed on your machine.
To download this repository open a terminal and enter:
```
git clone https://github.com/robebe/LoCoAn.git
```

## Run Demo
Make *demo.sh* executable and run it by typing:
```
chmod +x demo.sh
./demo.sh
```
## Run Tests
Run all Unittest scripts contained in folder "./test/" by executing *run_tests.sh*:
```
chmod +x run_test.sh
./run_test.sh
```
If you wish to execute each test script by itself, navigate to "./test/" and uncomment/comment the line 6 to 12 as follows:
```python
import unittest
import os, sys
src_path = os.path.abspath(os.path.join('..','src'))
sys.path.append(src_path)
"""
src_path = os.path.abspath('src')
sys.path.append(src_path)
"""
from binary_tree import Node, BinaryTree
```
The scripts can now be called typing the following command in your terminal:
```
python test_initial.py -v
python test_lca.py -v
python test_tree_repr.py -v
```
