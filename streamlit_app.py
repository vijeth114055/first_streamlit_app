
import streamlit
import pandas
streamlit.title("My parents breakfast menu")
streamlit.header("Breakfast Menu")
streamlit.text("🥣Bread omlette🍞 and Paneer sandwich")
streamlit.text("🥗Plain dosa and Sambar with 🥑flavoured rice")
streamlit.text("🐔Hard boiled eggs")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

