import streamlit as st

st.title('Rio Eats')

with st.sidebar:
  st.header('Rio Eats')
  st.write('Seu aplicativo da dicas para restaurantes')
  st.caption('Criado por Luana P. Silva')

st.write('Mosso aplicativo tem o foco de oferecer os restaurantes mais próximos perto de você ')
tab_corrida, tab_nutri, tab_news = st.tabs(["Corrida de Rua", "Nutrição", "Notícias"])

st.image('rio eats.jpg')
