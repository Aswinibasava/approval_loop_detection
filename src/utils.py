import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def detect_loops(df: pd.DataFrame):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['Approver'], row['Requestor'], tid=row['Transaction ID'])

    loops = list(nx.simple_cycles(G))
    return [loop for loop in loops if len(loop) > 1]

def visualize_graph(df: pd.DataFrame):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(row['Approver'], row['Requestor'])

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", arrows=True)
    return plt
