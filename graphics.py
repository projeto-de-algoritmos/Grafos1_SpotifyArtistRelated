import plotly.graph_objects as go
import plotly.express as px


node_trace = go.Scatter(
        x=[10,15, 20], y=[10,15, 20],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            reversescale=True,
            size=20,
            line_width=2))
          
edge_trace = go.Scatter(
        x=[10,15], y=[10,15],
        line=dict(width=1, color='magenta'),
        hoverinfo='none',
        mode='lines')



fig = go.Figure(data=[node_trace, edge_trace],layout=go.Layout(
   title='<b>'+"Artistas Relacionados"+'</b>',
     titlefont_size=16,
    margin=dict(b=20, l=5, r=5, t=40), 

    
))


fig.show()