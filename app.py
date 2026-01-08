import streamlit as st 
from backend import get_connection, daily_rentals_by_store, total_revenue_by_store, top_five_by_store
from matplotlib import pylab as plt 


def main():
    # Home section
    st.title("Sakila Video Rental Dashboard")
    st.image("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800")

    #EDA section

    st.header("Daily Rentals by Store: 2005")
    daily_rentals = daily_rentals_by_store()  # This IS a DataFrame

    # Split the data by store
    store_1 = daily_rentals[daily_rentals['Store ID'] == 1]
    store_2 = daily_rentals[daily_rentals['Store ID'] == 2]
    store_1 = store_1.sort_values('Rental Date')
    store_2 = store_2.sort_values('Rental Date')

    # Plot both lines
    plt.figure(figsize=(10, 10))
    plt.plot(store_1['Rental Date'], store_1['Rental Count'], label='Store 1', color='#FF6B6B')
    plt.plot(store_2['Rental Date'], store_2['Rental Count'], label='Store 2', color='#4ECDC4')
    plt.title("Daily Rentals By Store: 2005")
    st.pyplot(plt)

    st.header("Total Revenue by Store: 2005")
    # bar plot 
    total_revenue = total_revenue_by_store() # create the dataframe
    plt.figure(figsize=(10, 7))
    plt.bar(total_revenue["Store ID"].astype(str), total_revenue["Total Revenue Per Store"], color=['#FF6B6B', '#4ECDC4'], edgecolor='black', linewidth=1.5)
    plt.title("Total Revenue by Store: 2005")
    plt.xlabel('Store')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)


    st.header("Top 5 Movie Rentals by Store")
    top_5 = top_five_by_store()
    st.dataframe(top_5)

    st.header("Search")
    # text and input 



if __name__ == '__main__':
    main()