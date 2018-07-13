import osmnx as ox
G = ox.graph_from_place('Toronto, Canada', network_type='drive')
ox.save_graph_shapefile(G, filename='torontoshp')
G_projected = ox.project_graph(G)
ax = ox.plot_graph(G_projected, save=True, file_format='svg')
