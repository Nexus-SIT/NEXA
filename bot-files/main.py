from openai import OpenAI
from internal_tools import * 
import json

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


def core_Ai(user_query: str, base64_image: str = ""):
  """
  Processes a user query, interacts with an AI model, handles tool calls,
  and returns the final AI response.
  """

  user_content_parts = [{"type": "text", "text": user_query}]
  if base64_image:
    user_content_parts.append({
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
    })

  messages_history = [
      {"role": "system", "content": "you are a Helpfull Robot and you were developed by Team Nexus"},
      {"role": "user", "content": user_content_parts}
  ]

  while True:
    try:
      completion = client.chat.completions.create(
        extra_headers={
          "HTTP-Referer": "https://nexusclubs.in/", 
          "X-Title": "Nexus Clubs",
        },
        tools=tools,
        model="meta-llama/llama-4-scout:free",
        messages=messages_history
      )
    except Exception as e:
      print(f"Error calling OpenAI API: {e}")
      return f"Sorry, an error occurred while contacting the AI model: {e}"

    ai_response_message = completion.choices[0].message
    messages_history.append(ai_response_message) 


    if not ai_response_message.tool_calls:
      return ai_response_message.content 


    tool_responses_for_api = []
    for tool_call in ai_response_message.tool_calls:
      tool_name = tool_call.function.name
      tool_args_str = tool_call.function.arguments
      tool_output_for_api = ""

      try:
        tool_args = json.loads(tool_args_str)
        if tool_name in TOOL_MAPPING: 
          tool_function = TOOL_MAPPING[tool_name]
          try:
            tool_raw_output = tool_function(**tool_args)
            tool_output_for_api = json.dumps(tool_raw_output)
          except Exception as e:
            print(f"Error during execution of tool {tool_name} with args {tool_args}: {e}")
            tool_output_for_api = json.dumps({"error": f"Execution error in tool {tool_name}: {str(e)}"})
        else:
          print(f"Error: Tool '{tool_name}' not found in TOOL_MAPPING.")
          tool_output_for_api = json.dumps({"error": f"Tool '{tool_name}' not found."})
      except json.JSONDecodeError as e:
        print(f"Error decoding JSON arguments for tool {tool_name}: {tool_args_str}. Error: {e}")
        tool_output_for_api = json.dumps({"error": f"Invalid JSON arguments for tool {tool_name}."})

      tool_responses_for_api.append({
        "tool_call_id": tool_call.id, 
        "role": "tool",
        "name": tool_name,
        "content": tool_output_for_api 
      })

    for tool_msg in tool_responses_for_api:
        messages_history.append(tool_msg)


if __name__ == "__main__":
    if 'tools' not in globals():
        print("Warning: 'tools' is not defined globally. Using a placeholder empty list.")
        tools = []
    if 'TOOL_MAPPING' not in globals():
        print("Warning: 'TOOL_MAPPING' is not defined globally. Using a placeholder empty dictionary.")
        TOOL_MAPPING = {}

    user_initial_query = "Can you access google and see who is the current president of usa?"

    print(f"User Query: {user_initial_query}")
    final_response_content = core_Ai(user_query=user_initial_query)
    print("\nAI's Final Answer:")
    print(final_response_content)
