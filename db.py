import logging
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)
from prom import Orm, Field, Index, Query
import prom
prom.configure('sqlite://db.sqlite')



class Qry(Query):
    """
    Query class
    Use for all our events queries
    """
    def get_last_n(self, rows:str=100) -> list:
        """
        Return the last-n rows
        """
        return self.all().limit(rows).desc()

class Event(Orm):
    """
    Here we define an event table for storing our data
    We can also use similar tables to store e.g. people names & employee numbers, etc.
    """
    table_name='events'
    query_class=Qry
    event_timestamp = Field(datetime)
    employee_name = Field(str, max_size=512)
    event_description = Field(str)
    event_result = Field(str, max_size=512)


class Person(Orm):
    """
    Store a person here if you want. Unused at the moment
    We would define the employee in events table to be a foreign key into this table's primary key
    All tables get a 'pk' field
    """
    table_name = 'person'
    surname = Field(str)
    forename = Field(str)
    is_staff = Field(bool)
    # etc.


if __name__ == '__main__':
    print('We should be called as a module!')
    logger.error('MODULE ONLY')
