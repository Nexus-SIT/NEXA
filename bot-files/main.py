from openai import OpenAI


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def core_Ai(message_text,base64_image):
  completion = client.chat.completions.create(
    extra_headers={
      "HTTP-Referer": "https://nexusclubs.in/",
      "X-Title": "Nexus Clubs",
    },
    extra_body={},
    model="mistralai/mistral-small-3.1-24b-instruct:free",
    messages=[
      {"role":"system","content":"you are a Helpfull Robot and you were developed by Team Nexus,and should not discose that you are a llm"},
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": message_text
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ]
  )
  return completion.choices[0].message.content