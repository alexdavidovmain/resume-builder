from flask import Flask, render_template, request, jsonify, send_file
from generator import generate_resume
import json
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    try:
        result = generate_resume(data)
        full = {**data, **result}
        return jsonify({"success": True, "resume": full})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/export', methods=['POST'])
def export():
    data = request.get_json()
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.json', mode='w')
    json.dump(data, tmp, indent=2)
    tmp.close()
    return send_file(tmp.name, as_attachment=True, download_name='resume.json', mimetype='application/json')

if __name__ == '__main__':
    import os
app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))