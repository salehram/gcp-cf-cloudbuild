import os
from datetime import datetime
import mysql.connector

def return_basic(request):
  now = datetime.now()
  return '<h1>Welcome to Cloud Functions and Cloud Build demo</h1><br/>' + str(now)
