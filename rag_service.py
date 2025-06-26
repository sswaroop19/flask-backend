class RAGService:
    def process_pdf(self, conversation_id, file):
        print(f"Processing {file.filename} for conversation {conversation_id}")

    def get_answer(self, conversation_id, question):
        return {"answer": f"You asked: {question}"}
