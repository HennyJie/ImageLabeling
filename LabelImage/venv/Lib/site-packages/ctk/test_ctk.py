import os

def test_py2():
    ''' make sure the file is valid for py2 '''
    assert os.system('py -2 -c "import ctk"') == 0

def test_py3():
    ''' make sure the file is valid for py3 '''
    assert os.system('py -3 -c "import ctk"') == 0
