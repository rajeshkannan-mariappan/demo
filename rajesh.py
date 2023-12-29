pip install gdown
import streamlit as st
import gdown
st.write('puppy')
st.header('puppy')
st.image('https://i.pinimg.com/564x/36/b4/ef/36b4ef433ac9c2cf9d34e54aa3a38340.jpg', caption = 'puppy already sold')
file_id = '112QHrmuhyIKrpsPE_fGl_ZR4xx7OLUA0'
url = f'https://drive.google.com/uc?id={file_id}'
output = './myaudio.mp3'  # Replace with your desired local path and filename
gdown.download(url, output, quiet=False)
audio_file = open('./myaudio.mp3', 'rb').read()
st.audio(audio_file, format='audio/mp3')
