import google.generativeai as genai
import streamlit as st
import os

# Configure the API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get the model's response
def get_response_from_model(user_input):
    response = genai.generate_text(
        prompt=user_input
    )
    return response.result

# Streamlit app layout
st.set_page_config(page_title="My Gemini AI Chatbot", page_icon="✨")
st.title('✨ My Gemini AI Chatbot ✨')
st.markdown("""
    Welcome to **My Gemini**, an AI-powered chatbot using the Google Gemini model.
    Enter your prompt below and see the magic happen!
""")

st.sidebar.header('About')
st.sidebar.info("""
    This chatbot utilizes the Google Generative AI Gemini 1.5 Flash model.
    Powered by Streamlit and Google API.
""")

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Display conversation history in minimal styled boxes
for message in st.session_state.history:
    if message["role"] == "user":
        with st.container():
            st.markdown(f"""
                <div style="padding: 10px; border-radius: 10px; margin: 5px 0; background-color: #f0f0f0; color: black;">
                    <strong>User:</strong> {message["content"]}
                </div>
            """, unsafe_allow_html=True)
    else:
        with st.container():
            st.markdown(f"""
                <div style="padding: 10px; border-radius: 10px; margin: 5px 0; background-color: #e0e0e0; color: black;">
                    <strong>Gemini:</strong> {message["content"]}
                </div>
            """, unsafe_allow_html=True)

# User input and model response
if prompt := st.chat_input("💬 Enter your prompt:"):
    # Display user message
    with st.container():
        st.markdown(f"""
            <div style="padding: 10px; border-radius: 10px; margin: 5px 0; background-color: #f0f0f0; color: black;">
                <strong>User:</strong> {prompt}
            </div>
        """, unsafe_allow_html=True)
    st.session_state.history.append({"role": "user", "content": prompt})

    # Generate response
    with st.spinner("Gemini is thinking..."):
        response = get_response_from_model(prompt)
    
    # Display Gemini's response
    with st.container():
        st.markdown(f"""
            <div style="padding: 10px; border-radius: 10px; margin: 5px 0; background-color: #e0e0e0; color: black;">
                <strong>Gemini:</strong> {response}
            </div>
        """, unsafe_allow_html=True)
    st.session_state.history.append({"role": "assistant", "content": response})

# Footer
st.markdown("""
    ---
    **Made with ❤️ using Streamlit**
""")
