from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os

app = Flask(__name__)

# CORS - update with your actual Vercel URL after deployment
CORS(app, origins=[
    os.environ.get("FRONTEND_URL", "http://localhost:3000"),
    "http://localhost:5173"
])

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_SERVICE_KEY")
)

@app.route('/api/guestbook', methods=['GET'])
def get_guestbook():
    try:
        response = supabase.table('guestbook')\
            .select('*')\
            .order('created_at', desc=True)\
            .execute()
        return jsonify({"success": True, "data": response.data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/guestbook', methods=['POST'])
def post_guestbook():
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('message'):
            return jsonify({"success": False, "error": "Name and message required"}), 400
            
        entry = {
            "name": data['name'].strip()[:40],
            "message": data['message'].strip()[:280]
        }
        
        response = supabase.table('guestbook').insert(entry).execute()
        return jsonify({"success": True, "data": response.data[0]}), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)