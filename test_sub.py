import pytest
from add import sub

def test_sub():
    assert sub(1, 1)==0
    assert sub(-1, 1)==-2
    assert sub(0, 0)==0
    assert sub(10, 8)==2

