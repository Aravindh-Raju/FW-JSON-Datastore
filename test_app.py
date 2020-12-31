from unittest import TestCase
import app as x

"""

Comment the print statements in the "app.py" file before performing unit test.
Uncomment the raise statements in the "app.py" file before performing unit test.

"""


class TestOperations(TestCase):
    def test_create(self):
        val = 1024 * 1024 * 1024
        self.assertRaises(Exception, x.create, 22, 44, 3)  # Key can't be a number
        self.assertRaises(Exception, x.create, "Sweet", 22, "Age")  # Timeout can't be a string
        self.assertRaises(Exception, x.create, "Chocolates", val, 2)  # Memory limit exceeded
        self.assertEqual(x.create("Sweets", 22, 5), "JSON object created successfully!!")  # Successfully created
        self.assertRaises(Exception, x.create, "Sweets", 25)  # Key already in JSON file
        self.assertEqual(x.create("Cookies", 30, 5), "JSON object created successfully!!")

    def test_read(self):
        self.assertRaises(Exception, x.read, "Pickle")  # Key not in JSON file
        self.assertEqual(x.read("Sweets"), "Sweets : 22")  # Displaying key and value

    def test_delete(self):
        self.assertRaises(Exception, x.delete, "Pickle")  # Key not in JSON file
        self.assertEqual(x.delete("Cookies"), "Key successfully deleted")  # Deleted key and value

    def test_modify(self):
        self.assertRaises(Exception, x.modify, "Pickle")  # Key not in JSON file
