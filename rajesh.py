import streamlit as st
st.write('puppy')
st.header('puppy')
st.image('https://i.pinimg.com/564x/36/b4/ef/36b4ef433ac9c2cf9d34e54aa3a38340.jpg', caption = 'puppy already sold')
audio_file = open('https://drive.google.com/file/d/112QHrmuhyIKrpsPE_fGl_ZR4xx7OLUA0/view?usp=drive_link', 'rb').read()
st.audio(audio_file, format='audio/mp3')
