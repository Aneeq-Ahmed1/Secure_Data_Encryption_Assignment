import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# --------- Configuration ---------
st.set_page_config(page_title="Secure Encryption System 🔐", layout="centered")

# --------- Generate Encryption Key (Keep same during runtime) ---------
if "cipher" not in st.session_state:
    KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(KEY)

# --------- Session State for App Data ---------
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authorized" not in st.session_state:
    st.session_state.authorized = True

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --------- Utility Functions ---------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return st.session_state.cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()

# --------- Theme Toggle ---------
with st.sidebar:
    st.markdown("## 🎨 Theme")
    if st.button("🌙 Toggle Dark Mode" if not st.session_state.dark_mode else "☀️ Toggle Light Mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode

    if st.session_state.dark_mode:
        st.markdown(
            """
            <style>
                body { background-color: #0e1117; color: white; }
                .stButton > button { background-color: #444654; color: white; }
                .stTextInput > div > input { background-color: #1e1e1e; color: white; }
                .stTextArea > div > textarea { background-color: #1e1e1e; color: white; }
            </style>
            """,
            unsafe_allow_html=True
        )

# --------- App Title ---------
st.markdown("<h1 style='color:#6c63ff;'>🔐 Secure Data Encryption System</h1>", unsafe_allow_html=True)

# --------- Navigation ---------
menu = ["🏠 Home", "📝 Store Data", "🔓 Retrieve Data", "🔑 Login"]
choice = st.sidebar.radio("Navigation", menu)

# --------- Pages ---------
if choice == "🏠 Home":
    st.success("Welcome! Use this app to **securely store and retrieve** your data using passkeys.")
    st.info("🔐 Your data is encrypted using **Fernet (symmetric encryption)** and protected with SHA-256 hashed passkeys.")

elif choice == "📝 Store Data":
    st.subheader("📦 Store Your Data")
    user_data = st.text_area("🔸 Enter your secret data:")
    passkey = st.text_input("🔑 Create a passkey:", type="password")

    if st.button("✅ Encrypt & Save"):
        if user_data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(user_data)
            st.session_state.stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted, language='text')
        else:
            st.warning("⚠️ Please enter both data and a passkey!")

elif choice == "🔓 Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🚫 Too many failed attempts. Please log in to continue.")
        st.stop()

    st.subheader("🔍 Retrieve Encrypted Data")
    encrypted_input = st.text_area("🔐 Enter encrypted data:")
    passkey_input = st.text_input("🔑 Enter passkey to decrypt:", type="password")

    if st.button("🔓 Decrypt"):
        if encrypted_input and passkey_input:
            hashed_input = hash_passkey(passkey_input)
            record = st.session_state.stored_data.get(encrypted_input)

            if record and record["passkey"] == hashed_input:
                decrypted = decrypt_data(encrypted_input)
                st.success(f"✅ Decrypted Data:\n\n{decrypted}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")

                if st.session_state.failed_attempts >= 3:
                    st.session_state.authorized = False
                    st.warning("🚫 You have been locked out. Please go to the Login page.")
        else:
            st.warning("⚠️ All fields are required!")

elif choice == "🔑 Login":
    st.subheader("🔐 Reauthorize to Continue")
    password = st.text_input("Enter admin password:", type="password")

    if st.button("🔁 Login"):
        if password == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Successfully logged in! You can now access retrieval again.")
        else:
            st.error("❌ Incorrect admin password.")

