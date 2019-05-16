# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
search1 = search.breadth_first_graph_search(ab)
search2 = search.depth_first_graph_search(ab)
search3 = search.ram_and_cut_graph_search(ab)
search4 = search.ram_and_cut_h_graph_search(ab)
print("Breadth:", search1[0].path(), "El numero de nodos expandidos es:", search1[1])
print("Depth:", search2[0].path(), "El numero de nodos expandidos es:", search2[1])
print("Ramificacion + cut:", search3[0].path(), "El numero de nodos expandidos es:", search3[1])
print("Ramificacion + cut + heu:", search4[0].path(), "El numero de nodos expandidos es:", search4[1])

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
