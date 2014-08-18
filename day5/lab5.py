"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  print G
  
# def makeLink(G, node1, node2):
#   if node1 not in G:
#     G[node1] = {}
#   (G[node1])[node2] = 1
#   if node2 not in G:
#     G[node2] = {}
#   (G[node2])[node1] = 1
#   return G 

# makeLink({}, "WashU", "FP")

# Ring Network

# empty graph 

# n = 4 # number of nodes 

# Add in edges
# for i in range(n):
#   ring = makeLink(ring, i, (i+1))

# def recursive_test(passed1, passed2): 
# 	
# 	ring = {}
# 	
# 	bottom = passed1
# 	top = passed2
# 	
# 	vertical1 = passed1
# 	vertical2 = passed2
# 	
# 	
# 	for i in range(0, 15):
# 		for i in range(bottom, top):
# 			ring = makeLink(ring, i, (i+1))
# 	
# 		bottom += 4
# 		top += 4
# 		recursive_test(bottom, top)
# 		
# 	for i in range(0, 7):
# 		for i in range(vertical1, vertical2+1):
# 			ring = makeLink(ring, i, (i+4))
# 		
# 		vertical1 += 4
# 		vertical2 += 4
# 		recursive_test(vertical1, vertical2)
# 		
# 	
# 	print ring	
		
recursive_test(0,3) 

# print range(0,3)



	
	



# How many nodes?
# print len(ring)


# How many edges?
# print sum([len(ring[node]) for node in ring.keys()])/2   # takes len of innermost dict, sums, divides by 2. will work if can add to innermost the new connections  


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges


# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

How many nodes in movies?
How many edges in movies?

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 
# 
# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [] 
tour(movies, movie_tour)
# 
# 
# def findPath(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return path
#         if not graph.has_key(start):
#             return None
#         for node in graph[start]:
#             if node not in path:
#                 newpath = findPath(graph, node, end, path)
#                 if newpath: return newpath
#         return None
# 
# print findPath(movies, jr, ms)
# 
# 
# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)
# 
# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path