# Plot a scatter plot graph on the Covid data for different countries.

import pandas as pd 
import plotly.express as px 

df = pd.read_csv("dataFrame.csv")

#Line grpah 
#fig = px.line(df , x="Country", y="Population")

#Bar graph 
#fig = px.bar(df,x="Country", y="InternetUsers")

graph = px.scatter(df,x="date",y="cases" ,color="country", size_max=60)

graph.show()