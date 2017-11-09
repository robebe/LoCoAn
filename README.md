# LoCoAn
#### Implementation of Lowest Common Ancestor in a directed acyclic graph structure.

## Prerequesites
(Note that a GNU/Linux distribution is assumed for the following commands. Changes might apply for macOS or Windows.)
Have Python 2.7 or later installed on your machine.
To download this repository open a terminal and enter:
```
git clone https://github.com/robebe/LoCoAn.git
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
from dag import DirectedAcyclicGraph
```
The scripts can now be called typing the following command in your terminal:
```
python test_initial.py -v
python test_lca.py -v
```
