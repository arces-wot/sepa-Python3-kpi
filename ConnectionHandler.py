#!/usr/bin/python3

# global requirements
import requests
import logging

# local requirements

# class ConnectionHandler
class ConnectionHandler:

    """This is the ConnectionHandler class"""

    # constructor
    def __init__(self, host, updatePath, queryPath, registrationPath, tokenReqPath, # paths
                 httpPort, httpsPort, wsPort, wssPort, # ports
                 secure): # security

        """Constructor of the ConnectionHandler class"""

        # logger configuration
        logger = logging.getLogger("sepaLogger")

        # store parameters as class attributes
        self.httpPort = str(httpPort)
        self.httpsPort = str(httpsPort)
        self.wsPort = str(wsPort)
        self.wssPort = str(wssPort)
        self.host = host
        self.updatePath = updatePath
        self.queryPath = queryPath
        self.registrationPath = registrationPath
        self.tokenReqPath = tokenReqPath
        self.secure = secure

        # determine complete URIs
        self.queryURI = "http://" + self.host + ":" + self.httpPort + self.queryPath
        self.queryURIsecure = "https://" + self.host + ":" + self.httpsPort + self.queryPath
        self.updateURI = "http://" + self.host + ":" + self.httpPort + self.updatePath
        self.updateURIsecure = "https://" + self.host + ":" + self.httpsPort + self.updatePath


    # do HTTP query request
    def queryRequest(self, sparqlQuery):

        """Method to issue a SPARQL query over HTTP(S)"""
        
        if self.secure:
            pass

        else:

            # define headers and payload
            headers = {"Content-Type":"application/sparql-query", "Accept":"application/json"}
            payload = sparqlQuery

            # perform the request
            r = requests.post(self.queryURI, headers = headers, data = payload)
            return r.text


    # do HTTP update request
    def updateRequest(self, sparqlUpdate):

        """Method to issue a SPARQL update over HTTP(S)"""
        
        if self.secure:
            pass

        else:

            # define headers and payload
            headers = {"Content-Type":"application/sparql-update", "Accept":"application/json"}
            payload = sparqlUpdate

            # perform the request
            r = requests.post(self.queryURI, headers = headers, data = payload)
            return r.text
