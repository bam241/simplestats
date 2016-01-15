from stats import mean
from nose.tools import assert_equal, assert_almost_equals

def test_mean():
	assert_equal(mean([2,4]), 3)
#test_mean()

def test_empty_list():
	assert mean([]) == 0
#test_empty_list()

def test_float_mean():
	assert_almost_equals(mean([.5,.5,1]), .66, 1) # .66, 1-> can choose the degree of precision by changing 1 to 2, 3, 4..
#test_float_mean()


def test_str_list_mean():
	assert_equal(mean(['1','2','3']), 2.0)

