import os
from decorators.info_collectors import time_memory
from styles.styles import style, html_label
from prompt_toolkit import print_formatted_text
from prompt_toolkit.shortcuts import prompt, message_dialog, radiolist_dialog
from prompt_toolkit.validation import Validator, ValidationError
from dotenv import load_dotenv
load_dotenv() # load env vars before loading any modules

from models.trades import Trades
from models.datamanager import DataManager
from enums import QueryType, DataSource, DataReturnType

# from datetime import datetime, timezone
import decimal
from pytz import timezone
from tabulate import tabulate

# history = FileHistory('history.txt')
# session = PromptSession()
# create an instance of the datamanger class
datamanager = DataManager()

#===================== Validators ===========================
# validate input is decimal
def is_decimal_or_integer(text):
    try:
        decimal.Decimal(text)
        return True
    except ValueError:
        return False

decimal_validator = Validator.from_callable(
    is_decimal_or_integer,
    error_message='input has to be decimal',
    move_cursor_to_end=True
)

# validate input is an int
def is_int(text):
    return text.isdigit()

int_validator = Validator.from_callable(
    is_int,
    error_message='ERROR: Input has to be an Integer',
    move_cursor_to_end=True
)



#@time_memory
def get_revenue(new_balance, previous_balance):
    """ 
    calculates the revenue from the previous balance - balance.
    
    :param new_balance: decimal the represents the new balance.
    :param previous_balance: decimal that represents the last recorded balance.
    :returns revenue: decimal value

    takes the balance param and the previous_balance params and returns the revenue.
    """

    revenue = 0.00 if previous_balance == 0.00 else new_balance - previous_balance
    return revenue

#@time_memory
def set_balance(new_balance):
    """ 
    insert the current balance and revenue into the database. 
    
    before inserting it into the db, it will fetch the current balance,
    it will provide it to the get_revenue function to get back the revenue
    """

    # get the current balance to calculate the revenue
    current_balance = Trades().get_current_balance()
    if current_balance:

        # get the revenue
        revenue = get_revenue(new_balance, current_balance['Balance'])

        # insert the new balance
        inserted_record = Trades().set_balance_record(new_balance, revenue)
        
        txt = "revenue generated: " + str(revenue)
        print_formatted_text(html_label(txt))
    else:
        # if no balance was found, this means it's the first record.
        revenue = 0.00
        inserted_record = Trades().set_balance_record(new_balance, revenue)
        
        txt = "record inserted: " + str(inserted_record)
        print_formatted_text(html_label(txt))


def get_current_balance():
    """ Prints the current balance. """

    # get the current balance to calculate the revenue
    current_balance = datamanager.get_data(Trades, query_name='get_current_balance', data_source=DataSource.MYSQL, query_args=('ETHUSDT',), query_type=QueryType.FETCHONE, data_return_type=DataReturnType.DICTIONARY)  
    
    if current_balance:

        orders = [
            [
                current_balance['Balance'], 
                current_balance['Asset'], 
                current_balance['OrderDate'],
                current_balance['Revenue'], 

            ]
        ]

        data = tabulate(orders, headers=["Balance", "Asset", "OrderDate", "Revenue"], tablefmt="fancy_grid", floatfmt=".2f")
        print_formatted_text(html_label(data))

    else:
        txt = "No Balance found"
        print_formatted_text(html_label(txt))



def get_orders_history(days=1):
    """
    Prints the Orders placed last days. Days is set to a default of 1 day.

    :param days: int of days.
    :returns a print of orders.
    """

    orders = Trades().get_daily_orders(total_days=days, asset='ETHUSDT')
    if orders:
        data = tabulate(orders, headers=["Balance", "Asset", "OrderDate", "Revenue"], tablefmt="fancy_grid", floatfmt=".2f")
        print_formatted_text(html_label(data))
    else:
        print("no records found")


def get_total_daily_revenue_per_day(data=[()]):
    """
    Prints the total revenue per day. takes a list of data.

    :param data: list of tuples
    :returns a print of the revenue per day
    """

    revenue_data = tabulate(data, headers=["Date", "Revenue"], tablefmt="fancy_grid", floatfmt=".2f")
    print_formatted_text(html_label(revenue_data))




if __name__ == '__main__':

    options = [
        (1, 'Add New Balance'),
        (2, 'Check Current Balance with Last Revenue'),
        (3, 'Check Orders History'),
        (4, 'Check Total Revenue per day'),
    ]

    task = radiolist_dialog(
        title="Tasks",
        text="Select a task",
        values=options
    ).run()
    
    if not task:
        print("Cancelled")

    elif int(task) == 1:

        balance = prompt(message="enter new balance: ", style=style, validator=decimal_validator,validate_while_typing=True )
    
        set_balance(decimal.Decimal(balance))

    elif int(task) == 2:
        get_current_balance()

    elif int(task) == 3:

        days = prompt(message="how many days back: ", style=style, validator=int_validator,validate_while_typing=True )

        get_orders_history(days=days)

    elif int(task) == 4:

        days = prompt(message="how many days back: ", style=style, validator=int_validator,validate_while_typing=True )
        data = Trades().get_daily_revenue(total_days=days, asset='ETHUSDT')
        get_total_daily_revenue_per_day(data)
        
    else:
        print("unknown options")