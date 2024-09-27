import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# dataset dari URL
path_to_local_csv = './df_jam_analisis.csv'
df = pd.read_csv(path_to_local_csv)

image_path = './BikeSharing.jpg'  

# Display the logo in the sidebar above the filter options
st.sidebar.image(image_path, use_column_width=True)

st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Season", df['season'].unique())
selected_weather = st.sidebar.selectbox("Weather Condition", df['weather_condition'].unique())
selected_temp_group = st.sidebar.selectbox("Temperature Group", df['temp_group'].unique())

# Main page content
st.title("Bike Sharing Data Analysis")
st.header("Overview of Bike Sharing Usage")

st.subheader("Key Metrics")
total_users = df['count'].sum()
average_temp = df['temp'].mean()
total_casual = df['casual'].sum()
total_registered = df['registered'].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Users", f"{total_users:,}")
col2.metric("Average Temperature", f"{average_temp:.2f}")
col3.metric("Total Casual Users", f"{total_casual:,}")
col4.metric("Total Registered Users", f"{total_registered:,}")

filtered_data = df[(df['season'] == selected_season) &
                   (df['weather_condition'] == selected_weather) &
                   (df['temp_group'] == selected_temp_group)]

st.subheader(f"Hourly Bike Rentals - {selected_season} ({selected_weather}, {selected_temp_group})")
hourly_rentals = filtered_data.groupby('hour')['count'].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(hourly_rentals['hour'], hourly_rentals['count'], marker='o')
plt.title('Average Hourly Bike Rentals')
plt.xlabel('Hour')
plt.ylabel('Average Rentals')
st.pyplot(plt)

st.subheader("Rentals by Season and Weather Condition")
rentals_by_season_weather = df.groupby(['season', 'weather_condition'])['count'].sum().unstack()

plt.figure(figsize=(10, 6))
rentals_by_season_weather.plot(kind='bar', stacked=True)
plt.title('Bike Rentals by Season and Weather Condition')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt)

st.subheader("User Type Distribution (Casual vs Registered)")
user_type_data = [total_casual, total_registered]
labels = ['Casual Users', 'Registered Users']

plt.figure(figsize=(6, 6))
plt.pie(user_type_data, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.axis('equal')  
plt.title('User Type Distribution')
st.pyplot(plt)

st.subheader("Correlation Heatmap")
corr = df[['temp', 'hum', 'casual', 'registered', 'count']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Variables')
st.pyplot(plt)

if st.sidebar.checkbox("Show filtered data", False):
    st.subheader("Filtered Data")
    st.write(filtered_data)
