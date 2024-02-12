#Project Module 5
"""Project 5 integrates Python and SQL, focusing on database interactions using SQLite."""

# Import dependencies
import csv
import pathlib
from pathlib import Path
import sqlite3
import uuid
import pandas as pd
import pyarrow
from io import StringIO
import requests
import logging
import Sean_StClair_utils
import seanstclairprojsetup

#Logging
# Configure logging to write to a file, appending new logs to the existing file

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

# Define the database file in the current root project directory

db_file = pathlib.Path("project.db")

#Database creation and schema design with integration

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL script from a file."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        print(f"Error executing {sql_file}: {e}")

#Main functions

def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    db_filepath = 'project.db'

    base_path = pathlib.Path()  # Gets the current directory path

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'create_tables.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'insert_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'update_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'delete_records.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_filter.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_sorting.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_group_by.sql')
    execute_sql_from_file(db_filepath, base_path / 'sql' / 'query_join.sql')


    logging.info("All SQL operations completed successfully")


if __name__ == "__main__":
    main()