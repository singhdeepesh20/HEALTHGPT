# 🩺 HealthGPT – Your AI-Powered Medical Assistant

**HealthGPT** is a Generative AI-based medical chatbot designed to provide instant, accessible, and reliable health-related assistance to patients while supporting hospitals in streamlining basic triage and patient communication.

---

## 🚀 Features

✅ Multilingual support for inclusive healthcare access  
✅ Explains diseases, prescriptions, symptoms in simple terms  
✅ Provides general health suggestions (non-diagnostic)  
✅ Supports hospitals with pre-consultation triage and FAQs   
✅ Easy-to-use UI built with Streamlit  

---

## 🧠 Tech Stack

| Layer        | Technologies                          |
|--------------|----------------------------------------|
| 💬 LLM & Agents  | Groq / HuggingFace + LangChain agents |
| 🔍 Embeddings   | HuggingFaceEmbeddings / FAISS         |
| 📄 Retrieval    | RAG-based document chains             |
| 🌐 Frontend     | Streamlit                            |
| 🏥 Datasets     | Public medical knowledge bases        |

---

## 🏥 Real-World Applications

### 🔹 For Patients
- Empowers patients with 24/7 health information access  
- Promotes health literacy using plain-language explanations  
- Bridges healthcare gaps in rural and underserved areas
- Easy to use and easy to understand 

### 🔹 For Hospitals
- Reduces front desk workload with AI-powered triage  
- Automates repetitive health queries  
- Collects basic symptoms before doctor consultation
- They have summary of all the patient report 

---
How to Run

1. **Clone the repository**

git clone https://github.com/yourusername/HealthGPT.git
cd HealthGPT
Create a virtual environment and activate it

2. **Create a virtual environment and activate it


conda create -n healthgpt python=3.10 -y
conda activate healthgpt
Install dependencies

3. **Install dependencies

pip install -r requirements.txt
Run the Streamlit app

4. **Run the Streamlit app

streamlit run app.py



