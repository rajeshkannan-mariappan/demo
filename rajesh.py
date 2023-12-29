import streamlit as st
st.write('puppy')
st.header('puppy')
st.image('https://i.pinimg.com/564x/36/b4/ef/36b4ef433ac9c2cf9d34e54aa3a38340.jpg', caption = 'puppy already sold')
audio_file = open('C:\Users\New\Desktop\test new\Mudhal Nee Mudivum Nee.mp3', 'rb').read()
st.audio(audio_file, format='audio/mp3')
