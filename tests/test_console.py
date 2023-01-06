#!/usr/bin/python3
"""
this file contains the test class for state creation
"""

import unittest
import MySQLdb

class TestStateCreation(unittest.TestCase):
    def test_create_state(self):
        # Connect to the database
        conn = MySQLdb.connect(
            host='localhost',
            user='username',
            password='password',
            db='database'
        )

        # Create a cursor
        cursor = conn.cursor()

        # Get the initial number of rows in the table
        cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = cursor.fetchone()[0]

        # Execute the create state command (assuming it's a function
        create_state("California")

        # Get the final number of rows in the table
        cursor.execute("SELECT COUNT(*) FROM states")
        final_count = cursor.fetchone()[0]

        # Check that the count has increased by 1
        self.assertEqual(final_count, initial_count + 1)

        # Close the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
	unittest.main()
