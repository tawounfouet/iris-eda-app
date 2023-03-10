import time
import datetime
import streamlit as st


def main():
    """ Simple Iris EDA App """

    st.title("Iris EDA App with Streamlit")
    st.subheader("Streamlit is Cool")

    # Custom Color/Style
    html_page = """
    <div style="background-color: tomato;
            padding: 50px;
            color: aliceblue;">
        <p style="font-size: 50px;">Streamlit is Awesome</p>
    </div>
    <br>
    """
    st.markdown(html_page, unsafe_allow_html=True)

    # Date/Time
    st.markdown("#### Date/Time")
    today = st.date_input("Today is", datetime.datetime.now())

    the_time = st.time_input("The time is", datetime.time(10, 0))

    # Display JSON, CODE
    st.markdown("#### Display JSON, CODE")
    data = {
        "name": "John",
        "salary": 5000,
    }
    st.json(data)



if __name__ == '__main__':
    main()
