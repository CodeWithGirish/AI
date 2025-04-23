import re

def analyze_text(text):
    char_count = len(text)
    word_count = len(text.split())
    sentence_count = len(re.findall(r'[.!?]', text))
    line_count = text.count('\n') + 1
    tab_count = text.count('\t')
    number_count = len(re.findall(r'\b\d+\b', text))
    space_count = text.count(' ')

    print("Characters:", char_count)
    print("Words:", word_count)
    print("Sentences:", sentence_count)
    print("Lines:", line_count)
    print("Tabs:", tab_count)
    print("Numbers:", number_count)
    print("Spaces:", space_count)

# Example usage
sample_text = """Hello there! This is a test.
There are 3 lines, 2 numbers: 123 and 456.
Tabs\tare\there.\n"""

analyze_text(sample_text)
