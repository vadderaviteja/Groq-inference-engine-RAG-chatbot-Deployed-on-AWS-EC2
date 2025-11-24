# 🚀 Groq-inference-engine-RAG-chatbot-Deployed-on-AWS-EC2

This project is a **Retrieval-Augmented Generation (RAG) based AI Chatbot** powered by the **Groq Inference Engine** for extremely fast LLM responses.  
The backend is built using **Python**, **LangChain**, and **Groq API**, and the app is deployed on an **AWS EC2 Ubuntu Server** using Streamlit.

---

## 📌 Features
- ⚡ Ultra-fast responses using **Groq LLaMA / Mixtral models**
- 🔎 RAG Pipeline using **vector embeddings** + **FAISS**
- 🧠 Context-aware conversational memory
- 🌐 Public deployment using AWS EC2 (Ubuntu)
- 📦 Streamlit-based UI for the chatbot

---

# 🏗️ Project Structure
-app.py
-requiremets.txt


# 🔑 Requirements
- Python 3.10+
  
- Groq API Key → https://console.groq.com/
  
- AWS EC2 (Ubuntu 22.04)
  
- FAISS, LangChain, Streamlit

---

# 📥 Installation (Local)

git clone <your-repo-url>

cd project

pip install -r requirements.txt ````

# Set your Groq key:

GROQ_API_KEY="your_key_here"

### NOTE: API key key you can give two ways. first one is through environmet, you can store it is security pupose, one can access you api key. and another one is directly we can use with python variable.

# Run the app:

streamlit run app.py

# Deploying on AWS EC2 (Ubuntu)
## 1️⃣ Launch EC2 Instance

Choose Ubuntu 22.04

Instance type: t2.micro (Free Tier)

Enable port 22 (SSH)

Add rule → port 8501 (Streamlit)

## 2️⃣ Connect to EC2 via SSH
ssh -i your-key.pem ubuntu@your-ec2-public-ip

## 3️⃣ Update Server
sudo apt update && sudo apt upgrade -y

sudo apt install python3 pip -y

## 4️⃣ Clone Your Project on EC2 or through project folder path
git clone <your-repo-url>

cd project

pip install -r requirements.txt

# 5️⃣ Set Groq API Key on EC2
echo 'export GROQ_API_KEY="your_key_here"' >> ~/.bashrc
source ~/.bashrc

# 6️⃣ Start Streamlit App
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

# 7️⃣ Access Chatbot in Browser
http://<your-ec2-public-ip>:8501

# 🚀 Run Streamlit in Background (Optional)

So the server keeps running even after SSH disconnect:

nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

# 🧹 Stopping Streamlit
pkill streamlit

# 🔒 Security Notes

Never expose your Groq API Key in GitHub

Keep port 8501 open only while testing

Use Nginx Reverse Proxy + SSL for production


# Acknowledgements

Groq AI

LangChain

FAISS

AWS EC2


---


