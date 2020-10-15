""" Defines methods that can/should be used by class using this interface. """
from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
    

    @abstractmethod
    def get_query(self, query_name=str, extra=None):
        """ 
        Returns a query string that belongs to the table.

        takes two parameters, the query_name where the query belongs to and an optional
        extra param, default is None but can be used for added more options to select
        a query.
        
        """

        raise NotImplementedError('method should be implemented')

