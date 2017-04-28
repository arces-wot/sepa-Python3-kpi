#!/usr/bin/python3

# local requirements
import KP
import uuid

idd = str(uuid.uuid4())
print(idd)
k = KP.LowLevelKP("localhost", "/sparql", "/sparql", "/oauth/register", "/oauth/token", 8000, 8443, 9000, 9443, True, idd)
r,s = k.query("SELECT ?s WHERE { ?s ?p ?o }")
print(r)
print(s)
print("================================================") 
r,s = k.update('DELETE DATA { <http://sonoIo#oppureNo> <http://nonLoSo> "xxx" }')
print(r)
print(s)
print("================================================") 
r, s = k.update('DELETE DATA { <http://sonoIo#oppureNo> <http://nonLoSo> "xxx" }')
print(r)
print(s)
print("================================================") 
r,s = k.query("SELECT ?s WHERE { ?s ?p ?o }")
print(r)
print(s)
print("================================================") 
r, s = k.update('DELETE DATA { <http://sonoIo#oppureNo> <http://nonLoSo> "xxx" }')
print(r)
print(s)
