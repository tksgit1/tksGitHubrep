import numpy as np
# import pygame
import sys
import pyglet
import random
import time
import requests
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import torch
# import tensorflow as tf
from rest_framework import serializers
# from .models import Book
# import BookViewSet
import math
import utils
# import GFG
import fileinput
import operator
import mysql.connector
import matplotlib.pyplot as plt
from multiprocessing.connection import Connection
import time, os
from multiprocessing import Pool, freeze_support
import psycopg2

class Calculator:
    K=1

    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result
        K=1

    def run(self):
 #       n=W
        try:
    #        conn = psycopg2.connect(database="college", user='root',
    #                                password='Test@135mac', host='localhost',
    #                                port='3306')
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Test@135mac",
            database="college")


            cursor = conn.cursor()
            print("connection sucessful")
            cursor.execute('''SELECT * FROM employee''')
            print("statement executed")
            records = cursor.fetchall()

    rows = cur.fetchall()

    return records
        except:
            print("Connection not established to the database")
            return -1
    # Create object
#rint("Create object")
#k=1
calc = Calculator()
#k=1
M=1
print(calc.K)
M=calc.K
if M>0:
    M=M+1
print(M)

# Using default arguments
print("A = ", M)
print(calc.multiply())
print("B = ", M)
#print(calc.multiply(4))
print("C = ", M)


# Using multiple arguments
#print(calc.multiply(2, 3))
print("D = ", M)
#print(calc.multiply(2, 3, 4))
print("E = ", M)


if __name__ == "__main__":

#    freeze_support()
#    print("Enter the number of times to run the above query")
#    n = int(input())
#    results = []
    res=""
    results=""
 #   with Pool(processes=os.cpu_count() - 1) as pool:

 #       for _ in range(n):
 #       W=n
 #        print(n)
for i in range(0, 9):
    calc.run()
    results=results+res
    results=results+str(res)
    res = [result.get() for result in results]
#            print("Enter the number of times to run the above query")
#            n = int(input())

print(res)
#    pool.close()
#    pool.join()

