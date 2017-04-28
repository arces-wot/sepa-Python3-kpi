#!/usr/bin/python3

# global requirements
import requests
import logging
import base64
import json
import sys

# local requirements

# class ConnectionHandler
class ConnectionHandler:

    """This is the ConnectionHandler class"""

    # constructor
    def __init__(self, host, updatePath, queryPath, registrationPath, tokenReqPath, # paths
                 httpPort, httpsPort, wsPort, wssPort, # ports
                 secure, clientName): # security

        """Constructor of the ConnectionHandler class"""

        # logger configuration
        self.logger = logging.getLogger("sepaLogger")

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
        self.clientName = clientName

        # determine complete URIs
        self.queryURI = "http://" + self.host + ":" + self.httpPort + self.queryPath
        self.queryURIsecure = "https://" + self.host + ":" + self.httpsPort + self.queryPath
        self.updateURI = "http://" + self.host + ":" + self.httpPort + self.updatePath
        self.updateURIsecure = "https://" + self.host + ":" + self.httpsPort + self.updatePath
        self.registerURI = "https://" + self.host + ":" + self.httpsPort + self.registrationPath
        print self.registerURI
        self.tokenReqURI = "https://" + self.host + ":" + self.httpsPort + self.tokenReqPath

        # security data
        self.token = None
        self.clientSecret = None


    # do HTTP request
    def request(self, sparql, isQuery):

        """Method to issue a SPARQL request over HTTP(S)"""
        
        # if security is needed
        if self.secure:

            # initialization
            needRefresh = False

            # if the client is not yet registered, then register!
            if not self.clientSecret:
                if not(self.register()):
                    return False, "Registration failed!"
                    
            # if a token is not present, request it!
            if not(self.token):
                if not(self.requestToken()):
                    return False, "Token not obtained!"

            # perform the request
            self.logger.debug("Performing a secure SPARQL request")
            if isQuery:
                headers = {"Content-Type":"application/sparql-query", 
                           "Accept":"application/json",
                           "Authorization":self.token}
                r = requests.post(self.queryURIsecure, headers = headers, data = sparql, verify = False)
            else:
                headers = {"Content-Type":"application/sparql-update", 
                           "Accept":"application/json",
                           "Authorization":self.token}
                r = requests.post(self.updateURIsecure, headers = headers, data = sparql, verify = False)

                # check for errors on token validity
                if r.status_code == 401:
                    self.token = None                
                    return False, "Token expired"

            # return
            return r.status_code, r.text

        # insecure connection 
        else:

            # perform the request
            self.logger.debug("Performing a non-secure SPARQL request")
            if isQuery:
                headers = {"Content-Type":"application/sparql-query", "Accept":"application/json"}
                r = requests.post(self.queryURI, headers = headers, data = sparql)
            else:
                headers = {"Content-Type":"application/sparql-update", "Accept":"application/json"}
                r = requests.post(self.updateURI, headers = headers, data = sparql)
            return r.status_code, r.text


    # do register
    def register(self):

        # debug print
        self.logger.debug("Registering client " + self.clientName)
        
        # define headers and payload
        headers = {"Content-Type":"application/json", "Accept":"application/json"}
        payload = '{"client_identity":' + self.clientName + ', "grant_types":["client_credentials"]}'

        # perform the request
        r = requests.post(self.registerURI, headers = headers, data = payload, verify = False)        
        if r.status_code == 201:
            jresponse = json.loads(r.text)
            self.clientSecret = "Basic " + base64.b64encode(jresponse["client_id"] + ":" + jresponse["client_secret"])
            return True            
        else:
            return False


    # do request token
    def requestToken(self):

        # debug print
        self.logger.debug("Requesting token")
        
        # define headers and payload        
        headers = {"Content-Type":"application/x-www-form-urlencoded", 
                   "Accept":"application/json",
                   "Authorization": self.clientSecret}    

        # perform the request
        r = requests.post(self.tokenReqURI, headers = headers, verify = False)        
        if r.status_code == 201:
            jresponse = json.loads(r.text)
            self.token = "Bearer " + jresponse["access_token"]
            return True
        else:
            return False
