# OSPF search algorithm

OSPF(Open Shortest Path First) is using Dijkstra’s algorithm to find the 
shortest path to the next router, and the heuristic in networking isn’t the physical 
distance between the two routers but it’s the data transmition rate if “daterate1”
is more than “datarate2” that means the path to the router that has “datarate1”
is shorter than the path to the router that has “datarate2”.
