from aisearch.main import perform_ai_search


@app.route('/test-connection')
def hello():
    return 'ai-search-service is running.'


@app.route('/question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    result_limit = data.get('result_limit', 5)

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        answer, sources, query = perform_ai_search(
            question=question, result_limit=result_limit
        )
        return jsonify(
            {'question': question, 'query': query, 'answer': answer, 'sources': sources}
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500
