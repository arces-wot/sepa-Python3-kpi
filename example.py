#!/usr/bin/python3

# local requirements
import KP

k = KP.LowLevelKP("mml.arces.unibo.it", "/sparql", "/sparql", "", "", 8000, 8433, 9000, 9433, False)
k.query("SELECT ?s WHERE { ?s ?p ?o }")
k.update('INSERT DATA { <http://sonoIo#oppureNo> <http://nonLoSo> "xxx" }')
k.query("SELECT ?s WHERE { ?s ?p ?o }")

