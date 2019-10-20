from design_patterns.factory_method.queries import (
    QuerySQL,
    QueryDW
)


class QueryCreator(object):
    type = None

    def create(self):
        raise NotImplementedError('create')


class DatawarehouseQueryCreator(QueryCreator):
    type = 'DW'

    def create(self):
        return QueryDW()


class SqlQueryCreator(QueryCreator):
    type = 'SQL'

    def create(self):
        return QuerySQL()
