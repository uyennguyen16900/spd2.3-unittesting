import math
import pytest

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio <= 0:
        raise ValueError('Invalid input! Input must be between 0 and 1.')
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF 

# Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.

def test_get_age_carbon_14_dating():
    res = get_age_carbon_14_dating(0.35)
    assert math.isclose(res, 8680.34, rel_tol=1e-2)
    
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)

    with pytest.raises(ValueError):
        get_age_carbon_14_dating(-2)
    


# print(get_age_carbon_14_dating(-4))