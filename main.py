import streamlit as st
import time
import pandas as pd
import numpy as np
import random
from datetime import datetime, date
import folium
from streamlit_folium import st_folium


st.title("Streamlitの基礎")
st.write("Hello World")

col1, col2 = st.columns(2)
with col1:
    st.write("列1がここに表示されます")
with col2:
    st.write("列2がここに表示されます")

st.sidebar.write("Hello World")
st.text_input("ここに文字が入力できます。")

slider_text = st.slider("スライダーで数字を決定できます。", 0, 100, 5)
st.write("スライダーの数字:", slider_text)

st.button("ボタン")

x = st.empty()
bar = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    x.text(f"進捗: {i + 1}%")
    bar.progress(i + 1)

st.selectbox("選んでください。", ["選択肢1", "選択肢2", "選択肢3"])

output_text = "この文字がダウンロードされます"
st.download_button(label='記事内容 Download', data=output_text, file_name='out_put.txt', mime='text/plain')

file_upload = st.file_uploader("ここに画像をアップロードしてください。", type=["png", "jpg"])
if file_upload is not None:
    st.image(file_upload)

def rand_df(r=10, c=5):
    df = pd.DataFrame(np.random.randn(r, c), columns=("col %d" % i for i in range(c)))
    return df

dataframe = rand_df(r=10, c=3)
st.dataframe(dataframe.head(n=3))
st.line_chart(dataframe)

df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [33.3193, 130.5086], columns=["lat", "lon"])
st.map(df)

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.slider("Rate this:", 1, 5, 3)
st.markdown(f"You selected {sentiment_mapping[selected-1]} star(s).")

st.markdown("🆕 New!")
st.success("Success")

d = st.date_input("When's your birthday", date(2019, 7, 6))
st.write("Your birthday is:", d)

try:
    with open("myvideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)
except FileNotFoundError:
    st.warning("動画ファイルが見つかりません")

col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.balloons()

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg", caption="Streamlit Gallery")

with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

st.title("Homework")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")


# center on Liberty Bell, add marker
m = folium.Map(location=[33.3193, 130.5086], zoom_start=16)
folium.Marker(
    [33.3193, 130.5086], popup="久留米市", tooltip="久留米市"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

data_df = pd.DataFrame(
    {
        "appointment": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "appointment": st.column_config.DatetimeColumn(
            "Appointment",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
    },
    hide_index=True,
)

data_df = pd.DataFrame(
    {
        "apps": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "apps": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    hide_index=True,
)

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"AI: {prompt}")

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)


options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)