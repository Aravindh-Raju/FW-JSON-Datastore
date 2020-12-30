# Example to run the main file and import the main file as a library.

import app as lib
import time
from threading import *

# Import the main file as a library.

lib.create("Cookies", 75)
lib.create("Chocolates", 25, 2.5)
lib.create("Pizza", 10)
# Creating a key with key name,value and no time-to-live property(optional).
# TTL is a optional property passed as a number denoting seconds.

lib.create("Sweets", 70, 3600)
# Creating a key with key name,value and time-to-live property.

time.sleep(3)  # To check whether TTL property works while reading below.
lib.read("Sweets")
lib.read("Chocolates")
# Returns the value of given key in JSON object format.
# If TTL (time-to-live) property is given and the time is expired it returns an error.

lib.create("Sweets", 50)
# Returns an error since the key already exists.

lib.modify("Chocolates", 55)
# Replaces the initial value of given key with new value.
# Since TTL of the key expired it can't be deleted.

lib.delete("Cookies")
lib.read("Pizza")
# Deletes the given key and its value.

lib.display()
# Displays JSON objects present in the file.

# To use threads. Remove triple quotes to execute.
"""

t1 = Thread(target=x.create, args=("Pickle", 35, 50), daemon=True)
t1.start() 
# Only one thread will be executed since daemon is used. To use other threads we must use join().
t2 = Thread(target=x.read, args="Sweets", daemon=True)
t2.start()
t3 = Thread(target=x.read, args="Chips", daemon=True)
t3.start()

"""
