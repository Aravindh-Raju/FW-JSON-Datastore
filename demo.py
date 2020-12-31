# Example to run the main file and import the main file as a library.

import app as lib
import time
from threading import *

# Import the main file as a library.

# Creating a key with key name,value and no time-to-live property(optional).
# TTL is a optional property passed as a number denoting seconds.
lib.create("Cookies", 75)
lib.create("Chocolates", 25, 2.5)
lib.create("Pizza", 10)

# Creating a key with key name,value and time-to-live property.
lib.create("Sweets", 70, 3600)

# Returns the value of given key in JSON object format.
# If TTL (time-to-live) property is given and the time is expired it returns an error.
time.sleep(3)  # To check whether TTL property works while reading below.
lib.read("Sweets")
lib.read("Chocolates")

# Returns an error since the key already exists.
lib.create("Sweets", 50)

# Replaces the initial value of given key with new value.
# Since TTL of the key expired it can't be deleted.
lib.modify("Chocolates", 55)

# Deletes the given key and its value.
lib.delete("Cookies")
lib.read("Pizza")

# Displays JSON objects present in the file.
lib.display()

# To use threads.
t1 = Thread(target=lib.create, args=("Pickle", 35), daemon=True)
t1.start() 
# Only one thread will be executed since daemon is used. To use other threads we must use join().
t2 = Thread(target=lib.read, args="Sweets", daemon=True)
t2.start()
t3 = Thread(target=lib.read, args="Chips", daemon=True)
t3.start()

