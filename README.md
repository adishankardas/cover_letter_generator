# AI Cover Letter Generator

Generate professional, tailored cover letters using Google Gemini AI from the command line.

## Features

- Generates original, formal cover letters based on your input
- Uses Google Gemini API for high-quality content
- Simple command-line interface

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/ai-cover-letter.git
   cd ai-cover-letter
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   Or install manually:
   ```sh
   pip install requests python-dotenv
   ```

3. **Set up your API key:**
   - Copy your Google Gemini API key into a `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the script from the terminal:

```sh
python cover_letter_generator.py
```

You will be prompted for:
- Your Name
- Job Title
- Your Experience
- Company
- Job Description

The script will generate and display a cover letter.

## Example

```
📝 AI Cover Letter Generator

Your Name: Jane Doe
Job Title: Software Engineer
Your Experience: 5 years in backend development
Company: Acme Corp
Job Description: Building scalable APIs and microservices

Generating your cover letter...

------ COVER LETTER ------

[Generated cover letter appears here]
--------------------------
```

## License

MIT License

---

*Powered by Google Gemini AI*
