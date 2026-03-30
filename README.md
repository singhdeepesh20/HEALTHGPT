<div align="center">

# 🩺 HealthGPT — AI-Powered Medical Assistant

### Accessible, Intelligent, and Scalable Healthcare Support System

</div>

---

## Overview

**HealthGPT** is a Generative AI-powered medical assistant designed to provide **instant, accessible, and reliable health-related information** while supporting hospitals in **streamlining triage and patient communication**.

Built using modern **LLM + RAG architectures**, HealthGPT focuses on delivering **clear, context-aware, and easy-to-understand medical insights** for both patients and healthcare providers.

---

## Key Features

* 🌍 **Multilingual Support** → Inclusive access across diverse populations
* 💬 **AI-Powered Medical Q&A** → Understand diseases, symptoms, and prescriptions in simple language
* ⚠️ **Non-Diagnostic Guidance** → Provides general health suggestions (not medical diagnosis)
* 🏥 **Hospital Support** → Pre-consultation triage and FAQ automation
* 📊 **Patient Interaction Summary** → Structured insights before doctor consultation
* 🖥️ **User-Friendly Interface** → Built with Streamlit for simplicity and accessibility

---

## System Architecture

```
User Query → Streamlit UI → LangChain Agent
        ↓
 Retrieval (FAISS + Embeddings)
        ↓
   LLM (Groq / HuggingFace)
        ↓
   Contextual Response
```

---

## Tech Stack

| Layer           | Technologies                   |
| --------------- | ------------------------------ |
| 💬 LLM & Agents | Groq / HuggingFace + LangChain |
| 🔍 Embeddings   | HuggingFace Embeddings + FAISS |
| 📄 Retrieval    | RAG-based pipelines            |
| 🌐 Frontend     | Streamlit                      |
| 🏥 Data         | Public medical datasets        |

---

## Real-World Applications

### 🔹 For Patients

* 24/7 access to health-related information
* Simplified explanations of complex medical terms
* Improved health awareness and literacy
* Accessible support for rural and underserved areas

### 🔹 For Hospitals

* Automated triage and patient query handling
* Reduced front desk workload
* Pre-consultation symptom collection
* Structured summaries for doctors

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/HealthGPT.git
cd HealthGPT
```

### 2. Create Virtual Environment

```bash
conda create -n healthgpt python=3.10 -y
conda activate healthgpt
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## Engineering Approach

### Retrieval-Augmented Generation (RAG)

Ensures responses are:

* Context-aware
* Grounded in reliable data
* More accurate than standalone LLM outputs

### Agent-Based Design

* Dynamic query handling
* Tool integration for better reasoning

### Scalable System Design

* Modular architecture
* Easily extendable with new datasets and models

---

## What This Project Demonstrates

* End-to-end LLM application development
* Implementation of RAG pipelines in healthcare
* Integration of embeddings + vector databases
* Real-world AI system for patient interaction
* Strong focus on usability and impact

---

## Important Disclaimer

⚠️ HealthGPT is **not a substitute for professional medical advice, diagnosis, or treatment**.
Always consult a qualified healthcare provider for medical concerns.

---

## Vision

HealthGPT aims to bridge the gap between **patients and accessible healthcare information**:

* Democratizing medical knowledge
* Supporting healthcare systems with AI
* Enabling faster and more informed decisions

Long-term, it can evolve into a **scalable AI healthcare assistant integrated across hospitals, telemedicine platforms, and public health systems**.

---

<div align="center">

### "AI for accessible and intelligent healthcare."

<

