from models.trades import Trades
import models.sqlqueries as query

def test_get_query_string():
    """ Check the get_query function exists and returns a query string. """

    trades = Trades()
    query = trades.get_query(query_name='get_daily_revenue')

    assert type(query) == str

def test_queries():
    """ 
    test if the query_name will return the same value from the sqlqueires 
    string.
    """

    trades = Trades()
    get_current_balance_sql = trades.get_query(query_name='get_current_balance')
    get_daily_orders_sql = trades.get_query(query_name='get_daily_orders')
    get_daily_revenue_sql = trades.get_query(query_name='get_daily_revenue')
    set_balance_sql = trades.get_query(query_name='set_balance')
    
    assert get_daily_orders_sql == query.GET_DAILY_ORDERS
    assert get_daily_revenue_sql == query.GET_DAILY_REVENUE
    assert get_current_balance_sql == query.GET_CURRENT_BALANCE
    assert set_balance_sql == query.SET_BALANCE