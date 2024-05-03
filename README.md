1. We start by importing the necessary libraries, pandas for data manipulation and matplotlib.pyplot for plotting.
2. We load the dataset from the World Bank using the provided Dataset.
3. For categorical data, There is a column named 'Country Name' in the dataset. We use value_counts() to count the occurrences of each country and then plot a bar chart to visualize the distribution.
4. For continuous data, we assume there is a column named 'Indicator Name'. We create a pie show the distribution of Male Population with specified bins, color, and edge color.
5. Finally, we add labels to the axes and a title to each plot for better understanding and visualization.
