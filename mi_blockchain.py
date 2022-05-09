#MI primera blockchain con python
#Autor : Paul Vasquez

#Importaciones necesarias 
import datetime
import hashlib
import json  # cuadamos los datos en la cadena de BlockSequenceStartToken

from flask import Flask, jsonify

class Blockchain:

    #constructor 
    def __init__(self) : 
        self.chain = [] #guarda cadena de blocques
        self.create_block(proof=1,previous_hash='0') #creamos un primer bloque 

    #Adadir bloque sfuturos en la cadena 

    def create_block(self, proof, previous_hash) :
#diccionario
        block = {'index':len(self.chain)+1,
                  'timestamp': str(datetime.datetime.now()),
                  'proof': proof, 
                  'previous_hash': previous_hash}
        self.chain.append(block)
        return block           

#funcion para imprimir el ultimo
#  bloque de la cadena 

def print_previous_block(self):
    return self.chain[-1]

