# código do Web app do projeto de predição do preço de casas
# bibliotecas 
import streamlit as st
import pickle
import numpy as np
import os
import sklearn

# Cabeçalho do Web app
st.header('Web App: Predição do preço de imóveis da Beautiful Houses')
st.subheader('Construído em python')
st.markdown('Insira as informações para obter a previsão do modelo')

# Corpo do Web app

# área do imóvel 
area = st.slider('Qual a área do imóvel (pés quadrados):', min_value = 500, max_value = 19900)
st.write(area)

# nível de qualidade do acabamento do imóvel
nivel_qualidade = st.slider('Qual o nível de qualidade de acabamento do imóvel:', min_value = 1, max_value = 8)
st.write(nivel_qualidade)

# Ano de construção
ano_construcao = st.slider('Qual o ano de construção do imóvel:', min_value = 1940, max_value = 2021)
st.write(ano_construcao)

#N° de banheiros
banheiros = st.slider('Qual o n° de banheiros do imóvel:', min_value = 1, max_value = 5)
st.write(banheiros)

#N° de cômodos
comodos = st.slider('Qual o n° de cômodos do imóvel:', min_value = 1, max_value = 8)
st.write(comodos)

#N° de lareiras
lareiras =  st.slider('Qual o n° de lareiras do imóvel:', min_value = 0, max_value = 3)
st.write(lareiras)

# N° de vagas na garagem 
garagem = st.slider('Qual o n° de vagas na garagem do imóvel:', min_value = 0, max_value = 3)
st.write(garagem)

# Zona residêncial do imóvel
opcoes = ['Zona residencial de baixa densidade', 'Zona residencial de média densidade']
zona = st.radio('Qual a zona residencial do imóvel:', options = opcoes)

# condicional da variável zona para poder entrar no modelo
if (zona == 'Zona residencial de baixa densidade'):
    zona = 0
else:
    zona = 1

# carregando modelo
# condicional para ver se o arquivo existe
if(os.path.exists('models/modelo_predição_imóveis.pkl')):
    # carregando o modelo preditivo na variável modelo
    arquivo_modelo = open('models/modelo_predição_imóveis.pkl', 'rb')
    modelo = pickle.load(arquivo_modelo)
    arquivo_modelo.close()
    butao = st.button('Efetuar predição do preço do imóvel')
    if(butao):
        entrada = np.array([[area,
                            nivel_qualidade,
                            ano_construcao,
                            banheiros,
                            comodos,
                            lareiras,
                            garagem,
                            zona]])
        preco = modelo.predict(entrada)
        st.write('O preço do imóvel está avaliado em: US$', preco.round(2)[0])
else:
    st.error('Erro ao carregar modelo preditivo\nPor favor, contate o administrador do sistema!')