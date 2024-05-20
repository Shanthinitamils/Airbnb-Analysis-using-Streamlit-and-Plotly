import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import mysql.connector

def app():
 

    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor(buffered=True,)

    #create a engine to insert data value
    engine = create_engine("mysql+mysqlconnector://root:@localhost/airbnb") 

    #create database and use for table creation
    mycursor.execute('create database if not exists airbnb')
    mycursor.execute('use airbnb')

    st.subheader(":red[Explore Accommodation by Country]")

    df_Country=pd.read_sql_query('''SELECT DISTINCT Country from hotels_info''',con=engine)
    selected_country= st.selectbox("select Country",options=df_Country['Country'].tolist(),index=None)

    if selected_country:
        on=st.toggle('switch to view')

        if on:
            
            df=pd.read_sql_query('''  SELECT Name as 'HotelName', Longitude, Latitude  FROM hotels_info
                                where Country = %s  ''',con=engine,params=[(selected_country,)])
            
            df[['Longitude','Latitude']]=df[['Longitude','Latitude']].astype('float')
            
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                                    zoom=10,hover_name='HotelName',
                                    color_discrete_sequence=px.colors.colorbrewer.Blues_r)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig,use_container_width=True)