#!/usr/bin/python3

# global requirements
import json
import logging

# local requirements
from ConnectionHandler import *

# class KP
class LowLevelKP:

    """This is the Low-level class used to develop a KP"""

    # constructor
    def __init__(self, host, updatePath, queryPath, registrationPath, tokenReqPath, # paths
                 httpPort, httpsPort, wsPort, wssPort, # ports                 
                 secure, clientName): # security    
        
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
                                                   secure, clientName) # security


    # update
    def update(self, sparqlUpdate):

        """This method is used to perform a SPARQL update"""
        
        # debug print
        self.logger.debug("Performing a SPARQL update")

        # perform the update request
        status, results = self.connectionManager.updateRequest(sparqlUpdate)                

        # return
        if int(status) == 200:
            jresults = json.loads(results)
            if "updated" in jresults:
                if "status" in jresults["updated"]:
                    return jresults["updated"]["status"], jresults["updated"]["body"]
                else:
                    return False, results
            else:
                return False, results
        else:
            return False, results


    # query
    def query(self, sparqlQuery):

        """This method is used to perform a SPARQL query"""

        # debug print
        self.logger.debug("Performing a SPARQL query")
        
        # perform the query request
        status, results = self.connectionManager.queryRequest(sparqlQuery)

        # return 
        if int(status) == 200:
            jresults = json.loads(results)
            if "error" in jresults:
                return False, jresults["error"]["message"]
            else:
                return True, jresults
        else:
            return False, results
        

    # TODO -- subscribe
    def subscribe(self):
        pass
        
    
    # TODO -- unsubscribe
    def unsubsribe(self):
        pass
