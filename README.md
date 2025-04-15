# 🛡️ Secure Data Encryption System Using Streamlit

## 🔗 Live Demo
**Try it here 👉 [Secure Data App (Streamlit)](https://secure-data-encryption--assignment.streamlit.app/)**

---

## 📌 Overview

This is a **secure data encryption and decryption system** built using **Python** and **Streamlit**. It allows users to:

- Store their data securely with a unique passkey  
- Retrieve the encrypted data using the correct passkey  
- Automatically block access and require reauthentication after multiple failed attempts  

No external database is used — everything is managed in **in-memory storage** during the app session.

---

## 🔐 Key Features

- 🧠 **Fernet Encryption** for strong data protection  
- 🔐 **SHA-256 Hashed Passkeys** for security  
- ⛔ **3-Failed Attempts Lock** with reauthorization via Login  
- 🎛️ **Streamlit UI** with colorful interface and dark/light mode toggle  
- 💾 **In-memory storage** (no files or databases involved)  

---

## 🚀 How It Works

### ✅ Store Data
1. Go to **Store Data** section  
2. Enter any text and a secure passkey  
3. Data is encrypted and saved in memory  

### 🔍 Retrieve Data
1. Go to **Retrieve Data**  
2. Paste encrypted data and enter the correct passkey  
3. Data is decrypted if passkey is valid  
4. After **3 incorrect attempts**, you're forced to **Login** again  

### 🔑 Login Page
Enter the master password (`admin123` by default) to reset access after failed attempts.

---

## 💻 Technologies Used

- Python 3.x  
- Streamlit  
- Cryptography (Fernet)  
- Hashlib (SHA-256)  

---

## 📁 File Structure

```
📦 secure-data-encryption-assignment
├── app.py                ← Main Streamlit app
├── requirements.txt      ← Required Python libraries
└── README.md             ← Project documentation (this file)
```

---

## 📦 Installation & Run Locally

```bash
git clone https://github.com/your-username/secure-data-encryption-assignment.git
cd secure-data-encryption-assignment
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Security Notes

- This is a **demo-level project** and should not be used for production security storage.  
- For production, use **PBKDF2 hashing**, database storage, and encryption key rotation.

---

## 🧠 Assignment Credit

This project is part of a Python assignment to demonstrate:

- Encryption knowledge  
- Streamlit UI development  
- User authentication and control flow handling  

---

## 📬 Contact

For questions, reach out via GitHub Issues or contact aneeq.edward@outlook.com
