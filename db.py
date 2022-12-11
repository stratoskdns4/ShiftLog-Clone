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
    """
    table_name='events'
    query_class=Qry
    event_timestamp = Field(datetime)
    employee_name = Field(str, max_size=512)
    event_description = Field(str, max_size=512)
    event_result = Field(str)



if __name__ == '__main__':
    print('We should be called as a module!')
    logger.error('MODULE ONLY')
