
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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
   
streamlit.header("Fruityvice Fruit Advice!!!!")
import requests
from urllib.error import URLError
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   streamlit.write('The user entered ', fruit_choice)
   if not fruit_choice:
        streamlit.error("Please select the fruit to get information")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()



streamlit.stop()
import pandas
import requests
import snowflake.connector

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()
if streamlit.button('Get Fruit Load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)



add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('The user entered ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")



