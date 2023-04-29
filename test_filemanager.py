import pytest
import os
import sys

import Console_FM as cfm
import io


def test_check_sys_path():
    path = 'test_path'
    cfm.check_sys_path(path)
    fullpath = os.path.join( os.getcwd(), path)
    assert (fullpath in sys.path, True)
    # f'sys.path not contains {fullpath}'

def test_getDirName():
    exists, path = cfm.getDirName("")
    assert( exists == os.path.exists(path), True)
#assert exists == os.path.exists(path)

def test_print_decorator():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    cfm.show_file_or_dir(True)                      # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    # print ('Captured', capturedOutput.getvalue())   # Now works as before.
    # assert (capturedOutput.getvalue(), cfm.rezultPrinting(cfm.show_file_or_dir(True)) )
    assert (capturedOutput.getvalue(), cfm.rezultPrinting(cfm.get_file_or_dir(True)) )
    


