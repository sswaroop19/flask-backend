from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from rag_service import RAGService

app = Flask(__name__)
CORS(app)
rag_service = RAGService()

@app.route('/api/conversations', methods=['POST'])
def create_conversation():
    conversation_id = str(uuid.uuid4())
    return jsonify({'conversation_id': conversation_id})

@app.route('/api/conversations/<conversation_id>/upload', methods=['POST'])
def upload_pdf(conversation_id):
    file = request.files.get('file')
    if not file or not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files allowed'}), 400
    rag_service.process_pdf(conversation_id, file)
    return jsonify({'message': 'PDF uploaded'})

@app.route('/api/conversations/<conversation_id>/chat', methods=['POST'])
def chat(conversation_id):
    data = request.get_json()
    question = data.get('question')
    result = rag_service.get_answer(conversation_id, question)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
