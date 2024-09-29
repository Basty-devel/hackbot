# file: app.py
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API key
openai.api_key = 'your_openai_api_key'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    # Send the user's message to OpenAI GPT API
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"{user_message}\n\n",
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the response text
    bot_response = response.choices[0].text.strip()

    # Send response back to the frontend
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
