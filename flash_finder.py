import os
import fnmatch
import sqlite3
from datetime import datetime

class FlashFinder:
    def __init__(self, db_path='file_index.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_index_table()

    def create_index_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    path TEXT NOT NULL,
                    last_modified TEXT
                )
            ''')

    def index_directory(self, directory):
        print(f"Indexing directory: {directory}")
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                self.store_file_info(filename, file_path, last_modified)
        print("Indexing completed.")

    def store_file_info(self, name, path, last_modified):
        with self.conn:
            self.conn.execute('''
                INSERT INTO files (name, path, last_modified)
                VALUES (?, ?, ?)
            ''', (name, path, last_modified))

    def search(self, pattern):
        print(f"Searching for: {pattern}")
        with self.conn:
            cursor = self.conn.execute('''
                SELECT name, path, last_modified FROM files
                WHERE name LIKE ?
            ''', (f'%{pattern}%',))
            results = cursor.fetchall()
        return results

    def display_results(self, results):
        if not results:
            print("No files found.")
            return
        print(f"Found {len(results)} file(s):")
        for name, path, last_modified in results:
            print(f"Name: {name}, Path: {path}, Last Modified: {last_modified}")

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    flash_finder = FlashFinder()

    # Example usage:
    # Index a directory
    flash_finder.index_directory('C:\\Your\\Directory\\Path')

    # Search for files with a pattern
    results = flash_finder.search('example')
    flash_finder.display_results(results)

    flash_finder.close()