from context_retriever import retrieve_context
def generate_response(email_data):
    query = email_data['body']
    context = retrieve_context(query)

    prompt = f"""
You are a professional support assistant. Respond to the following email in a friendly, empathetic tone.

Email:
Subject: {email_data['subject']}
Body: {email_data['body']}

Context from knowledge base: {context}

Sentiment: {email_data['sentiment']}
Urgency: {email_data['urgency']}

Response:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
