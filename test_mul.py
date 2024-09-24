import pytest
from add import mul

def test_mul():
    assert mul(1, 1)==1
    assert mul(-1, 1)==-1
    assert mul(0, 0)==0
    assert mul(2, 4)==8
    assert mul(-2, -2)==4


