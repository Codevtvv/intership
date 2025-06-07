from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# 1. Connect and load the dataset
connect()
df = get_df("my_dataset")

# 2. Query: Get days with temperature above 20C
sql = "SELECT * FROM my_dataset WHERE temperature_c > 20"
filtered_df = query(sql, "my_dataset")

# 3. Interactive UI
text("# Weather Data Analysis")
table(filtered_df, title="Days with Temperature > 20°C")

# 4. Visualization: Temperature vs. Precipitation
fig = px.scatter(df, x="date", y="temperature_c", size="precipitation_mm", color="weather",
                 title="Temperature and Precipitation Over Time")
plotly(fig)
