#122318693
#Used chatgpt and copilot

from APQ import *
class Vertex():
   def __init__(self,element: str):
      self._element = element

   def __str__(self):
      return str(self._element)
   

class Edge():
   def __init__(self, edge_label: str , weight: int,vertexOne: Vertex, vertexTwo: Vertex):
      self._edge = edge_label
      self._weight = weight
      self._vertexOne = vertexOne # vertex class
      self._vertexTwo = vertexTwo # vertex class
    
   def __str__(self):
      return f" Weight: {self._weight}, Path: {self._vertexOne} <-> {self._vertexTwo} "
    
   def source(self):
      return self._vertexOne
    
   def destination(self):
      return self._vertexTwo
    
   def opposite(self,vertex):
      if vertex == self._vertexOne:
         return self._vertexTwo
      else:
         return self._vertexOne 

class Graph():
   #Graph partially taken from chatgpt
   def __init__(self):
      self._Adjacency_Map = {}

   def __str__(self):
      string = ""
      for vertex in self._Adjacency_Map:
         string += str(vertex) + " ["
         for connected_vertex, edge in self._Adjacency_Map[vertex].items():
            string +=  "\n\t" +str(connected_vertex) + "->" + str(edge) 
         string += "\n]\n"
      return string
    
   def vertices(self):
      return [str(vertex) for vertex in self._Adjacency_Map.keys()]
    
   def edges(self):
      edges = set()
      for vertex in self._Adjacency_Map:
         for vertexEdge in self._Adjacency_Map[vertex]:
            edges.add(str(self._Adjacency_Map[vertex][vertexEdge]))
      return list(edges)
    
   def num_vertices(self):
      return len(self.vertices())
    
   def num_edges(self):
      return len(self.edges())
    
   def get_edge(self,vertexOne,vertexTwo):
    if vertexOne in self._Adjacency_Map and vertexTwo in self._Adjacency_Map[vertexOne]:
        return self._Adjacency_Map[vertexOne][vertexTwo]
    else:
        return None
    
   def degree(self, vertex):
      return len(self._Adjacency_Map[vertex])
    
   def get_edges(self,vertex):
      return [edge for edge in self._Adjacency_Map[vertex].values()]
   
   def add_vertex(self,element):
      for vertex in self._Adjacency_Map:
         if vertex._element == element:
            return vertex
      

      new_vertex = Vertex(element)
      self._Adjacency_Map[new_vertex] = dict()
      return new_vertex

   def add_edge(self,vertexOne,vertexTwo, edge=0,weight=0):
      if vertexOne and vertexTwo in self._Adjacency_Map:
         new_edge = Edge(edge,weight,vertexOne,vertexTwo)

         self._Adjacency_Map[vertexOne][vertexTwo] = new_edge
         self._Adjacency_Map[vertexTwo][vertexOne] = new_edge    
         return new_edge

   def remove_vertex(self,vertex):
      if vertex in self._Adjacency_Map:
         for connected_vertex in self._Adjacency_Map[vertex]:
            self._Adjacency_Map[connected_vertex].pop(vertex)
         self._Adjacency_Map.pop(vertex)
      else:
         print("The vertex is not in the graph")


   def remove_edge(self,edge):
      vertexOne = edge._vertexOne
      vertexTwo = edge._vertexTwo

      if (vertexOne in self._Adjacency_Map and vertexTwo in self._Adjacency_Map[vertexOne]) and (vertexTwo in self._Adjacency_Map and vertexOne in self._Adjacency_Map[vertexTwo]):
         self._Adjacency_Map[vertexOne].pop(vertexTwo)
         self._Adjacency_Map[vertexTwo].pop(vertexOne)
      else:
         print("Edge not in graph")

if __name__ == "__main__":
   # CREATING RANDOM GRAPH HELP FROM CHATGPT
   import random
   import time

   def create_graph(n, m): # n vertices and m edges
      graph = Graph()  # Create an empty Graph object
      vertices = []    # List to store references to the vertices
      
      # Add n vertices to the graph and store their references in the list
      for i in range(n):
         vertex = graph.add_vertex("V"+str(i))  # Add vertex with element ranging from 0 to n-1
         vertices.append(vertex)

      connected = []
      for v in vertices:
         connected.append(v)
         if len(connected) != 1:
            v2 = random.choice(connected)
            while v == v2:
               v2 = random.choice(connected)
            graph.add_edge(v,v2, edge="0", weight=random.randint(1,20))
      max_edges = n*(n-1)
      more_edges = int(round((max_edges*m),) - (n-1))

      for _ in range(more_edges):
         # Randomly select two different vertices from the list
         vertexOne = random.choice(vertices)
         vertexTwo = random.choice(vertices)
         
         # Ensure the selected vertices are different and have different edges and not already in graph
         while vertexTwo == vertexOne or graph.get_edge(vertexOne, vertexTwo) is not None:
               vertexOne = random.choice(vertices)
               vertexTwo = random.choice(vertices)

         
         # Check if the edge already exists in the graph
         # If not, add the edge to the graph
         if graph.get_edge(vertexOne, vertexTwo) is None:
               graph.add_edge(vertexOne, vertexTwo, edge="0", weight=random.randint(1,20))

      return graph
   
   def create_dense_graph(n):
      graph = Graph()  # Create an empty Graph object
      
      # Add n vertices to the graph
      vertices = [graph.add_vertex("V" + str(i)) for i in range(n)]
      
      # Connect each vertex to every other vertex
      for i in range(n):
         for j in range(i + 1, n):  # Start from i+1 to avoid self-loops and duplicate edges
               # Check if an edge already exists between vertices v1 and v2
               if graph.get_edge(vertices[i], vertices[j]) is None:

                  # Add an edge between the vertices with the calculated weight
                  graph.add_edge(vertices[i], vertices[j], edge="0", weight=random.randint(1,20))
               
      return graph


   #Prims logic taken from chatgpt
   def Prims(g,apq):
      q = apq()
      tree = []
      locs = {}
      for v in g._Adjacency_Map:
         element = q.add(float("inf"), [v, None])
         locs[v] = element

      while not q.is_empty():
         c = q.remove_min()[1] # [v,None]
         locs.pop(c[0])

         if c[1] is not None:
               tree.append(c[1])

         for e2 in g.get_edges(c[0]):
               v2 = e2.opposite(c[0])
               if v2 in locs:
                  cost = e2._weight
                  if cost < q.get_key(locs[v2]):
                     q.update_key(locs[v2], cost)
                     locs[v2]._value[1] = e2
      return tree

   def evaluation():
      test_amount = 1 # test cases
      #Tested for 30k but crashed due to memory error around 20k on 48Gb Ram
      vertices = [100, 200, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
      
      for vertices_count in vertices:
         sparse_time_list = []
         sparse_time_heap = []      
         medium_sparse_time_list = []
         medium_sparse_time_heap = []
         dense_time_list = []
         dense_time_heap = []

         for _ in range(test_amount): 
            # sparse graphs
            graph = create_graph(vertices_count,0)

            # list
            start_time = time.perf_counter()
            Prims(graph,APQArray)
            end_time = time.perf_counter()
            sparse_time_list.append(end_time-start_time)

            # heap
            start_time = time.perf_counter()
            Prims(graph,APQHeap)
            end_time = time.perf_counter()
            sparse_time_heap.append(end_time-start_time)

            # mid sparse graphs
            graph = create_graph(vertices_count,0.5)

            # list
            start_time = time.perf_counter()
            Prims(graph,APQArray)
            end_time = time.perf_counter()
            medium_sparse_time_list.append(end_time-start_time)

            # heap
            start_time = time.perf_counter()
            Prims(graph,APQHeap)
            end_time = time.perf_counter()
            medium_sparse_time_heap.append(end_time-start_time)

            # dense graphs
            graph = create_dense_graph(vertices_count)

            # list
            start_time = time.perf_counter()
            Prims(graph,APQArray)
            end_time = time.perf_counter()
            dense_time_list.append(end_time-start_time)

            # heap
            start_time = time.perf_counter()
            Prims(graph,APQHeap)
            end_time = time.perf_counter()
            dense_time_heap.append(end_time-start_time)
         
         print(f"Unsorted List Sparse, Size={vertices_count}, Time={sum(sparse_time_list)/len(sparse_time_list)}")
         print(f"Heap Sparse, Size={vertices_count}, Time={sum(sparse_time_heap)/len(sparse_time_heap)}")
         print(f"Unsorted List Medium Sparse, Size={vertices_count}, Time={sum(medium_sparse_time_list)/len(medium_sparse_time_list)}")
         print(f"Heap Medium Sparse, Size={vertices_count}, Time={sum(medium_sparse_time_heap)/len(medium_sparse_time_heap)}")
         print(f"Unsorted List Dense, Size={vertices_count}, Time={sum(dense_time_list)/len(dense_time_list)}")
         print(f"Heap Dense, Size={vertices_count}, Time={sum(dense_time_heap)/len(dense_time_heap)}")
         print("\n\n")
   
   evaluation()