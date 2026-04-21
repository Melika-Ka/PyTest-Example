import pytest
def sum_numbers(numn1 , num2):
     return numn1 + num2
# way1
@pytest.mark.parametrize("num1,num2,result",[(1,2,3) , (2,3,5) , (3,4,7)])

def test_sum_numbers_way1(num1 , num2 , result):
    assert sum_numbers(num1 , num2) == result

# way2
@pytest.fixture(params=[(1,2,3) , (2,3,5) , (3,4,7)])
def sum_parameters(request):
     return request.param

def test_sum_numbers_way2(sum_parameters):
        num1= sum_parameters[0]
        num2= sum_parameters[1]
        assert sum_numbers(num1, num2) == sum_parameters[2]

