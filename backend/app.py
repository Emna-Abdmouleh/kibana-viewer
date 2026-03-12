from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

KIBANA_BASE_URL = os.getenv("KIBANA_BASE_URL", "http://127.0.0.1:5601")
ES_URL = os.getenv("ES_URL", "http://localhost:9200")
ES_INDEX = os.getenv("ES_INDEX", "cvs")

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

@app.route("/api/stats", methods=["GET"])
def get_stats():
    try:
        response = requests.get(f"{ES_URL}/{ES_INDEX}/_count")
        data = response.json()
        return jsonify({ "cv_count": data.get("count", 0) })
    except Exception as e:
        return jsonify({ "cv_count": 0, "error": str(e) })

if __name__ == "__main__":
    app.run(debug=True, port=5000)