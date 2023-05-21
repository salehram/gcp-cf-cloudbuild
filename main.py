import os
from datetime import datetime
import mysql.connector

def return_basic(request):
  now = datetime.now()
  return 'Welcome to Cloud Functions - ' + now
