import plotly.graph_objects as go
import plotly.express as px
import array as arr

cars = ["Ford", "Volvo", "BMW"] 
teste = [1, 2 , 3],
x_val = arr.array('i', [10,15, 20, 150, 22, 80, 66]),
y_val = [10,15, 20, 150, 80, 17, 37],
y_value = [20,30],
 
f_node_trace = go.Scatter(
        x=[ 250 , 250], y = [250 ,250],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            reversescale=True,
            size=25,
            line_width=2))

s_node_trace = go.Scatter(
        x=[ 0 , 500], y = [0 ,500],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            reversescale=True,
            size=25,
            line_width=2))
          
f_node_trace.text = cars

edge_trace = go.Scatter(
        x=[10,15], y=[0,5],
        line=dict(width=1, color='magenta'),
        hoverinfo='none',
        mode='lines')


fig = go.Figure(data=[f_node_trace, s_node_trace, edge_trace],layout=go.Layout(
   title='<b>'+"Artistas Relacionados"+'</b>',
     titlefont_size=16,
    margin=dict(b=20, l=5, r=5, t=40), 

    
))


fig.show()