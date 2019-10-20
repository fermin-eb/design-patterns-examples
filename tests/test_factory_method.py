import pytest


from design_patterns.factory_method.creator import (
    QueryCreator,
    DatawarehouseQueryCreator,
    SqlQueryCreator
)


def test_get_query_by_abstract_creator_throw_exception():
    creator = QueryCreator()
    with pytest.raises(Exception):
        creator.create()


def test_get_query_sql_by_creator_dw():
    creator = DatawarehouseQueryCreator()
    query = creator.create()
    assert query.run() == 'DW'


def test_get_query_sql_by_creator_sql():
    creator = SqlQueryCreator()
    query = creator.create()
    assert query.run() == 'SQL'
