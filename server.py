from flask import Flask, request, jsonify
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

app = Flask(__name__)

# Members API Route
@app.route("/testing")
def members():
	return {"members": ["Member1", "Member2", "Member3"]}
	

# Question API Route
qa_model_name = "deepset/roberta-base-squad2"
@app.route("/question", methods=["POST"])
def post_data():
    # Get form data from the request
    data = request.form

    # Assuming the form data has a key named 'data'
    received_question = data.get('question', None)
    received_context = data.get('context', None)

    if received_question is not None:
        qa_nlp = pipeline('question-answering', model=qa_model_name, tokenizer=qa_model_name)
        QA_input = { 'question': received_question,'context': received_context}
        res = qa_nlp(QA_input)
        result = {"message": res}
        return jsonify(result)
    else:
        return jsonify({"error": "No Question received"}), 400


# Summary API Route
@app.route("/summary", methods=["POST"])
def post_summary_data():
    # Get form data from the request
    data = request.form
    # Assuming the form data has a key named 'data'
    received_data = data.get('data', None)
    if received_data is not None:
        summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        res = summarizer(received_data, max_length=230, min_length=30, do_sample=False)
        result = {"message": res}
        return jsonify(result)
    else:
        return jsonify({"error": "No Data received"}), 400

if __name__ == "__main__": 
	app.run(debug=True)