from trades import get_revenue

def test_get_revenue_previouse_balance_gt_0():
    """ 
    provide a balance and previous balance greater than 0.00 and expect to 
    get back a decimal number. 
    """

    balance = 10.00
    previous_balance = 8.00
    expected_revenue = 2.00

    revenue = get_revenue(balance, previous_balance)

    assert revenue == expected_revenue


def test_get_revenue_previouse_balance_eq_0():
    """ 
    provide a balance and previous balance of 0.00 and expect to get back a 
    the revenue 0.00 . 
    """

    balance = 10.00
    previous_balance = 0.00
    expected_revenue = 0.00

    revenue = get_revenue(balance, previous_balance)

    assert revenue == expected_revenue

