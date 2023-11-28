# Import necessary libraries
import os
import re
from docx import Document  # For reading .docx files
import textstat  # For calculating the Flesch-Kincaid Grade Level

# Function to read a .docx file and return its content as a string
def read_docx(file_path):
    doc = Document(file_path)  # Load the document
    # Join all paragraphs in the document into a single string, separated by newlines
    return "\n".join([p.text for p in doc.paragraphs])

# Function to separate the text into sections based on different speakers
def separate_interview_sections(text):
    sections = {}  # Dictionary to store sections keyed by speaker name
    current_speaker = None  # Variable to track the current speaker

    # Regex pattern to identify speaker names followed by a colon
    speaker_pattern = re.compile(r'\[?\d*:?[\d{2}]*\]?\s*(.+?):')

    # Process each line in the text
    for line in text.split('\n'):
        speaker_match = speaker_pattern.match(line)
        if speaker_match:
            # If a new speaker is found, update the current speaker
            current_speaker = speaker_match.group(1).strip()
            # Remove the speaker name from the line and add the rest to the section
            speech = speaker_pattern.sub('', line).strip()
            sections[current_speaker] = sections.get(current_speaker, '') + speech + ' '
        elif current_speaker:
            # If the line belongs to the current speaker, add it to their section
            sections[current_speaker] += line.strip() + ' '

    return sections

# Get a list of all .docx files in the current directory
docx_files = sorted([file for file in os.listdir('.') if file.endswith('.docx')])

# Process each file
for file in docx_files:
    file_content = read_docx(file)  # Read the content of the file
    interview_sections = separate_interview_sections(file_content)  # Separate content by speaker

    print(f"Processing file: {file}")
    # Calculate and print the Flesch-Kincaid Grade Level for each speaker
    for speaker, text in interview_sections.items():
        fk_score = textstat.flesch_kincaid_grade(text)
        print(f"{speaker}: Flesch-Kincaid Grade Level = {fk_score}")
    print("\n")
