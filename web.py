from flask import request, jsonify

def process_question(question):
    answer = 'this worked'
    files = 'this also worked'  
    return answer, files

@app.route('/test-connection')
def hello():
    return 'ai-search-service is running.'

@app.route('/question', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    try:
        answer, files =  process_question(question) #Replace function with correct function
        return jsonify({'question': question, 'answer': answer, 'filelist': files})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

