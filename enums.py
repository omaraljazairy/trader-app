from enum import Enum


class QueryType(Enum):
    """ define the query types accepted. """

    FETCHONE = 'fetchone'
    FETCHALL = 'fetchall'
    INSERT = 'insert'

class DataSource(Enum):
    """ define the datasource expect to use. """

    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'
    REDIS = 'redis'

class DataReturnType(Enum):
    """ define the return types possible to get from data sources. """

    LIST = 'list'
    TUPLE = 'tuple'
    JSON = 'json'
    DICTIONARY = 'dict'