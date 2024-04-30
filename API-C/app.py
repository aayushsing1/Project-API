from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route('/generate_response', methods=['POST'])
def generate_response():
    content = request.json.get('content')
    
    if not content:
        return jsonify({"error": "Content not provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}],
        )
        generated_response = response.choices[0].message.content

        return jsonify({"response": generated_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
