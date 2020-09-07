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
            size=30,
            line_width=0))

s_node_trace = go.Scatter(
        x=[ 325 , 250, 175, 200, 300], 
        y = [275 ,375, 275, 150, 150],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            reversescale=True,
            size=25,
            line_width=0))

t_node_trace = go.Scatter(
        x=[
        250, 275, 225, 287, 213,
        135, 145, 145, 160, 160,
        365, 355, 355, 340, 340,
        175, 175, 180, 190, 200,
        325, 325, 320, 310, 300,
        ], 
        y = [
        450, 425, 425, 400, 400,
        275, 250, 300, 225, 325,
        275, 250, 300, 225, 325,
        175, 150, 125, 100, 75,
        175, 150, 125, 100, 75,
        ],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            reversescale=True,
            size=15,
            line_width=0))
          
s_node_trace.text = cars

edge_trace = go.Scatter(
        x=[
        250,250, 250, 325, 250, 175, 250, 200, 250, 300,
        300, 325, 300, 325, 300, 320, 300, 310, 300, 300,
        ], y=[
        250,375, 250, 275, 250, 275, 250, 150, 250, 150,
        150, 150, 150, 175, 150, 125, 150, 100, 150, 75,
        ],
        line=dict(width=0.75, color='black'),
        hoverinfo='none',
        mode='lines')


fig = go.Figure(data=[f_node_trace, s_node_trace, t_node_trace, edge_trace],layout=go.Layout(
   title='<b>'+"Artistas Relacionados"+'</b>',
     titlefont_size=16,
    margin=dict(b=20, l=5, r=5, t=40), 

    
))


fig.show()