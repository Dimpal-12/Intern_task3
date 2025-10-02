# Task 3 Report: AI Chatbot with NLP

## Objective
Build a chatbot using Natural Language Processing libraries (NLTK / spaCy) to answer user queries related to the internship.

## Tools and Libraries
- Python 3
- NLTK (tokenization, stopwords, stemming)
- scikit-learn (TF-IDF + cosine similarity) — optional fallback to keyword matching if not available

## Design
This project uses a knowledge-base (kb.txt) containing FAQ-like sentences. The chatbot preprocesses text (tokenize, remove stopwords, stem), vectorizes using TF-IDF and answers incoming queries by finding the most similar sentence in the KB. If scikit-learn is unavailable, a keyword overlap fallback is used.

## Files
- chatbot.py — main chatbot implementation
- run_chatbot.py — demo runner showing example Q&A
- kb.txt — knowledge base used by the bot
- README.md — instructions for GitHub
- report.pdf — this file in PDF form

## How to run
1. Install dependencies:
   ```bash
   pip install nltk scikit-learn
