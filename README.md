# Airbnb-Analysis-using-Streamlit-and-Plotly


# Airbnb Analiysis Using Streamlit and Plotly

## Introduction for Airbnb:
Airbnb is an online marketplace that connects travelers with local hosts who offer unique accommodations and experiences. Founded in 2008, Airbnb has grown into a global platform with millions of listings in over 220 countries and regions.
### Key Features of Airbnb:
    - **Accommodations**: Airbnb offers a wide range of accommodations, including apartments, houses, villas, and unique properties like treehouses and yurts.
    - **Experiences**: In addition to lodging, Airbnb hosts can offer experiences such as guided tours, cooking classes, and outdoor adventures.
    - **Host Program**: Individuals can become Airbnb hosts by listing their properties or experiences on the platform, allowing them to earn income and connect with travelers.
    - **Reviews and Ratings**: Airbnb incorporates a review system where guests and hosts can leave feedback, helping to build trust and transparency within the community.
### About the Dataset:
    You have Airbnb 2018 data, which includes information about listings, hosts, reviews, and other relevant details. This dataset can provide insights into the types of accommodations available, pricing trends, and popular destinations during the year 2018.

## Deployment

To deploy this project streamlit run main.py

## Pip install
pip install pandas,streamlit,streamlit_option_menu,mysql-connector-python,matpllotlib,seaborn,plotly
## Libraries
import os
import json
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu



## Appendix

Get the data from the link:https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view

## Data Extraction

## Data Extract:
     Get a data from airbnb JSON 2018 data.I extract hotel info,room info,review info host info.
## Data Cleaning:
    - Checking the Null Values and replace it with 0
    - Checking the data type and change responsible to it.

## Sql"
    Transfer the data to Sql Database.

## Data Analysis:
    Data nalysis have been done using plotly,matplotlib,seaborn

## Challenges faced:
    **Data Quality and Completeness**:
    1.    - **Missing Values**: Many datasets have missing values, which can complicate analysis and require imputation or exclusion techniques.
        - **Inconsistent Data**: Variations in data entry, such as different formats for dates or addresses, can lead to inconsistencies that need cleaning.

    2. **Data Volume and Complexity**:
        - **Large Datasets**: Airbnb datasets can be large, containing millions of rows, which can make data processing and analysis computationally intensive.
        - **Complex Relationships**: The data often includes complex relationships between hosts, listings, reviews, and bookings, requiring advanced data modeling techniques.

    3. **Geospatial Analysis**:
        - **Location Data**: Analyzing geographic data involves working with coordinates, mapping tools, and geospatial libraries, which can be technically challenging.
        - **Regional Differences**: Listings in different regions can vary widely in terms of availability, pricing, and regulations, complicating cross-regional analysis.


## Work flow:
    - Creating streamlit page by the method of streamlit multiapp method and done having five pages with that one which contain main function about all the pages.
    -secondly,about the airbnb-Introduction.
    -Third contain Exploration of Airbnb data.
    -Fourth page contains Geo Visualizatiom of Hotels.
    -Fifth page contains Data analysis in various methods.
    -Also had ipynb file which contains data extraction and sql part


## Demo Link:
https://www.linkedin.com/posts/shanthini-tamilselvan-2a0a102b6_my-next-project-demo-airbnb-analysis-using-activity-7198291143468486657-dGMb?utm_source=share&utm_medium=member_desktop



