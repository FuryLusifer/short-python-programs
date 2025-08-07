# Write a test file for Employee with two test functions, test_give_default
# _raise() and test_give_custom_raise(). Write your tests once without using a
# fixture, and make sure they both pass. Then write a fixture so you don’t
# have to create a new employee instance in each test function. Run the tests
# again, and make sure both tests still pass

import pytest
from employee import Employee

@pytest.fixture
def emp():
    emp = Employee("Piyush", "Kayastha", 50000)
    return emp

def test_give_default_raise(emp):
    # emp = Employee("Piyush", "Kayastha", 50000)
    new_salary = emp.give_raise()
    assert new_salary == 55000

def test_give_custom_raise(emp):
    # emp = Employee("Piyush", "Kayastha", 50000)
    new_salary = emp.give_raise(7000)
    assert new_salary == 57000