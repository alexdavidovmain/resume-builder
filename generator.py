from groq import Groq
import json

import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def generate_resume(data):
    prompt = f"""
You are a professional resume writer. Based on the following user data, write a clean, professional resume summary and enhance their job descriptions and skills.

User Data:
{json.dumps(data, indent=2)}

Respond ONLY with a JSON object in this exact format, no extra text, no markdown:
{{
  "summary": "2-3 sentence professional summary",
  "enhanced_experience": [
    {{
      "title": "job title",
      "company": "company name",
      "duration": "duration",
      "bullets": ["bullet 1", "bullet 2", "bullet 3"]
    }}
  ],
  "enhanced_skills": ["skill1", "skill2", "skill3"],
  "enhanced_education": [
    {{
      "degree": "degree name",
      "school": "school name",
      "year": "graduation year"
    }}
  ]
}}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    text = response.choices[0].message.content
    clean = text.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)