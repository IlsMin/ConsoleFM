import pytest
import os
import sys

import Console_FM

def test_check_sys_path():
    tst_path= 'some_test_path'

    Console_FM.check_sys_path(tst_path)
    fullpath = os.path.join( os.getcwd(), tst_path)
    assert (fullpath in sys.path, True)
    # f'sys.path not contains {fullpath}'

def test_getDirName():
   
    exists, path = Console_FM.getDirName("")
    assert( exists == os.path.exists(path), True)
#assert exists == os.path.exists(path)


