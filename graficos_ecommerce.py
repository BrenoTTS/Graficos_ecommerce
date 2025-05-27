from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

# Grafico de Dispersão
fig1 = px.scatter(df, x='Nota', y='Preço', color='Gênero', hover_data=['Marca'])
fig1.update_layout(
    title='Nota vs preço por marca',
    xaxis_title='Nota',
    yaxis_title='Preço'
)

# Grafico Histograma
fig2 = px.histogram(df, x='Preço', nbins=30, title='Distribuição de Preço')

# grafico de Pizza
fig3 = px.pie(df, names='Gênero', color='Gênero', hole=0.2, color_discrete_sequence=px.colors.sequential.Purp)

# Grafico Bolha
fig4 = px.scatter(df, x='Qtd_Vendidos_Cod', y='Preço', size='Nota', size_max=5, hover_name='Marca', color='Material')
fig4.update_layout(
    title='Quantidade Vendido pelo Preço',
    xaxis_title='Quantidade Vendidos',
    yaxis_title='Preço'
)

# Grafico 3d
fig5 = px.scatter_3d(df, x='Desconto', y='N_Avaliações', z='Preço', color='Gênero')


# Griar app
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5)
])

# Executar App
app.run(debug=True, port=8050) # porta padrão

