import pytest
pytest.mark.parameterize("num",[1,2,3])
def test_numbers(num):
    print(num)
