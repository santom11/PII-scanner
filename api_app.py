from flask import Flask, request, jsonify, send_file
from core.analyzer import TextAnalyzer
from core.anonymizer import TextAnonymizer
from core.writer_html import write_html_report
import os
from core.logger import logger


app = Flask(__name__)
analyzer = TextAnalyzer()
anonymizer = TextAnonymizer()

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    text = data.get("text", "")
    results = analyzer.analyze(text)
    anonymized = anonymizer.anonymize(text, results)
    report_path = write_html_report(text, anonymized, results)
    logger.info(f"Generated report: {report_path}")
    return jsonify({
        "original_text": text,
        "anonymized_text": anonymized,
        "detected_entities": [r.to_dict() for r in results],
        "report_url": f"/report/{os.path.basename(report_path)}"
    })

@app.route("/report/<filename>")
def report(filename):
    # Serve the raw HTML file from the output/ directory
    path = os.path.join("output", filename)
    if not os.path.isfile(path):
        return "Report not found", 404
    return send_file(path, mimetype="text/html")

if __name__ == "__main__":
    app.run(debug=True)