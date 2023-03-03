# Troubleshooting Streamlit
# pip install --upgrade streamlit
# pip install --upgrade streamlit==1.11.1
# pip install pydeck==0.7.1
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import time
from datetime import datetime
from io import StringIO
import pickle

st.markdown("""# Example Page.
This page will include sample code for elements in a Streamlit app.""")

st.markdown("# Text Elements")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write("Standard text")

# Markdown Equivalent
st.markdown("""# Title
## Header
### Subheader
Standard text""")

st.caption("Caption")
st.code("""Sample Code
print('Hello World')
a = 1234""")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


#  Displaying Data
df = pd.DataFrame(
   np.random.randn(30, 20),
   columns=('col %d' % i for i in range(20)))

json = {"fun": "ok", "interesting": "very", "knowledge": "breathtaking", "review": ["best experience", "rate it out of 10", 13]}

st.dataframe(df)  # Same as st.write(df)
st.table(df) # will show all the rows of data
st.json(json)

st.markdown("## Chart elements")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [30, 20] + [1.3521, 103.8198],
    columns=['lat', 'lon'])

st.markdown("## Line Chart")
st.line_chart(chart_data)

st.markdown("## 2D Map")
st.map(map_df)

st.markdown("## 3D Map")
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=1.3521,
        longitude=103.8198,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=map_df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=map_df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

st.markdown("## Graph")
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

st.markdown("# Caching")
@st.cache # updated to cache_data in streamlit 1.12.0
def fetch_data(url):
    time.sleep(3)
    return pd.DataFrame(
        np.random.randn(5, 3),
        columns=['a', 'b', 'c'])

@st.cache
def transform(df):
    time.sleep(3)
    df = df.filter(items=['a', 'c'])
    return df

@st.cache 
def load_model():
    time.sleep(3)
    with open('../deploymentWorkshopModel.pkl', 'rb') as model:
        model = pickle.load(model)
    return model

if st.checkbox("Fetch Data - www.google.com"):
    data = fetch_data("https://www.google.com")
    st.write(data)

if st.checkbox("Fetch Data - www.bing.com"):
    data = fetch_data("https://www.bing.com")
    st.write(data)

if st.checkbox("Transform Data"):
    data = transform(data)
    st.write(data)    

if st.checkbox("Load Model"):
    model = load_model()
    st.write(model)

st.markdown("# Input Elements")

st.markdown("## Button")
if st.button('Click me', help='click me if you dare'):
    st.write('Wake Up!')
else:
    st.write('Hello there!')

st.markdown("## Image Capture")
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))

st.markdown("## Radio Buttons")
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

genre = st.radio(
    "What\'s your favorite movie genre!",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You are not funny.")

st.markdown("## Drop down Menu")
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.markdown("## Mutli Select")
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.markdown("## Slider")
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

start_time = st.slider(
    "Choose a starting date.",
    value=datetime(2023, 3, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.markdown("## Date Time")
d = st.date_input(
    "When\'s your birthday")
st.write('Your birthday is:', d)

st.markdown("## Text Input")
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.markdown("## Text Area")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
''')

st.markdown("## Number Input")
number = st.number_input('Insert a number', min_value=1, max_value=10, value=5, step=1)
st.write('The current number is ', number)

st.markdown("## Time Input")
t = st.time_input('Set an alarm for')
st.write('Alarm is set for', t)

st.markdown("## File Uploader")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

st.markdown("# Message Boxes")
st.info("This is a purely informational message")
st.success("This is a success message!")
st.exception("NameError('Error name is not defined')")
st.warning("This is a warning message")
st.error("This is an error message")

st.markdown("# ALL DONE")
if st.button('Done'):
    st.balloons()
    st.snow()