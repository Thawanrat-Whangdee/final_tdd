from function import validate_number,amount_of_vehicle
import pytest 

@pytest.mark.code #pytest => code
def test_people_morethan_11_12():
    input = 12
    excepted_result = ('1', ' van','1', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_23():
    input = 23
    excepted_result = ('2', ' van','1', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_29():
    input = 29
    excepted_result = ('2', ' van','2', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_equal_11():
    input = 11
    excepted_result = ('1', ' van','0', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_10():
    input = 10
    excepted_result = ('0', ' van','3', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_8():
    input = 8
    excepted_result = ('0', ' van','2', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_3():
    input = 3
    excepted_result = ('0', ' van','1', ' car')
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_char_a():
    input = "a"
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_amount_of_people_input_0():
    input = 0
    excepted_result = "input amount of people"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_minus_1():
    input = -1
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_1_5():
    input = 1.5
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_minus_1_5():
    input = -1.5
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_char_sharp():
    input = "#"
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result