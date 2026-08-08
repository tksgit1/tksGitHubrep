import numpy as np
#import pygame
import sys
import pyglet
import random
import time
import requests
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import torch
#import tensorflow as tf
from rest_framework import serializers
#from .models import Book
#import BookViewSet
import math
import utils
#import GFG
import fileinput
import operator
import mysql.connector
import matplotlib.pyplot as plt
from multiprocessing.connection import Connection
import time,os
from multiprocessing import Pool, freeze_support
import psycopg2


class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())
print(calc.multiply(4))

# Using multiple arguments
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))


