import streamlit as st

def main():
    st.set_page_config(
        page_title="Study Material Website",
        page_icon=":books:",
        layout="wide"
    )

    # HTML and CSS for custom styling
    custom_html = """
    <style>
        /* Add custom CSS styles here */
        .header {
            background-color: #3366ff;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .content {
            margin: 0 auto;
            width: 80%;
        }
        .material-container {
            background-color: #f0f0f0;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }
        .material-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .material-description {
            font-size: 16px;
        }
    </style>
    <div class="header">Study Material Website</div>
    """

    st.markdown(custom_html, unsafe_allow_html=True)

    # Main content
    st.markdown("<div class='content'>", unsafe_allow_html=True)

    # Sample study materials
    study_materials = [
        {"title": "Introduction to Python", "description": "Python basics and fundamentals."},
        {"title": "Machine Learning 101", "description": "Introduction to machine learning concepts."},
        {"title": "Web Development with Flask", "description": "Building web applications with Flask."},
    ]

    for material in study_materials:
        st.markdown(
            f"""
            <div class="material-container">
                <div class="material-title">{material['title']}</div>
                <div class="material-description">{material['description']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
