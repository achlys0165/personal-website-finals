from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import os
from datetime import datetime

app = Flask(__name__)

# CORS - update with your Vercel domain
CORS(app, origins=[
    "https://your-vercel-domain.vercel.app",
    "http://localhost:3000",
    "http://localhost:5173"
])

# Supabase
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# ============ GUESTBOOK ============

@app.route('/api/guestbook', methods=['GET'])
def get_guestbook():
    """Get all guestbook entries, newest first"""
    try:
        response = supabase.table('guestbook')\
            .select('id,name,message,created_at')\
            .order('created_at', desc=True)\
            .execute()
        return jsonify({"success": True, "data": response.data}), 200
    except Exception as e:
        print(f"Error fetching guestbook: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/guestbook', methods=['POST'])
def post_guestbook():
    """Create new guestbook entry"""
    try:
        data = request.get_json()
        
        # Validation
        name = data.get('name', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not message:
            return jsonify({"success": False, "error": "Name and message required"}), 400
        
        if len(name) > 40 or len(message) > 280:
            return jsonify({"success": False, "error": "Field too long"}), 400
        
        entry = {
            "name": name,
            "message": message
        }
        
        response = supabase.table('guestbook').insert(entry).execute()
        
        if response.data:
            return jsonify({"success": True, "data": response.data[0]}), 201
        else:
            return jsonify({"success": False, "error": "Insert failed"}), 500
            
    except Exception as e:
        print(f"Error posting guestbook: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# ============ CONTACT ============

@app.route('/api/contact', methods=['POST'])
def post_contact():
    """Create new contact message"""
    try:
        data = request.get_json()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email:
            return jsonify({"success": False, "error": "Name and email required"}), 400
        
        if '@' not in email:
            return jsonify({"success": False, "error": "Invalid email"}), 400
        
        contact_data = {
            "name": name,
            "email": email,
            "message": message
        }
        
        response = supabase.table('contacts').insert(contact_data).execute()
        
        if response.data:
            return jsonify({"success": True, "data": response.data[0]}), 201
        else:
            return jsonify({"success": False, "error": "Insert failed"}), 500
            
    except Exception as e:
        print(f"Error posting contact: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# ============ HEALTH ============

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "supabase_connected": bool(supabase_url and supabase_key)
    }), 200

if __name__ == '__main__':
    app.run(debug=True)