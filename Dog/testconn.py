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



def run():
    try:
#        conn = psycopg2.connect(database="college", user='root',
#                                password='Test@135mac', host='localhost',
#                                port='3306')
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Test@135mac",
        database="college"
    )



        cursor = conn.cursor()
        print("connection sucessful")
        cursor.execute('''SELECT *
                          FROM employee''')
        print("statement executed")
        records = cursor.fetchall()
        return records
    except:
        print("Connection not established to the database")
        return -1


if __name__ == "__main__":

#    freeze_support()
    print("Enter the number of times to run the above query")
    n = int(input())
    results = []

    with Pool(processes=os.cpu_count() - 1) as pool:

        for _ in range(n):

            res = pool.apply_async(run)
            results.append(res)
            res = [result.get() for result in results]



    print(res)
    pool.close()
    pool.join()

