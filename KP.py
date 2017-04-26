#!/usr/bin/python3

# global requirements
import logging

# local requirements
from ConnectionHandler import *

# class KP
class LowLevelKP:

    """This is the Low-level class used to develop a KP"""

    # constructor
    def __init__(self, host, updatePath, queryPath, registrationPath, tokenReqPath, # paths
                 httpPort, httpsPort, wsPort, wssPort, # ports                 
                 secure): # security    
        
        """Constructor for the Low-level KP class"""

        # logger configuration
        self.logger = logging.getLogger("sepaLogger")
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        self.logger.debug("Initializing KP")

        # initialize data structures
        self.subscriptions = {}

        # initialize handler
        self.connectionManager = ConnectionHandler(host, updatePath, queryPath, registrationPath, tokenReqPath, # paths
                                                   httpPort, httpsPort, wsPort, wssPort, # ports
                                                   secure)


    # TODO -- update
    def update(self, sparqlUpdate):

        """This method is used to perform a SPARQL update"""
        
        # debug print
        self.logger.debug("Performing a SPARQL update")

        # perform the update request
        text = self.connectionManager.updateRequest(sparqlUpdate)
        


    # query
    def query(self, sparqlQuery):

        """This method is used to perform a SPARQL query"""

        # debug print
        self.logger.debug("Performing a SPARQL query")
        
        # perform the query request
        text = self.connectionManager.queryRequest(sparqlQuery)
        

    # TODO -- subscribe
    def subscribe(self):
        pass
        
    
    # TODO -- unsubscribe
    def unsubsribe(self):
        pass
