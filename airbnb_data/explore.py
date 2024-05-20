import streamlit as st
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go

import mysql.connector
from sqlalchemy import create_engine

mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor(buffered=True,)

#create a engine to insert data value
engine = create_engine("mysql+mysqlconnector://root:@localhost/airbnb") 
def app():
 

    #create database and use for table creation
    mycursor.execute('create database if not exists airbnb')
    mycursor.execute('use airbnb')
    icon='https://avatars.githubusercontent.com/u/698437?s=280&v=4'
    st.title(':blue[Airbnb]')
    col1,col2=st.columns([2,1])

    with col2:
            st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnY5bXJ4ZTV3NW1ndWVmNHQzZm5vaDNhZzRpN2tuYm1weGptaTFiZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/geSnRnLiLYKUbQ8ODK/giphy.gif",use_column_width=True)

    with col1:
        st.write(' ')
        st.subheader(':blue[Welcome to the Airbnb Explorer!]')
        st.markdown(':orange[Embark on Your Journey with us]')
        df_Country=pd.read_sql_query('''SELECT DISTINCT Country from airbnb.hotels_info''',con=engine)
        selected_country= st.selectbox("Search destinations",options=df_Country['Country'].tolist(),index=None)
        st.write(' ')

        df_street=pd.read_sql_query('''SELECT DISTINCT Street from airbnb.hotels_info WHERE country =%s''',
                                    con=engine,params=[(selected_country,)])
        selected_street= st.selectbox("Select Street",options=df_street['Street'].tolist(),index=None)
        st.write(' ')

        df_hotels=pd.read_sql_query('''SELECT DISTINCT Name from airbnb.hotels_info WHERE street =%s''',
                                    con=engine,params=[(selected_street,)])
        selected_Hotel=st.selectbox('Select Hotel',options=df_hotels['Name'].tolist(),index=None)


        st.write("Selected Accommodation:", f"<span style='color:#F8CD47'>{selected_Hotel}</span>", unsafe_allow_html=True)

    if selected_Hotel:
            more=st.button('Click for Details')

                
            df=pd.read_sql_query('''SELECT Name,Listing_url,Description,Country,Price,Images,Property_Type,Room_Type,Amenities,
                                            Host_Name,Host_about,Host_location,Overall_score,Rating,Number_of_review
                                            from hotels_info
                                            join rooms_info on hotels_info.id=rooms_info.id
                                            JOIN hosts_info on hotels_info.id = hosts_info.id
                                            join reviews_info on hotels_info.id = reviews_info.id
                                            where Name= %s ''',con=engine,params=[(selected_Hotel,)])
                    
            extract_detail = df.to_dict(orient='records')[0] 

            c1,c2=st.columns(2)
            with c1:
                        st.write('**:green[Basic Details]**')
                        st.write("**:violet[Name :]**", f'**{extract_detail['Name']}**')
                        st.write("**:violet[Website Url :]**",extract_detail['Listing_url'])
                        st.write("**:violet[country :]**",f'**{extract_detail['Country']}**')
                        st.write("**:violet[Description :]**",f'**{extract_detail['Description']}**')
                        st.write("**:violet[Price in $ :]**",f'**{extract_detail['Price']}**')
                        st.write("**:violet[Total Reviews :]**",f'**{extract_detail['Number_of_review']}**')
                        st.write("**:violet[Overall Score:]**", f"**{extract_detail['Overall_score']} &nbsp;&nbsp;&nbsp; **:violet[Rating:]** {extract_detail['Rating']}**")
                        st.write("**:violet[Room Picture :]**")
                        st.image(extract_detail['Images'],width=300)

            with c2:
                        st.write('**:green[Room Details]**')
                        st.write("**:violet[Property Type :]**",f'**{extract_detail['Property_Type']}**')
                        st.write("**:violet[Room Type :]**",f'**{extract_detail['Room_Type']}**')
                        st.write("**:violet[Amenities :]**",f'**{extract_detail['Amenities']}**')
                        st.write('**:green[Host Details]**')
                        st.write("**:violet[Host Name :]**",f'**{extract_detail['Host_Name']}**')
                        st.write("**:violet[Host location :]**",f'**{extract_detail['Host_location']}**')
                        st.write("**:violet[Host About :]**",f'**{extract_detail['Host_about']}**')

                        
                        