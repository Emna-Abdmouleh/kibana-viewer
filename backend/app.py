from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

KIBANA_BASE_URL = os.getenv("KIBANA_BASE_URL", "http://127.0.0.1:5601")

@app.route("/api/dashboards", methods=["GET"])
def get_dashboards():
    dashboards = [
        {
            "id": "1",
            "title": "Dashboard CVS",
            "url": f"{KIBANA_BASE_URL}/app/dashboards#/view/{os.getenv('DASHBOARD_ID_1')}?embed=true&hide-filter-bar=true"
        }
    ]
    return jsonify(dashboards)

if __name__ == "__main__":
    app.run(debug=True, port=5000)