from mysql.connector import Error
from db import db_conn
# from datetime import datetime
from decorators.info_collectors import time_memory
from models.datainterface import DataManagerInterface
from models.datamanager import DataManager
import models.sqlqueries as query



class Trades(DataManager, DataManagerInterface):
    """ 
    The Trade model inherits the DataManager class and implements
    the abstract method of the datainterface class.  
    """

    def get_query(self, query_name=str):
        """ select the query to be executed based on the name provided as arg. """
 
        sql_query = {
            'get_current_balance': query.GET_CURRENT_BALANCE,
            'get_daily_orders': query.GET_DAILY_ORDERS,
            'get_daily_revenue': query.GET_DAILY_REVENUE,
            'set_balance': query.SET_BALANCE,
        }

        return sql_query[query_name]

    @time_memory
    def get_current_balance(self, asset='ETHUSDT'):
        """ 
        returns the current balance of the asset provided in the param
        with the datetime it was inserted.
        
        :param asset: str with default value ETHUSDT.
        return dict of the last record for the provided asset.
        """

        sql = """select Balance, Asset, CONVERT_TZ(OrderDate,'UTC','Europe/Amsterdam') as OrderDate, Revenue from Trades where Asset = %s order by Id DESC limit 1"""

        cursor = self.dbconn.cursor(dictionary=True)
        try:
            cursor.execute(sql, (asset,))
            records = cursor.fetchone()
            cursor.close()
            return records
        except Error as error:
            print("Error selecting records with error: %s", str(error))
        finally:
            cursor.close()

    #@time_memory
    def set_balance_record(self, new_balance, revenue=0.00, asset='ETHUSDT'):
        """ 
        takes three params and insert them into the Trades table.

        :param new_balance: decimal represents the new balance.
        :param revenue: optional decimal param.
        :param asset: optional str with default value ETHUSDT.
        """

        values = (new_balance, revenue, asset)
        sql = """ INSERT INTO Trades (Balance, Revenue, Asset) Values (%s, %s, %s) """

        cursor = self.dbconn.cursor()
        try:
            cursor.execute(sql, values)
            self.dbconn.commit()
            cursor.close()
        except Error as error:
            print("Error inserting the records with error: %s", str(error))
        finally:
            cursor.close()


    def get_daily_orders(self, total_days=1, asset='ETHUSDT'):
        """
        Returns the daily orders as a list of dict.

        The parameter total_days will get records from the number of days backwards.
        :param total_days: int default 1 day
        :param asset: str default value ETHUSDT
        :returns: list of tuples
        """

        values = (asset, total_days)
        sql = """ SELECT Balance, Asset, CONVERT_TZ(OrderDate,'UTC','Europe/Amsterdam') as OrderDate, Revenue from Trades where Asset = %s and CONVERT_TZ(OrderDate,'UTC','Europe/Amsterdam') >= CONVERT_TZ(CURDATE(),'UTC','Europe/Amsterdam') - INTERVAL %s DAY order by Id ASC """

        cursor = self.dbconn.cursor()
        try:
            cursor.execute(sql, values)
            records = cursor.fetchall()
            cursor.close()
            return records
        except Error as error:
            print("Error fetching records with error: %s", str(error))
        finally:
            cursor.close()
            

    def get_daily_revenue(self, total_days=1, asset='ETHUSDT'):
        """
        Returns a list of the sum of revenue per date.

        Takes the total_days param to get result based on the total days backwards. 
        the default total_days is 1. Also the asset param has the default 'ETHUSDT'.

        :param total_days: int default 1 day
        :param asset: str default value ETHUSDT
        :returns: list of tuples
        """

        values = (asset, total_days)
        sql = """ SELECT Date(CONVERT_TZ(OrderDate,'+00:00','Europe/Amsterdam')) as OrderDate, SUM(Revenue) from Trades where Asset = %s and CONVERT_TZ(OrderDate,'+00:00','Europe/Amsterdam') >= CONVERT_TZ(CURDATE(),'+00:00','Europe/Amsterdam') - INTERVAL %s DAY group by 1 order by 1 ASC """

        cursor = self.dbconn.cursor()
        try:
            cursor.execute(sql, values)
            records = cursor.fetchall()
            cursor.close()
            return records
        except Error as error:
            print("Error fetching records with error: %s", str(error))
        finally:
            cursor.close()


    def __del__(self):
        """ destruct the object and close the db connection. """

        self.dbconn.close()


    


