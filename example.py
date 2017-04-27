#!/usr/bin/python3

# local requirements
import KP

k = KP.LowLevelKP("mml.arces.unibo.it", "/sparql", "/sparql", "", "", 8000, 8433, 9000, 9433, False)
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
# r,s = k.query("asdfSELECT ?s WHERE { ?s ?p ?o }")
# print(r)
# print(s)
r, s = k.update('DELET DATA { <http://sonoIo#oppureNo> <http://nonLoSo> "xxx" }')
print(r)
print(s)
