from abc import (
    ABCMeta,
    abstractmethod,
)


class Query(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        raise NotImplementedError('run')


class QuerySQL(Query):
    def run(self):
        return "SQL"


class QueryDW(Query):
    def run(self):
        return "DW"
