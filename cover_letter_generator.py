import requests
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
GENAI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def generate_cover_letter(name, job_title, experience, company, job_desc, today):
    prompt = f"""
    Write a professional cover letter for the following:
    
    Name: {name}
    Applying for: {job_title}
    Experience: {experience}
    Target Company: {company}
    Job Description: {job_desc}
    Date: {today}
    The cover letter should highlight the applicant's relevant skills and experiences, align with the job description, and express enthusiasm for the position and the company.
    
    The letter should be formal, convincing, and 100% original.
    """

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(f"{GENAI_URL}?key={API_KEY}", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Error: {response.status_code}\n{response.text}"

# CLI Input
if __name__ == "__main__":
    print("📝 AI Cover Letter Generator\n")

    name = input("Your Name: ")
    job_title = input("Job Title: ")
    experience = input("Your Experience: ")
    company = input("Company: ")
    job_desc = input("Job Description: ")   
    today = date.today().strftime("%B %d, %Y")
    print("\nGenerating your cover letter...\n")
    letter = generate_cover_letter(name, job_title, experience, company, job_desc, today)

    print("------ COVER LETTER ------\n")
    print(letter)
    print("--------------------------")
# End of cover_letter_generator.py