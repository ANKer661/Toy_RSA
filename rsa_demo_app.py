import streamlit as st

from rsa.keys_generation import generate_keypair
from rsa.rsa_operations import rsa_pipeline

st.title("RSA Encryption and Decryption")

# Key generation with specified bit length
key_length = st.number_input(
    "Enter the bit length for key generation:",
    min_value=512,
    max_value=4096,
    value=1024,
    step=512,
)

if st.button("Generate Keys"):
    st.session_state["keys"] = generate_keypair(key_length)
    st.session_state["keys_generated"] = True

if "keys_generated" in st.session_state:
    st.write("Public Key:", st.session_state["keys"]["public"])
    st.write("Private Key:", st.session_state["keys"]["private"])

# Input message
message = st.text_input("Enter a message:", "Hello, World!")

# Encrypt and Decrypt
if st.button("Encrypt and Decrypt"):
    if "keys" not in st.session_state:
        st.error("Please generate keys first.")
    else:
        try:
            final_message, outputs = rsa_pipeline(message, st.session_state["keys"])
            st.write("Original Message:", message)
            st.write("Message As Number:", outputs.message_as_number)
            st.write("Encrypted Message:", outputs.encrypted_message)
            st.write("Decrypted Message (as number):", outputs.decrypted_message)
            st.write("Final Message:", final_message)
        except ValueError as e:
            st.error(f"Encryption failed: {str(e)}")
            st.warning("Please try shorter message or longer keys")
