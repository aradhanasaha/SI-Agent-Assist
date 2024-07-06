import pandas as pd

ticket_id = "TKT001"
agent_id = "123"

df_agent = pd.read_csv("data\Agent.csv")


df_customer = pd.read_csv("data\customer.csv")


df_data = pd.read_csv("data\data.csv")


df_dataset = pd.read_csv("data\dataset.csv")

# Merge datasets on Customer_ID
merged_df = pd.merge(df_customer, df_data, on='Customer_ID', how='inner')


selected_column = ["Agent_Name","Agent_ID","Password","Agent_emailaddress","Agent_phonenumber"]
df_agent_unique = df_agent[selected_column].drop_duplicates()


# agent_name = df_agent.loc[df_agent['Agent_ID'] == agent_id, 'Agent_Name'].iloc[0]

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
