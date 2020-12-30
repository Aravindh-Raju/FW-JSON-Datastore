import time
import json  # This is to save our JSON object in a file.

dictionary = {}  # This is the dictionary to store our data


# To create
def create(key, value, timeout=0):
    if key in dictionary:
        print("Error: Key already exists")
    else:
        if key.isalpha():
            # For file size to be less than 1GB and JSON object value less than 16KB.
            if len(dictionary) < (1024 * 1024 * 1024) and value <= (16 * 1024 * 1024):
                """
                  
                Timeout is optional you can continue by passing two arguments without timeout.
                Timeout denotes the TTL (time-to-live) property of the given key.
                
                """
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                # For input key capped at 32chars.
                if len(key) <= 32:
                    dictionary[key] = l
                print("JSON object created successfully!!")
            else:
                print("Error: Memory limit exceeded")
        else:
            print("Error: Invalid key. Key must contain only alphabets")
    with open('data.txt', 'w+') as outfile:
        json.dump(dictionary, outfile)


# To read
def read(key):
    if key not in dictionary:
        print("Error: Key doesn't exist. Enter a valid key")
    else:
        display = dictionary[key]
        if display[1] != 0:
            # Comparing with expiry time.
            if time.time() < display[1]:
                string = str(key) + " : " + str(display[0])
                # Prints the value in the form of JSON object."
                print(string)
            else:
                print("Error: TTL(time-to-live) of", key, "has expired")
        else:
            string = str(key) + ":" + str(display[0])
            return string
    with open('data.txt', 'w+') as outfile:
        json.dump(dictionary, outfile)


# To delete
def delete(key):
    if key not in dictionary:
        print("Error: Key doesn't exist. Enter a valid key")
    else:
        display = dictionary[key]
        if display[1] != 0:
            # Comparing with expiry time.
            if time.time() < display[1]:
                del dictionary[key]
                print("Key successfully deleted")
            else:
                print("Error: TTL(time-to-live) of", key, "has expired")
        else:
            del dictionary[key]
            print("Key successfully deleted")
    with open('data.txt', 'w+') as outfile:
        json.dump(dictionary, outfile)


# To modify (Additional operation)
def modify(key, value):
    display = dictionary[key]
    if display[1] != 0:
        if time.time() < display[1]:
            if key not in dictionary:
                print("Error: Key doesn't exist. Enter a valid key")
            else:
                new = [value, display[1]]
                dictionary[key] = new
                print("Modified successfully!!")
        else:
            print("Error: TTL(time-to-live) of", key, "has expired")
    else:
        if key not in dictionary:
            print("Error: Key doesn't exist. Enter a valid key")
        else:
            new = [value, display[1]]
            dictionary[key] = new
            print("Modified successfully!!")
    with open('data.txt', 'w+') as outfile:
        json.dump(dictionary, outfile)


# To display (Additional operation)
def display():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        # Printing the JSON objects in the file. 
        printing = json.dumps(data, indent=5)
        print(printing)
