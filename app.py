from flask import Flask, jsonify, request
from email_fetcher import fetch_emails
from nlp_utils import analyze_sentiment, detect_urgency
from response_generator import generate_response
from info_extractor import extract_info
from db_handler import save_email, get_all_emails, mark_email_resolved

app = Flask(__name__)

# Route to fetch and process emails
@app.route("/emails", methods=["GET"])
def get_emails():
    raw_emails = fetch_emails()  # You can pass credentials via env vars
    processed = []

    for email in raw_emails:
        sentiment = analyze_sentiment(email["body"])
        urgency = detect_urgency(email["body"])
        info = extract_info(email["body"])
        response = generate_response({
            **email,
            "sentiment": sentiment,
            "urgency": urgency
        })

        email_record = {
            **email,
            "sentiment": sentiment,
            "urgency": urgency,
            "info": info,
            "response": response,
            "status": "pending"
        }

        save_email(email_record)
        processed.append(email_record)

    return jsonify(processed)

# Route to get all stored emails
@app.route("/stored-emails", methods=["GET"])
def get_stored_emails():
    emails = get_all_emails()
    return jsonify(emails)

# Route to mark an email as resolved
@app.route("/resolve", methods=["POST"])
def resolve_email():
    email_id = request.json.get("email_id")
    mark_email_resolved(email_id)
    return jsonify({"message": "Email marked as resolved"})

# Route to get analytics
@app.route("/analytics", methods=["GET"])
def get_analytics():
    emails = get_all_emails()
    total = len(emails)
    resolved = sum(1 for e in emails if e["status"] == "resolved")
    pending = total - resolved

    sentiment_count = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
    for e in emails:
        sentiment_count[e["sentiment"]] += 1

    return jsonify({
        "total": total,
        "resolved": resolved,
        "pending": pending,
        "sentiment": sentiment_count
    })

if __name__ == "__main__":
    app.run(debug=True)
