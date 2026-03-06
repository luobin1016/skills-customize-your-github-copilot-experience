def load_and_clean_lines(file_path):
    # Read lines from a file, trim whitespace, and skip blank lines.
    pass


def word_frequency_report(lines):
    # Build and return a normalized word-count dictionary from text lines.
    pass


if __name__ == "__main__":
    sample_path = "sample.txt"
    cleaned_lines = load_and_clean_lines(sample_path)
    frequencies = word_frequency_report(cleaned_lines)
    print(frequencies)
