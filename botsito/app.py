from flask import Flask, request, jsonify
from flask_cors import CORS
import main  # Asegúrate de que 'main.py' esté en el mismo directorio    
 

app = Flask(__name__)
CORS(app)

@app.route('/get_response', methods=['POST'])
def api_get_response():
    user_input = request.json['user_input']
    response = main.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

# python -m venv myenv
# .\myenv\Scripts\activate  
# cd botsito
# pip install Flask-CORS
# python app.py





