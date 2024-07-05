
# Proper functional one for now =====================================================================================================================

# ===================================================== Import libraies ============================================================================
import streamlit as st
import pandas as pd
# import plotly.express as px
from streamlit_pills import pills

import os
from dotenv import load_dotenv
import google.generativeai as gen_ai
import google.ai.generativelanguage as glm
import re

# ====================================================== Load Dataset ========================================================
df_agent = pd.read_csv("C:/Users/shrestha.ria/Documents/Agent.csv")
print(df_agent)

df_customer = pd.read_csv("C:/Users/shrestha.ria/Documents/customer.csv")
print(df_customer)
print(df_customer.info())

df_data = pd.read_csv("C:/Users/shrestha.ria/Documents/data.csv")
print(df_data)

df_dataset = pd.read_csv("C:/Users/shrestha.ria/Documents/dataset.csv")
print(df_dataset)

# Merge datasets on Customer_ID
merged_df = pd.merge(df_customer, df_data, on='Customer_ID', how='inner')
print(merged_df)

selected_column = ["Agent_Name","Agent_ID","Password","Agent_emailaddress","Agent_phonenumber"]
df_agent_unique = df_agent[selected_column].drop_duplicates()
print(df_agent_unique)

# ============================================ Setting Ticket ID and agent ID ===================================================
ticket_id = "TKT001"
agent_id = "123"

# ============================================== Gemini Parameters ======================================================================
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro APPI model
gen_ai.configure(api_key=GOOGLE_API_KEY)

# ============================================== Response model (AI is customer) ==========================================================
generation_config_1 = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 90,
  "max_output_tokens": 20000,
  # "response_mime_type": "text/plain"
}

safety_settings_1 = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model_1 = gen_ai.GenerativeModel(
    model_name= "gemini-1.5-pro",
    generation_config = generation_config_1,
    safety_settings = safety_settings_1)

def translate_role_for_streamlit_col1(user_role_1):
    if user_role_1 == "model":
        return "assistant"
    else:
        return user_role_1

# ================================================== Recommendation model (AI is assistant) ==========================================
generation_config_2 = {
  "temperature": 0.9,
  "top_p": 0.8,
  "top_k": 65,
  "max_output_tokens": 20000,
  # "response_mime_type": "text/plain"
}
safety_settings_2 = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model_2 = gen_ai.GenerativeModel(
    model_name= "gemini-1.5-pro",
    generation_config= generation_config_2,
    # generation_config = glm.GenerationConfig(candidate_count = 3),
    safety_settings = safety_settings_2
)

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

    # =========================================== Top KPI's for agent ===================================================================

    # agent_name = df_agent.loc[df_agent['Agent_ID'] == agent_id, 'Agent_Name'].iloc[0]
    # print(agent_name)
    daily_average = int(df_agent[df_agent["Agent_Name"] == "Sam"]["Count_customer"].sum())
    rewards_points = int(df_agent[df_agent["Agent_Name"] == "Sam"]["Rewards_points"].sum())
    average_ratings = round(df_agent[df_agent["Agent_Name"] == "Sam"]["Ratings"].mean(),1)
    star_ratings = ":star:" *int(round(average_ratings,0))
    # name = df_agent_unique[df_agent_unique["Agent_ID"] == agent_id]["Agent_Name"]
    # email_address = df_agent_unique[df_agent_unique["Agent_ID"] == agent_id]["Agent_emailaddress"]

    # ============================================ Top KPI's for customer ==========================================================================

    customer_ID = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_ID'].iloc[0]
    customer_name = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_Name'].iloc[0]
    customer_emailaddress = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_emailaddress'].iloc[0]
    customer_phonenumber = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_phonenumber'].iloc[0]
    customer_type = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_type'].iloc[0]
    duration = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Customer_duration_in_months'].iloc[0]
    purchase_frequency = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Purchase_Frequency'].iloc[0]
    favourite_product_type = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Favourite_Product_type'].iloc[0]
    recent_growth = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Recent_growth'].iloc[0]
    average_spending = merged_df.loc[merged_df['Ticket_ID'] == ticket_id, 'Average_spending(per_product)'].iloc[0]


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

    # ============================================== Streamlit Interface ======================================================================

    def main():
        # Create two columns layout
        col1, col2 = st.columns([6, 4])

        with col1:
            st.title("Agent Interaction Window")

            with st.container(height=1000):

                # ============================================ Response model 1 Col 1 ======================================================
                # Initialize chat session in Streamlit if not already present
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

                context_1 = f"""
                    You are a customer at a multi national company which sells product related to retail, electronics, home items and groceries.
                    You have to ask questions related to the various policies of company which are of different types like pricing, offers, discounts, EMI, payment options, delivery, shipping and privacy.
                    You as a customer who has to ask questions in 1 line about either of these policies.
                    You are not an AI assistant. You are not there to answer any question. you can not even ask the user to ask questions to them.
                    
                    Some examples for the questions are stated below:-
                    How do I know my order has been confirmed?
                    Can I buy online and pick delivery at the nearest store?
                    How can I track my order?
                    Can I get a GST invoice for my order?
                    What are the different payment options?
                    How can I apply for an EMI?
                    What are the different EMI options?
                    What are the various discounts currently going on the various products of the company?
                    What to do if my items are damaged?
                    It's been 10 days and I have not received my orders,could you please guide me or help me connect with the customer service?
                    Can you check the status of my returned item?
                    How to add special instructions for shipping?
                    
                    These are some examples of the questions that you can ask or something similar.
                    Your questions should not include any information or answers related to anything.
                    You are a customer who has questions so strictly restrict yourself from answering things.
                    
                    After a questions has been asked by you, you then have to take the conversation forward by about 3 to 4 reply from the user's side. 
                    The user's response is received via {user_prompt_1}.
                    
                    Based on the responses received provided by the user answers the questions that you have asked, you need to thank the agent for their prompt response and then ask a follow up question for realted to the previous repply.
                    
                    
                    On the basis of the user's response you as a customer has to carry forward the conversation till you get the answers of the questions you asked for.
                    Strictly ask only 1 question at a time. 
                    Do not ask multiple questions naming them as 1 and 2 and so on.
                    
                    Ask questions related to the product policies.
                    Do not ask questions related to the company's area of work, internal policies, HR policies. You are aware of the company's basic products.
                    Ask questions as a customer who is willing to buy things from there.
                    Do not ask questions related to policies of working remotely, etc.
                    Ask questions related to the shipping/ return policies or about discounts/ offers or emi policies.
    
                    """

                chat_session_1 = model_1.start_chat(
                    history=[
                        {
                            "role": "user",
                            "parts": [context_1]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Can I buy multiple products in one order?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Yes, you can buy multiple products in one order. Simply add the items to your cart and proceed to checkout."
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Alright, can you guide me to find the cart?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Sure, you can open your mobile app and then on to the at-most right you would find cart symbol."
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Can I get a GST invoice for my order?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello! Yes, you can obtain a GST invoice. You can provide your GST details at checkout or contact customer support with your order number and GST details after purchase. Thank you!"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Can you guide me with my electronics item which is under warranty but not working?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello! For warranty service, please contact our customer support team with your order number and a description of the issue. We will guide you through the process for repair or replacement. Thank you!"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Okay, I want to get it repaired. Can you help me with that?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello! Sure, please provide your order number and issue details. We will arrange for the repair service under warranty. Thank you!"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Okay, so my order number is XXXXXXX and that was a laptop which is not starting."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Alright, Would Thursday be suitable for you to come to your nearest shop? If yes would book your slot."
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Yes so Thursday seems fine to me. Thank you!"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Happy to help. Let me know if have any other questions."
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Hello, I am willing to buy an earbuds but I find it very expensive at your store and am getting a good price somewhere else. Could you please look into it? "
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer."
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Okay so I got this offer at a XYZ company which is giving me 30% discount based on the my credit score. "
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello, How are you? "
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "I am good but I need some questions to be answered related to your product policies?"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Sure, go ahead. Feel free to ask anything. I will be happy to help."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Alright. My question is What is the EMI policies of the product category of electronics?"
                            ]
                        }
                    ]
                )

                # ====================================== Display chat history ==================================================================================

                # print(len(st.session_state.chat_session_1.history))
                for message_1 in st.session_state.chat_session_1.history:
                    with st.chat_message(translate_role_for_streamlit_col1(message_1.role)):
                        st.markdown(message_1.parts[0].text)
                # selected = None
                #
                # if user_input_1:
                #     user_prompt_1 = user_input_1
                # else:
                #     user_prompt_1 = st.chat_input(st.write(selected))

                if user_prompt_1:
                    # add user's message to chat and display it
                    st.chat_message("user").markdown(user_prompt_1)
                    # st.session_state.chat_history.append({"role": "user", "text": user_prompt_1})
                    # Send user's message to Gemini-pro and get the response
                    gemini_response_1 = st.session_state.chat_session_1.send_message(user_prompt_1)
                    # st.session_state.chat_history.append({"role": "assistant", "text": gemini_response_1.text})

                    # Display Gemini Pro response
                    with st.chat_message("assistant"):
                        st.markdown(gemini_response_1.text)

                    # text_1 = gemini_response_1.text

        with (col2):
            st.title("Customer Details")
            st.subheader("Ticket ID: " +f"{ticket_id}")

            # left_col,right_col = st.columns(2)

            # with left_col:
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


                context_2 = f"""
                    You are an agent at the customer support of a Multinational company which has product related to retail, electronics, home items and groceries.
                    You know your company really well and have answers to all the questions related to the various policies.
                    The different types of policies ranges from pricing policies , information related to offers, discounts, EMI policies, available payment options, delivery, shipping and privacy policies.
                    You need to generate 3 appropriate responses as the agent to answer the query. The response should be a maximum of 40 words.
                    Your customers are very valuable and thus you have to be very supportive and answer the questions wisely and in a helpful tone.
                    You response will have to be in 3 ways and each of the ways should start with 'Recommendation 1:', Recommendation 2:' and Recommendation 3:' 
                    The three recommendations are just different ways to put the answer. Couple of examples are displayed below."
                    Examples:-
                    If users asks 'How do I know my order has been confirmed?'
                    The answers via model should be:-  
                    Recommendation 1: Hello! You will receive an email confirmation with your order details shortly after placing your order. Thank you!\n Recommendation 2: Hello! After placing your order, you will receive an email confirmation with all the details. You can also check your order status in your account on our website. Thank you! \n Recommendation 3: Hello! You can check your mail, you would have received a mail regading confirmation.
                    If users asks 'How can I apply for an EMI?'
                    The answers via model should be:-
                    Recommendation 1: Hello! To apply for an EMI, choose the EMI option during checkout and select your preferred bank and plan. Thank you!\n Recommendation 2: Hello! You can apply for an EMI during the checkout process by selecting the EMI payment option. Choose your bank and preferred EMI plan, then complete the payment. Thank you! \n Recommendation 3: Hello! Select the EMI option at checkout, choose your bank and plan, and complete the payment. Thank you!
                    It is important that the answer which you are providing are separated by the keywords 'Recommendation 1:', 'Recommendation 2:' and 'Recommendation 3:'
                    The recommendations should start by greeting the customer and then answer the question precisely.
                    If the questions asks the customer to directly connect with the human agent. Ask then to call on their tool free no. This as well in three different ways. 
                    The customer can say anything, despite of you having any proper or concrete answer provide 3 separate ways to answer/ reply what the customer has written as the headings specified i.e. Recommendation 1: Recommendation 2: and Recommendation 3:.
                    You can also comment on the tone in which the customer has asked the query in the prior description. Do not comment anything about the tone in the three recommendation.
                    
                    """

                # Start the chat session with the context included in the initial history
                chat_session_2 = model_2.start_chat(
                    history=[
                        {
                            "role": "user",
                            "parts": [context_2],
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Hello, I am here to assist you with your queries related to the policies of our ecommerce company. Please feel free to ask."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Can I get a GST invoice for my order?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Yes, you can obtain a GST invoice. Provide your GST details at checkout or contact customer support with your order number and GST details after purchase. Thank you! \n Recommendation 2: Hello! You can get a GST invoice by providing your GST number during checkout. If missed, contact customer support with your order and GST details to get the invoice. Thank you!\n Recommendation 3: Hello! To get a GST invoice, provide your GST number during checkout. If missed, contact customer support with your order number and GST details, and we’ll send you the invoice. Thank you!"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Can you guide me with my electronics item which is under warranty but not working?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Please contact our customer support with your order number and issue details. We will assist you with warranty service and repair or replacement options. Thank you! \n Recommendation 2: Hello! For warranty service, please contact our customer support team with your order number and a description of the issue. We will guide you through the process for repair or replacement. Thank you!\n Recommendation 3: Hello! For warranty assistance, provide issue details and order number with necessary details. You can then proceed with either repairement or replacement. "
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Okay, I want to get it repaired. Can you help me with that?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Sure, please provide your order number and issue details. We will arrange for the repair service under warranty. Thank you! \n Recommendation 2: Hello! Absolutely, please share your order number and a brief description of the issue. We will schedule a repair service and provide further instructions. Thank you!\n Recommendation 3: Hello! To proceed with the repair. Kindly provide your order details. We will schedule an appointment for you."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How can I apply for an EMI?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! To apply for an EMI, choose the EMI option during checkout and select your preferred bank and plan. Thank you! \n Recommendation 2: Hello! You can apply for an EMI during the checkout process by selecting the EMI payment option. Choose your bank and preferred EMI plan, then complete the payment. Thank you!\n Recommendation 3: Hello! Select the EMI option at checkout, choose your bank and plan, and complete the payment. Thank you!"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello, I am willing to buy an earbuds but I find it very expensive at your store and am getting a good price somewhere else. Could you please look into it? "
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Thank you for reaching out. We offer top-quality products with excellent customer service, including warranties and easy returns. Can you provide the price you found elsewhere?\n Recommendation 2: Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer. \n Recommendation 3: Thank you for your concern. Have you checked our current promotions? We offer benefits like free shipping, loyalty points, and extended warranties. Let me know if you need assistance."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Okay so I got this offer at a XYZ company which is giving me 30% discount based on the my credit score. "
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Thank you for sharing this. We can offer a similar discount based on your credit score. Please provide the details, and we’ll proceed. \n Recommendation 2: Thank you for the info. We strive to offer competitive pricing. Let’s review your credit score to see if we can match or improve on this offer. \n Recommendation 3: Thank you for the update. We offer various discounts and financing options. Let's check your eligibility for similar or better deals."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How do I know my order has been confirmed?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! You will receive an email confirmation with your order details shortly after placing your order. Thank you!\n Recommendation 2: Hello! After placing your order, you will receive an email confirmation with all the details. You can also check your order status in your account on our website. Thank you! \n Recommendation 3: Hello! You can check your mail, you would have received a mail regading confirmation."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How can I apply for an EMI?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! To apply for an EMI, choose the EMI option during checkout and select your preferred bank and plan. Thank you!\n Recommendation 2: Hello! You can apply for an EMI during the checkout process by selecting the EMI payment option. Choose your bank and preferred EMI plan, then complete the payment. Thank you! \n Recommendation 3: Hello! Select the EMI option at checkout, choose your bank and plan, and complete the payment. Thank you!"
                            ]
                        }
                    ]
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