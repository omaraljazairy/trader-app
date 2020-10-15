from enums import QueryType, DataSource, DataReturnType

def test_querytypes_instances():
    """ check that the querytypes fetchone, fetchall and insert exist. """

    fetchall = QueryType.FETCHALL
    fetchone = QueryType.FETCHONE
    insert = QueryType.INSERT

    assert isinstance(fetchall, QueryType)
    assert isinstance(fetchone, QueryType)
    assert isinstance(insert, QueryType)

def test_querytypes_values():
    """ check if the values match the fetchall, fetchone and insert"""

    fetchall = QueryType.FETCHALL
    fetchone = QueryType.FETCHONE
    insert = QueryType.INSERT

    assert fetchone.value == 'fetchone'
    assert fetchall.value == 'fetchall'
    assert insert.value == 'insert'


def test_datasource_type_instances():
    """ test if the mysql, postgresql or redis exist. """

    mysql = DataSource.MYSQL
    postgresql = DataSource.POSTGRESQL
    redis = DataSource.REDIS

    assert isinstance(mysql, DataSource)
    assert isinstance(postgresql, DataSource)
    assert isinstance(redis, DataSource)

def test_datasource_values():
    """ test if the values match mysql, postgresql or redis. """

    mysql = DataSource.MYSQL
    postgresql = DataSource.POSTGRESQL
    redis = DataSource.REDIS

    assert mysql.value == 'mysql'
    assert postgresql.value == 'postgresql'
    assert redis.value == 'redis'

def test_datareturntype_instances():
    """ test if the expected tuple, list, json and dictionary instances exist"""

    json_type = DataReturnType.JSON
    list_type = DataReturnType.LIST
    tuple_type = DataReturnType.TUPLE
    dict_type = DataReturnType.DICTIONARY

    assert isinstance(json_type, DataReturnType)
    assert isinstance(list_type, DataReturnType)
    assert isinstance(tuple_type, DataReturnType)
    assert isinstance(dict_type, DataReturnType)


def test_datareturntype_values():
    """ test if the values match list, json, dict and tuple. """

    json_type = DataReturnType.JSON
    list_type = DataReturnType.LIST
    tuple_type = DataReturnType.TUPLE
    dict_type = DataReturnType.DICTIONARY

    assert json_type.value == 'json'
    assert list_type.value == 'list'
    assert tuple_type.value == 'tuple'
    assert dict_type.value == 'dict'



