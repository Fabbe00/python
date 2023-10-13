import os
import sqlite3
from sqlite3 import Error

def main():
    print("Hej")
    add_bil_to_table()

    list_bil_table()

def list_bil_table():
    sqliteConnection = sqlite3.connect("bilar.db")
    cursor = sqliteConnection.cursor()

    sqlite_select_query = """SELECT * from bilar ORDER BY fabrikat"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    for row in records:
        print(f"ID: {row[0]}, \tFABRIKAT: {row[1]}, \tCOLOR: {row[2]}")

    cursor.close()
    sqliteConnection.close()

def add_bil_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    fabrikat = input("Mata in bil fabrikat: ")
    color = input("Mata in color: ")

    sqliteConnection = sqlite3.connect('bilar.db')
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""INSERT INTO bilar
                        (fabrikat, color)
                         VALUES
                        ('{fabrikat}', '{color}')"""
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Closed")

    cursor.close()

    sqliteConnection.close()

main()