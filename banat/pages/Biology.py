import streamlit as st
import google.generativeai as genai

# WARNING: Hardcoded API key for local testing ONLY.
# Replace "YOUR_ACTUAL_API_KEY" with your actual API key.
GEMINI_API_KEY = "AIzaSyBIVtuxm9cA3U0r49vpC3lYHusQPaweMlk"  # Replace this
genai.configure(api_key=GEMINI_API_KEY)

# Model for use
model = genai.GenerativeModel("gemini-1.5-flash")

def call_gemini_api(prompt):
    """
    Calls the Gemini API using SDK with the user's prompt and returns the response.
    Handles errors.
    """
    try:
        preamble = "You are a helpful biology tutor for K-12 students. Explain the following in simple terms, using examples, and avoid overly technical jargon. If the question is ambiguous, respond with a question asking for clarification. Do not ask me to provide further context on this unless it is ambiguous, respond with a specific question that can help clarify:"
        full_prompt = f"{preamble} {prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Biology Page Function
def biology_page():
    st.title("Biology Tutor")
    st.write("Welcome! I'm here to help you with your SS biology questions. Let's explore the fascinating world of Biology!")

    # --- Chat Box Section ---
    st.header("Ask a Biology Question")
    st.write("Type your biology question below, and I'll do my best to explain it in a way that's easy to understand:")

    # Chat input box
    user_input = st.text_input("Ask me a biology question", placeholder="e.g., What is Photosynthesis?")

     # Submit button
    if st.button("Ask"):
        if user_input.strip() == "":
             st.warning("Please enter a question before clicking 'Ask'.")
        else:
            # Show a spinner while waiting for the API response
            with st.spinner("Let me find that out for you!"):
                # Call the Gemini API
                response = call_gemini_api(user_input)
                if response.lower().startswith("i need more context"):
                    st.warning("Your question was too broad, rephrase it, and provide more specifics")
                else:
                    # Display the response
                    st.success("Here's the answer:")
                    st.write(response)

# Call the function to render the page
biology_page()