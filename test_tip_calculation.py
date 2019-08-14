from tip_calculation import tip_calc
def test_tip_calc():
    tip_amount, total_amount = tip_calc(10, 1.5)
    assert tip_amount == 15
    assert total_amount == 25

def test_tip_calc_char():
    result = tip_calc('dsf', 15)
    assert result==None