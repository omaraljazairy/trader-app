from mysql.connector import Error
from db import db_conn
from decorators.info_collectors import time_memory
from enums import QueryType, DataSource, DataReturnType


class DataManager:
    """ Contains the main query functions where all db models can inherit from. """

    def __init__(self):
        """ initalize the db connection. """
        
        self.dbconn = db_conn()


    def get_data(self, model, query_name=str, data_source=DataSource, query_args=(), query_type=QueryType, data_return_type=DataReturnType):
        """ 
        communicates with different datasources, mysql, postgresql and redis. this will be the main 
        function that other classes interact with.
        takes a model, query_args, data_source,  query_type and data_return_type. based on the values
        it will call the mysql_data function and return the data.  
        
        from the query_name it will get the query and use the args to pass them as arguments.
        It expects the child class to have the get_query function that returns the query.
        """

        query = getattr(model, 'get_query')(model, query_name)
        print('query: ', query_name)
        print('model: ', model)
        return_type = True if data_return_type.value == 'dict' else False
        print('returntype: ', return_type)
        # print('model: ', model)
        

        if data_source.value == 'mysql':
            return self._mysql_data(sql=query, query_args=query_args, return_type=return_type, query_type=query_type)
        elif data_source.value == 'postgresql':
            return self._postgresql_data()
        elif data_source.value == 'redis':
            return self._redis_data()
        else:
            raise Exception("Unknown data source")
    


    def _mysql_data(self, sql=str, **kwargs):
        """ 
        connects to the mysql db to get/update/insert/delete data.
        
        :param sql: a string represents the sql query to be executed.
        :param query_args: a tuple of args if required for the query.
        :param query_type: an Enum QueryType instance.
        """

        query_args = kwargs.get('query_args', None)
        isDict = kwargs.get('return_type', False) # return type either dict if True or tuple if False
        query_type = kwargs.get('query_type', QueryType.FETCHONE )
        
        print('sql: ', sql)
        cursor = self.dbconn.cursor(dictionary=isDict)
        try:
            cursor.execute(sql, query_args)
            if query_type.value == 'fetchone':
                records = cursor.fetchone()
                cursor.close()
                return records
            elif query_type.value == 'fetchall':
                records = cursor.fetchall()
                cursor.close()
                return records
            elif query_type.value == 'insert':
                self.dbconn.commit()
                cursor.close()
            else:
                raise Exception('Unknown query type')
        except Error as error:
            print("sql error: %s", str(error))
        finally:
            # close the cursor in all cases
            cursor.close()


    def _redis_data(self):
        """ connect to Redis """
        pass

    def _postgresql_data(self):
        """ connect to postgresql. """
        pass
    

