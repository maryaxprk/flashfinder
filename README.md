# FlashFinder

FlashFinder is a Python-based tool designed to facilitate rapid file searching and indexing on Windows systems for quicker data retrieval. This program can index files in specified directories and allows users to perform searches across the indexed data to quickly locate files.

## Features

- Indexes files within a specified directory, storing their names, paths, and last modified dates in an SQLite database.
- Supports pattern-based searching to quickly find files based on partial names.
- Displays search results with file names, full paths, and last modified timestamps.

## Installation

1. Clone or download the repository.
2. Ensure you have Python 3.x installed on your system.
3. Install required Python packages (if any).

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `flash_finder.py`.
3. Run the program using Python:

   ```bash
   python flash_finder.py
   ```

4. To index a directory, modify the `index_directory` method call in the `__main__` section with your desired path:

   ```python
   # Index a directory
   flash_finder.index_directory('C:\\Your\\Directory\\Path')
   ```

5. Search for files using a pattern by modifying the `search` method call:

   ```python
   # Search for files with a pattern
   results = flash_finder.search('example')
   ```

6. View the search results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.