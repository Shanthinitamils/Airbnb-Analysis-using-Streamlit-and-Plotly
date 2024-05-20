import streamlit as st
def app():
    st.title(":blue[Airbnb Analysis Using Streamit and Plotly]")
    col2,col1=st.columns([2,1])
    with col2:
         st.write("""
    ### :green[About Airbnb:]
    Airbnb is an online marketplace that connects travelers with local hosts who offer unique accommodations and experiences. Founded in 2008, Airbnb has grown into a global platform with millions of listings in over 220 countries and regions.
    """)
         st.write("""
    ### :green[Key Features of Airbnb:]
    - **Accommodations**: Airbnb offers a wide range of accommodations, including apartments, houses, villas, and unique properties like treehouses and yurts.
    - **Experiences**: In addition to lodging, Airbnb hosts can offer experiences such as guided tours, cooking classes, and outdoor adventures.
    - **Host Program**: Individuals can become Airbnb hosts by listing their properties or experiences on the platform, allowing them to earn income and connect with travelers.
    - **Reviews and Ratings**: Airbnb incorporates a review system where guests and hosts can leave feedback, helping to build trust and transparency within the community.
    """)

    st.write("""
    ### :green[About the Dataset:]
    You have Airbnb 2018 data, which includes information about listings, hosts, reviews, and other relevant details. This dataset can provide insights into the types of accommodations available, pricing trends, and popular destinations during the year 2018.
    """)
    with col1:
         st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2JocjltNzB4ZHhncGo3MHZ6Yms4cjNzOXNvamU0dG40cW9oaWJ4ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J1LEDZftGWZrQNrCr5/giphy.gif")

    
