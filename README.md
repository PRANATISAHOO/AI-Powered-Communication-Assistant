# AI-Powered-Communication-Assistant
# 🤖 AI-Powered Communication Assistant

An intelligent assistant that automates the end-to-end handling of support emails—filtering, prioritizing, responding, and analyzing—all with empathy and speed.

---

## 🚀 Overview

Modern organizations receive hundreds of support-related emails daily. Manually managing these is time-consuming and error-prone. This assistant uses AI to:

- Automatically retrieve and filter support emails
- Detect sentiment and urgency
- Generate context-aware responses using GPT-4
- Extract key information for faster resolution
- Display everything on a clean, interactive dashboard

---

## 🧠 Features

- 📥 **Email Retrieval**: Connects to Gmail/IMAP to fetch incoming emails
- 🧪 **Sentiment & Urgency Detection**: Classifies tone and priority using NLP
- ✍️ **Auto-Responses**: Uses GPT-4 + RAG to generate empathetic replies
- 🔍 **Information Extraction**: Pulls contact info, product names, and requests
- 📊 **Dashboard & Analytics**: View emails, responses, and performance stats
- ✅ **Mark as Resolved**: Update status and track resolution progress

---

## 🛠️ Tech Stack

| Layer        | Tools Used                                      |
|--------------|--------------------------------------------------|
| Backend      | Python, Flask, OpenAI API, Hugging Face, FAISS  |
| Frontend     | React.js, Material UI, Chart.js                 |
| Database     | MongoDB                                         |
| NLP Models   | DistilBERT, SentenceTransformer, GPT-4          |

---

## ⚙️ Setup Instructions

### 🔧 Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
