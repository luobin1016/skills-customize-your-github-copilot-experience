# 📘 Assignment: Python Text Processing

## 🎯 Objective

Build practical Python skills for processing text data by reading files, cleaning and transforming strings, and generating useful summary output.

## 📝 Tasks

### 🛠️ File Reader and Line Cleaner

#### Description
Create a function named `load_and_clean_lines(file_path)` that opens a text file, reads all lines, removes extra whitespace, and returns only non-empty lines.

#### Requirements
Completed program should:

- Open and read a text file using `with open(...)`.
- Strip leading and trailing whitespace from each line.
- Ignore blank lines after stripping.
- Return a list of cleaned strings.
- Example:
  ```python
  # Input file lines:
  # "  Hello  \n"
  # "\n"
  # "World\n"
  # Return value: ["Hello", "World"]
  ```


### 🛠️ Word Frequency Report

#### Description
Create a function named `word_frequency_report(lines)` that combines cleaned lines into text, normalizes case, removes basic punctuation, and returns a dictionary of word counts.

#### Requirements
Completed program should:

- Join the list of lines into one string.
- Convert text to lowercase.
- Remove punctuation characters such as `. , ! ? : ;`.
- Split text into words and count each word.
- Return a dictionary where keys are words and values are counts.
- Example:
  ```python
  # Input lines: ["Hello world!", "Hello, Python world."]
  # Return value: {"hello": 2, "world": 2, "python": 1}
  ```
