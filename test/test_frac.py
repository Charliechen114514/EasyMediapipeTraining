import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from ParamsSettings.fraction_creator import FractionOfDataset
import math

TOLORANCE = 1e-9

def test_fractions():
    frac = FractionOfDataset()
    result = frac.transform_to_mediapipe()
    assert all(not math.isnan(each) and not abs(each) < TOLORANCE for each in result)
    print(result)

    frac.set_split_param(2, 1, 1)
    result = frac.transform_to_mediapipe()
    assert all(not math.isnan(each) and not abs(each) < TOLORANCE for each in result)
    print(result)

    try:
        frac.set_split_param(0, 0, 0)
        frac.check_params()
        # if the assertion success, then it will not failed the test
        assert 0
    except ValueError as e:
        print("Can not set the params, contains 0 or None!")


