
# Proper functional one for now =====================================================================================================================

# ===================================================== Import libraies ============================================================================
import streamlit as st
import pandas as pd
# import plotly.express as px

import os
import google.generativeai as gen_ai
import google.ai.generativelanguage as glm
import re

from models import model_1,model_2
from preprocess import (ticket_id,agent_id,customer_ID,customer_name,customer_emailaddress,
    customer_phonenumber,customer_type,duration,purchase_frequency,favourite_product_type,
    recent_growth,average_spending,daily_average,rewards_points,average_ratings,star_ratings
)
from context import context_one,context_two
from history import get_history1,get_history2
GOOGLE_API_KEY = 'AIzaSyDuR12RvaTOfL7c_hDLmzRF0OPqxIEYO74'

# Set up Google Gemini-Pro APPI model
gen_ai.configure(api_key=GOOGLE_API_KEY)


def translate_role_for_streamlit_col1(user_role_1):
    if user_role_1 == "model":
        return "assistant"
    else:
        return user_role_1

# ================================================== Recommendation model (AI is assistant) ==========================================


def translate_role_for_streamlit_col2(user_role_2):
    if user_role_2 == "model":
        return "assistant"
    else:
        return user_role_2



# ===================================================== Authentication =========================================================================
def creds_entered():
    if st.session_state["user"].strip() == agent_id and st.session_state["passwd"].strip() == "abc":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please Enter Password")
        elif not st.session_state["user"]:
            st.warning("Please Enter Agent ID")
        else:
            st.error("Invalid Username/password")

def authenticate_user():
    if "authenticated" not in st.session_state:
            st.write("Agent Login: ")
            st.text_input(label="Agent ID: ", value= "", key="user", on_change= creds_entered)
            st.text_input(label="Password: ", value="", key="passwd", type= "password", on_change= creds_entered)
            return False
    else:
            if st.session_state["authenticated"]:
                return True
            else:
                st.write("Agent Login: ")
                st.text_input(label="Agent ID: ", value="", key="user", on_change=creds_entered)
                st.text_input(label="Password: ", value="", key="passwd", type="password", on_change=creds_entered)
                return False


if authenticate_user():

    # Configure Streamlit page setup
    st.set_page_config(
        page_title= "Agent Assist AI",
        layout= "wide",
        page_icon= "👩🏻‍💻"
    )

    # Streamlit page title
    st.title("💻 Agent Assist AI")

  
    # ================================================= Sidebar ===============================================================================

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
    else:
        st.session_state["authenticated"] = True

    st.sidebar.title("Welcome Sam!")
    # st.sidebar.title("Welcome " +f"{name}" +"!")
    # st.sidebar.write("Email: " + f"{email_address}")

    with st.sidebar.expander("My Stats"):
        with st.container(height= 50):
            st.write("Daily Average: " + f"{daily_average}")
    with st.sidebar.expander("My Rewards"):
        with st.container(height=50):
            st.write("Rewards: " + f"{rewards_points}")
    with st.sidebar.expander("My Ratings"):
        with st.container(height=50):
            st.write(f"{average_ratings} {star_ratings}")

    def main():
        # Create two columns layout
        col1, col2 = st.columns([6, 4])

        with col1:
            st.title("Agent Interaction Window")

            with st.container(height=1000):
                if "chat_session_1" not in st.session_state:
                    st.session_state.chat_session_1 = model_1.start_chat(history=[
                        {
                            "role": "model",
                            "parts": [
                                "Hello I have a couple of question?"
                            ],
                        }
                    ])

                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []

                # input field for user's message prompt
                user_prompt_1 = st.chat_input("Answer the customer")

                context_1 = context_one

                chat_session_1 = model_1.start_chat(
                    history=get_history1(context_1)
                )

                # ====================================== Display chat history ==================================================================================

                # print(len(st.session_state.chat_session_1.history))
                for message_1 in st.session_state.chat_session_1.history:
                    with st.chat_message(translate_role_for_streamlit_col1(message_1.role)):
                        st.markdown(message_1.parts[0].text)

                if user_prompt_1:
                    # add user's message to chat and display it
                    st.chat_message("user").markdown(user_prompt_1)
                    gemini_response_1 = st.session_state.chat_session_1.send_message(user_prompt_1)

                    with st.chat_message("assistant"):
                        st.markdown(gemini_response_1.text)

                    # text_1 = gemini_response_1.text

        with (col2):
            st.title("Customer Details")
            st.subheader("Ticket ID: " +f"{ticket_id}")
            # ============================================== Customer Details ===========================================================

            with st.container(height=100):
                st.write("Customer Name: " + f"{str(customer_name)}            " + "Customer ID: " + f"{str(customer_ID)}")
                st.write("Email: " + f"{customer_emailaddress}              " + "Contact No: " + f"{customer_phonenumber}")
                st.write("Customer Type: " + f"{customer_type}              " + "Customer Duration: " + f"{duration}" +" months")

            # with right_col:
            with st.container(height = 100):
                st.write("Product Type: " + f"{favourite_product_type}               " + "Frequency: " + f"{purchase_frequency}")
                st.write("Avg expenditure: " + f"{average_spending}               " + "Recent trend: " + f"{recent_growth}")

            st.markdown("----")

            # ================================================= Recommendation Model ====================================================================

            st.title("Suggestions for Agent")

            with st.container(height=750):
                # st.write(gemini_response_1.text)

                if "chat_session_2" not in st.session_state:
                    st.write(
                        "Recommendation 1: Hello, I am here to assist you with your queries related to the policies of our ecommerce company. Please feel free to ask.\n Recommendation 2: Hello! Sure go ahead with your question related to our company policies. \n Recommendation 3: Hello! Hope you are doing well. You can ask your questions. We provide a range of products in the retails industry.")

                    st.session_state.chat_session_2 = model_2.start_chat(history=[
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello, I am here to assist you with your queries related to the policies of our ecommerce company. Please feel free to ask.\n Recommendation 2: Hello! Sure go ahead with your question related to our company policies. \n Recommendation 3: Hello! Hope you are doing well. You can ask your questions. We provide a range of products in the retails industry.  "
                            ],
                        }
                    ])


                context_2 = context_two

                # Start the chat session with the context included in the initial history
                chat_session_2 = model_2.start_chat(
                    history=get_history2(context_2)
                )

                # user_prompt_2 = gemini_response_1
                gemini_response_2 = chat_session_2.send_message(gemini_response_1.text)

                st.write(gemini_response_2.text)
                text_2 = gemini_response_2.text

                # Initialize recommendation variables
                recommendation_1 = recommendation_2 = recommendation_3 = " Welcome!"

                # Define the patterns
                pattern1 = r"(?<=Recommendation 1:\s)(.*?)(?=\sRecommendation 2:)"
                pattern2 = r"(?<=Recommendation 2:\s)(.*?)(?=\sRecommendation 3:)"
                pattern3 = r"(?<=Recommendation 3:\s)(.*?)(?=\s*$)"

                # Search for the patterns in the text
                match1 = re.search(pattern1, text_2, re.DOTALL)
                if match1:
                    recommendation_1 = match1.group(1).strip()

                match2 = re.search(pattern2, text_2, re.DOTALL)
                if match2:
                    recommendation_2 = match2.group(1).strip()

                match3 = re.search(pattern3, text_2, re.DOTALL)
                if match3:
                    recommendation_3 = match3.group(1).strip()

                # Store the recommendations in a list
                recommendations = [recommendation_1, recommendation_2, recommendation_3]

                with st.container():
                    selected = pills("Recommendations: ", recommendations, None, None)
                    st.write(selected)

    if __name__ == "__main__":
        main()