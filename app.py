import streamlit as st
from blog_generation import generate_title, generate_content


st.set_page_config(page_title="AI Blog Generator", layout="centered")
st.title("📝 AI-Powered Blog Generator")

user_input = st.text_input("Enter a topic for your blog:", "")

if st.button("Generate title"):
    if not user_input.strip():
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating Title..."):
            title = generate_title(user_input)  # Call the imported function
            st.subheader(f"📌 Blog Title: {title}")

if st.button("Generate content"):
    if not user_input.strip():
        st.warning("Please enter a topic!")
    else:
        with st.spinner("Generating Blog Content..."):
            blog_content = generate_content(user_input)  # Call the imported function
            st.write(blog_content)

        st.download_button(
            label="📥 Download Blog as Text File",
            data=blog_content,
            file_name="generated_blog.txt",
            mime="text/plain",
        )
