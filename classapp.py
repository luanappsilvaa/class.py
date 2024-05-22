import streamlit as st

st.title('Salut')

with st.sidebar:
  st.header('Salut')
  st.write('Seu aplicativo da dicas de saúde')
  st.caption('Criado por Luana P. Silva')

st.write('Mosso aplicativo tem o foco de oferever dicas sobre corrida, nutrição e motíciassaúde')
tab_corrida, tab_nutri, tab_news = st.tabs(["Corrida de Rua". "Nutrição", "Notícias])
