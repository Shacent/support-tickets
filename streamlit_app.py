import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from supabase import create_client, Client
from sqlalchemy import create_engine

SUPABASE_DATABASE_URL = (
    "postgresql://postgres.pjehdrugpzsjqwcmxsmg:yJ17Elq905YI6ij3@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
)

# Create SQLAlchemy engine for connecting to the database
engine = create_engine(SUPABASE_DATABASE_URL)

# Use a SQL query to fetch the data from the 'Villa' table
# Ensure the column names match the actual database column names
query = 'SELECT "Silahkan Isi Data Anda !", "Kelas", "Submission ID" FROM villa'
df = pd.read_sql(query, con=engine.connect())

# Show app title and description.
st.set_page_config(page_title="Support tickets", page_icon="🎫")
st.title("🏠Villanations V3🏠")
st.write(
    """
    Berikut data nama-nama yang sudah mendaftar Villanations Labti V3.
    """
)

# Create a random Pandas dataframe with existing tickets.
if "df" not in st.session_state:

    # Save the dataframe in session state (a dictionary-like object that persists across
    # page runs). This ensures our data is persisted when the app updates.
    st.dataframe(df,use_container_width=True)

    st.write("Total Data yang masuk: ",df.shape[0])
