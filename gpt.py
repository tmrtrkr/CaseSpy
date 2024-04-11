import openai
import threading

   
def send_prompt(Prompt, api):
        openai.api_key = api
        response = openai.chat.completions.create(
        model="gpt-4",  
        messages=[{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": Prompt}],
        temperature=0.7,
        max_tokens=600,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )    
        print("HTTP 200")
        return response.choices[0].message.content