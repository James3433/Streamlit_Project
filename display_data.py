import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


st.set_page_config(page_title='Dataset',layout= 'wide')

# Load the dataset
dataset1 = pd.read_csv('White Corn Price.csv')
dataset2 = pd.read_csv('Yellow Corn Price.csv')

# Title of the web app
st.title('Corn Price in the Phillipines')

# Create two columns
col1, col2, col3, spacer = st.columns([1, 1, 1, 1])
# Display the dataframe in the first column
with col1:
    st.dataframe(dataset1)
# Display the second dataframe in the second column
with col2:
    st.dataframe(dataset2)
# Display the barchart
with col3:
    month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    selected_month = st.selectbox('Select a month', month_order)

    selected_year = int(st.selectbox('Select a year', ['2018', '2019', '2020'], key='year_selector_1'))

  
    dataset_select1 = dataset1[(dataset1['Year'] == selected_year) & (dataset1['Month'] == selected_month)]
    dataset_select2 = dataset2[(dataset2['Year'] == selected_year) & (dataset2['Month'] == selected_month)]
    
    # Find the minimum and maximum prices for setting y-ticks and y-axis limit
    min_price = dataset_select1['Price'].min()
    max_price = dataset_select1['Price'].max()

    # Create bar plot
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x='Week #', y='Price', data=dataset_select1, ax=ax)
    ax.set_title(f'Price of White Corn in {selected_month} {selected_year}')
    ax.set_xlabel('Week')
    ax.set_ylabel('Price')
    ax.set_ylim(min_price - 0.1, max_price + (max_price - min_price) * 0.1)
    for tick in ax.get_xticklabels():
        tick.set_fontsize(8)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(8)
        
    # Save the plot to a temporary file
    plt.savefig('temp_1.png')
        
    # Display the plot in Streamlit
    st.image('temp_1.png', width=460)  # Adjust the plot width

    min_price2 = dataset_select2['Price'].min()
    max_price2 = dataset_select2['Price'].max()

     # Create bar plot
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x='Week #', y='Price', data=dataset_select2, ax=ax)
    ax.set_title(f'Price of Yellow Corn in {selected_month} {selected_year}')
    ax.set_xlabel('Week')
    ax.set_ylabel('Price')
    ax.set_ylim(min_price2 - 0.1, max_price2 + (max_price2 - min_price2) * 0.1)
    for tick in ax.get_xticklabels():
        tick.set_fontsize(8)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(8)
        
    # Save the plot to a temporary file
    plt.savefig('temp_2.png')
        
    # Display the plot in Streamlit
    st.image('temp_2.png', width=460)  # Adjust the plot width




# Create a choice box for selecting the dataset
selected_dataset = st.selectbox('Select a dataset', ['White Corn Price', 'Yellow Corn Price'])

# Group the data by year
if selected_dataset == 'White Corn Price':
    grouped = dataset1.groupby('Year')
    dataset = dataset1
else:
    grouped = dataset2.groupby('Year')
    dataset = dataset2


# Set the font size
matplotlib.rcParams.update({'font.size': 8})

# Create two columns
col1, spacer, col2 = st.columns([0.5, 1, 1])
with col1:
# Create a plot for each year
    for year, group in grouped:
        fig, ax = plt.subplots(figsize=(10, 4))  
        ax.plot(group['Month'], group['Price'], marker='o', markersize=4)  
        ax.set_title(f'{selected_dataset} for Year {year}', fontsize=8)
        
        # Adjust the font size for the x and y tick labels
        for tick in ax.get_xticklabels():
            tick.set_fontsize(8)
        for tick in ax.get_yticklabels():
            tick.set_fontsize(8)
        
        # Save the plot to a temporary file
        plt.savefig('temp.png')
        
        # Display the plot in Streamlit
        st.image('temp.png', width=550)  # Adjust the plot width

with col2:
    # Define the month order
    month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    # Create a choice box for selecting the year
    selected_year1 = int(st.selectbox('Select a year', ['2018', '2019', '2020'], key='year_selector_2'))

    dataset_year = dataset[dataset['Year'] == selected_year1]

    # Convert the 'Month' column to a categorical type with the specified order
    dataset_year['Month'] = pd.Categorical(dataset_year['Month'], categories=month_order, ordered=True)

    grouped = dataset_year.groupby('Month')

    with st.expander(f"Price plots for the year {selected_year1}", expanded=True):
        for month, group in grouped:
            fig, ax = plt.subplots(figsize=(6, 4))  
            ax.plot(group['Week #'], group['Price'], marker='o', markersize=4)
                
            ax.set_xlabel('Month')
            ax.set_ylabel('Price')
            ax.set_title(f'Price by {month} for {selected_year1}')
                
            # Adjust the font size
            for tick in ax.get_xticklabels():
                tick.set_fontsize(8)
            for tick in ax.get_yticklabels():
                tick.set_fontsize(8)
                
            # Save the plot to a temporary file
            plt.savefig('temp1.png')
                
            # Display the plot in Streamlit
            st.image('temp1.png', width=350)

