## Interview Transcript Analysis w/ Flesch-Kincaid Grade Level

This Python script, `assess_grade.py`, offers a simple and effective way to analyze qualitative interview transcripts and calculate the Flesch-Kincaid grade level for each participant's responses. It's ideal for researchers, linguists, and educators interested in readability and qualitative data analysis.

## Features

- **Transcript Parsing**: Reads `.docx` files containing interview transcripts and extracts the text.
- **Speaker Identification**: Separates the transcript into different sections based on speaker.
- **Readability Analysis**: Calculates the Flesch-Kincaid grade level for each speaker's contributions.

## Requirements

- Python 3.x
- `python-docx`: For reading `.docx` files.
- `textstat`: For calculating the Flesch-Kincaid Grade Level.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/TLDWTutorials/FleschKincaidPython/
```
Install the required packages:

```bash
pip install python-docx textstat
```
## Usage

(1) Place your .docx interview transcript files in the same directory as the script.

(2) Run the script:

```bash
python assess_grade.py
```

(3) The script will process each file and output the Flesch-Kincaid grade level for each speaker.

## Contributing
Contributions, issues, and feature requests are welcome! 

## License
Distributed under the MIT License. 

## Contact
Email - TLDW_Tutorials@protonmail.com

