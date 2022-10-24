import pandas as pd
import sqlite3 as sql

# read in csv as pandas dataframe
listings_df = pd.read_csv('listings.csv')

# create sql connection
conn = sql.connect('listings.db')

# save dataframe to sql file
listings_df.to_sql('listings', conn)

# commit the changes and close connection
conn.commit()
conn.close()
