import streamlit as st
from arabic_support import support_arabic_text
import google.generativeai as genai

# WARNING: Hardcoded API key for local testing ONLY.
# Replace "YOUR_ACTUAL_API_KEY" with your actual API key.
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # Replace this
genai.configure(api_key=GEMINI_API_KEY)

# Apply Arabic text support
support_arabic_text(all=True)

# Model for use
model = genai.GenerativeModel("gemini-1.5-flash")

def call_gemini_api(prompt):
    """
    Calls the Gemini API using SDK with the user's prompt and returns the response.
    Handles errors.
    """
    try:
        preamble = "أنت معلم أدب عربي متخصص للطلاب. اشرح الموضوع بطريقة بسيطة وواضحة، واستخدم أمثلة، وتجنب المصطلحات التقنية المعقدة. إذا كان السؤال غامضًا، اطلب توضيحًا:"
        full_prompt = f"{preamble} {prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

# Arabic Literature Page Function
def arabic_literature_page():
    # Custom CSS for precise RTL alignment
    st.markdown("""
    <style>
    .stMarkdown, .stTitle, .stHeader, .stButton {
        text-align: right;
    }
    .stMarkdown h1, .stMarkdown h2 {
        text-align: right;
    }
    .stButton > button {
        float: right;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main Title with bold markdown
    st.markdown("<h1 style='text-align: right;'>**معلم الأدب العربي**</h1>", unsafe_allow_html=True)
    st.write("مرحبًا بك! أنا هنا لمساعدتك في أسئلة الأدب العربي. دعنا نستكشف عالم الأدب معًا!")

    # Chat Section with bold markdown for header
    st.markdown("<h2 style='text-align: right;'>**اسأل سؤالًا في الأدب العربي**</h2>", unsafe_allow_html=True)
    st.write("اكتب سؤالك أدناه، وسأحاول شرحه بطريقة سهلة الفهم:")

    # Chat input box
    user_input = st.text_input("اطرح سؤالًا عن الأدب العربي", placeholder="مثال: ما هي خصائص شعر المعلقات؟")

    # Submit button
    if st.button("اسأل"):
        if user_input.strip() == "":
            st.warning("يرجى إدخال سؤال قبل النقر على 'اسأل'")
        else:
            # Show a spinner while waiting for the API response
            with st.spinner("دعني أبحث عن الإجابة لك!"):
                # Call the Gemini API
                response = call_gemini_api(user_input)
                if response.lower().startswith("أحتاج إلى مزيد من السياق"):
                    st.warning("سؤالك كان عامًا جدًا، يرجى إعادة صياغته وتقديم تفاصيل أكثر")
                else:
                    # Display the response
                    st.success("إليك الإجابة:")
                    st.write(response)

# Call the function to render the page
if __name__ == "__main__":
    arabic_literature_page()