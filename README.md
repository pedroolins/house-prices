# Projeto de análise de imóveis e predição do preço de compra (Problema de regressão)
![bandeira](https://blog.faspec.edu.br/wp-content/uploads/2019/12/realtor-3261160_640-1.jpg)
# Observações importantes sobre o projeto:
* **Com o objetivo de simular um cenário real de um projeto de ciência de dados dentro de uma empresa, o contexto de negócio deste projeto é fictício, ou seja a empresa Beautiful Houses e o CEO da mesma não existem realmente.**
# Problema de negócio do proejto:
* O problema de negócio deste projeto vem a partir da empresa Beautiful Houses, que tem como modelo de negócio a compra, reforma e venda de imóveis. Portanto a mesma vem sofrendo de um sério problema, que é pagar um valor ideal e justo na compra imóveis a partir de suas determinadas características (área, n° de banheiros e etc..), afinal niguém gosta de saber que investiu um valor alto demais na compra de um imóvel que não vale o valor investido, principalmente uma empresa que tem a compra e venda de imóveis como modelo de negócio. Dessa forma, quanto mais a organização comprar imóveis pelo seu valor ideal de mercado, mais lucro ela irá obter posteriormente na venda deste imóvel.  
--------------------------------------------------------------------------------------------------------------------------------
* CEO da empresa Beautiful Houses disponibilizou um conjunto de dados para mim, o cientista de dados da empresa, e ordenou a criação de um relatório de análise de imóveis para responder a seguintes perguntas feitas por ele: 

  1. *Qual seria o preço de compra ideal de um imóvel a partir de determinadas características?*
  3. *Quais características do imóvel mais interferem no valor de compra do mesmo?*
  4. *Imóveis localizados em zona residêncial com baixa densidade apresentam, em sua maioria, valor de compra mais elevados que os imóveis localizados em zonas de média densidade?*
# Descrição das variáveis do conjunto de dados:
* Zona: Classificação da zona de venda
		
       RL	Zona residencial de baixa densidade
       RM	Zona residencial de média densidade

* Area: Tamanho do terreno (pés quadrados)

* Qualidade: Qualidade do material e acabamento do imóvel

* AnoConstrucao: Data de construção

* QualidadeAquecimento: Qualidade do sistema de aquecimento

       Ex	Excelente
       Gd	Bom
       TA	Mediano
       Fa	Aceitável

* Banheiros: Banheiros

* Quartos_t1: Quartos tipo 1

* Quartos_t2: Quartos tipo 2
      	
* Comodos: Total de cômodos
		
* Lareiras: Quantidade de lareiras
		
* Garagem: Tamanho da garagem em termos de quantidade de carros

* Preco: Preço de venda do imóvel em dólar

# Definição do Baseline (Como a empresa resolve o problema atualmente):

* **Atualmente a empresa beautiful Houses precifica os imóveis através de uma média dos preços do mercado e muitas vezes através da própria intuição do CEO da empresa e do time de negócio**
* **Nosso papel como Cientista de dados da empresa, é melhorar a forma como ela vem lidando com o problema atualmente, com isso irei criar um modelo de machine learning baseado em regressão linear múltipla para precificar os imóveis através de suas características (Área, n° de banheiros e etc..).**

# Planejamento da solução:
1. Carregar o conjunto de dados.
2. Observar a dimensão do conjunto de dados.
3. Observar possíveis dados faltantes.
4. Observar os tipos de dados.
5. Análise exploratória de dados:
 * **Validar ou rejeitar hipóteses:**
     * Imóveis que foram construídos mais recentemente tendem a ser mais caros?
     * Imóveis com maior quantidade de banheiros tendem a ser mais caros?
     * Imóveis com maior qualidade de aquecimento tendem a ser mais caros?
     * Imóveis com menor área tendem a ter um valor de compra menor?  
     * Imóveis com lareiras tendem a apresentar umn preço de compra mais elevado?
     * Imóveis com maior quantidade de vagas na garagem tendem a apresentar valores de compra mais elevado?
     * Imóveis localizados em áreas de média densidade tendem a apresentar valores de compra mais elevado?
     * Imóveis com maior quantidade de cômodos tendem a ter um valor de compra mais elevado?
     * Imóveis com maior nível de qualidade de acabamento possuem preço de compra mais elevado?
 * **Extrair insights;**
6. Analisando as correlações entre as variáveis. 
7. Preparar os dados para estimar um modelo de regressão linear múltipla que através das características do imóvel consiga retornar o valor ideal de compra do mesmo.
8. Estimar o modelo de regressão lienar múltipla
9. Responder as perguntas do CEO:
     * **Qual seria o preço de compra ideal de um imóvel a partir de suas determinadas características?**
         * área = 10920 (pés quadrados) 
         * Nível de qualidade de acabamento = 7
         * Ano de construção = 1978
         * N° de banheiros = 1
         * N° de cômodos = 6
         * N° de lareiras = 3
         * N° de vagas na garagem = 1
         * Imóvel em Zona residência de baixa densidade
     * **Quais caractéristicas do imóvel mais interferem no valor de compra do mesmo?**
     * **Imóveis localizados em zona residêncial com baixa densidade apresentam, em sua maioria, valor de compra mais elevados que os de média densidade?**
10. Conclusôes
