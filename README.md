# CODTECH Internship — Task 3: AI Chatbot with NLP

This repository contains the solution for **Task-3 of the CODTECH Internship**:  
👉 Building an **AI Chatbot with Natural Language Processing (NLP)** using Python.

---

## 📌 Project Overview
The chatbot is built using:
- **NLTK** for text preprocessing (tokenization, stopwords, stemming).
- **scikit-learn** (TF-IDF + cosine similarity) for query matching.
- A **knowledge base (kb.txt)** with internship-related FAQs.
- Fallback to simple keyword matching if scikit-learn is not available.

The bot answers user queries such as internship details, submission guidelines, tools, deliverables, and certification info.

---

## 📂 Repository Contents
- `chatbot.py` — Main chatbot implementation.  
- `run_chatbot.py` — Demo runner that shows sample Q&A.  
- `kb.txt` — Knowledge base (FAQ text file).  
- `report.md` — Detailed project report.  
- `README.md` — This file (instructions & documentation).  
- `requirements.txt` — Python dependencies.  

---

## 🚀 How to Run

### 1️⃣ Setup Environment
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

2️⃣ Run Demo

python run_chatbot.py

3️⃣ Interactive Chat Mode

python chatbot.py --kb kb.txt


---

📋 Example Demo Output

You: What libraries should I use?
Bot: Use NLTK for tokenization, stopwords and simple preprocessing. Optionally use scikit-learn TfidfVectorizer for similarity.

You: Will I get a certificate?
Bot: This internship provides a completion certificate on your internship end date.


---

🛠 Requirements

Python 3.8+

nltk

scikit-learn (optional but recommended)


Install dependencies:

pip install nltk scikit-learn


---

📜 Report

The report (report.md / report.pdf) contains:

Objective

Tools & Libraries used

System Design

How to run the project

Sample output

Improvements & Conclusion

