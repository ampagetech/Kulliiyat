import streamlit as st

def about_page():
    # Ensure content is displayed
    # st.image("assets/profile_image.png", width=230)  # Corrected image path (Commented out)
    st.title("Kulliyatul Banat Kaduna", anchor=False)
    st.write("Kulliyatul Banat is a faith-based Girls college.")

    st.subheader("More about the school", anchor=False)
    st.write("""
    Kulliyatul Banat is a faith-based Girls college meant to provide affordable good quality modern and religious education to the women folks. The school is sex-biased to promote and improve the educative quality of both students and teachers who could otherwise be denied such opportunity in mixed schools because of fear -dictated by modesty – of the moral decadence that has permeated the education sector in the country and even world at large.
    """)

    st.subheader("Key Skills", anchor=False) # Updated section title
    st.write("""
    **Core Academic Skills:**
    *   **Literacy and Communication:**
        *   Advanced Reading and Comprehension: Ability to analyze complex texts, critical thinking, and in-depth understanding of various subjects.
        *   Effective Written Communication: Proficiency in writing clear, concise, and well-structured essays, reports, and other written materials.
        *   Public Speaking and Presentation Skills: Confidence in delivering presentations and expressing ideas clearly in front of an audience.

    *   **Mathematical and Analytical Skills:**
        *   Problem-Solving: Ability to approach and solve mathematical problems, including logical reasoning and application of mathematical principles.
        *  Basic Statistical Understanding: Ability to interpret data, understand basic statistics and perform simple calculations.
        *  Financial Literacy: Ability to manage finances, understand budgeting, and make informed decisions.

    **Digital Literacy & Modern Skills**
    *   Basic Computer Literacy: Proficiency in using computers, operating systems, word processors (like MS Word), spreadsheets (like MS Excel) and presentation software.
    *   Internet Research Skills:  Ability to effectively search online for information, evaluate sources, and synthesize data.
    *   Digital Communication: Proficiency in using email and other digital communication tools for effective communication.
    *   Information Management: Using applications for managing files, notes and ideas.

    **Religious & Cultural Skills**
    *   Quranic Studies:  In-depth knowledge of the Quran, including recitation, interpretation and application.
    *   Hadith Studies: Understanding of Hadith literature and its role in Islamic practice.
    *   Islamic Jurisprudence: Basic understanding of Islamic law and its principles.
    *   Arabic Proficiency: Reading, writing, and basic spoken Arabic as used in Islamic texts.

    **Interpersonal & Leadership Skills:**
    *   Collaboration and Teamwork: Working effectively with peers in groups, sharing ideas, and achieving common goals.
    *   Leadership Skills: Developing leadership qualities such as decision-making, organization, and initiative.
    *   Conflict Resolution: Ability to mediate disagreements and find peaceful solutions.
    *   Empathy and Understanding: Ability to appreciate and relate to others, with diverse backgrounds.
    """)

# Ensure the page is callable
about_page()