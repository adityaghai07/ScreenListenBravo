import os
from openai import OpenAI
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))  


def is_tech_company(description: str) -> bool:

    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that determines if a company is a technology company based on its description."},
            {"role": "user", "content": f"Is the following company a technology company? Respond with only 'Yes' or 'No'.\n\nCompany description: {description}"}
        ]
    )
    return response.choices[0].message.content.strip().lower() == "yes"




#Example Usage 1

# if __name__ == "__main__":
#     print(is_tech_company("We are a software company that specializes in creating productivity tools for businesses.")) # True
    