# Graph Coloring and Chromatic Number
A **Coloring** of a simple Graph is the assignment of a color to each vertex of the graph so that no two adjacent vertices are assigned the same color.
The **Chromatic Number** of a graph is the **least number** of colors needed for a coloring of this graph, denoted by $\chi(G)$.
Obviously, 
$$\chi(K_n)=n, \chi(K_{m,n})=2
$$
For a cycle graph $c_n$, we have:
$$
\chi(C_n)=
\begin{cases}
    2\ \ (n\ is\ even)\\
    3\ \ (n\ is\ odd)
\end{cases}
$$
### Useful properties of chromatic number:
1. $$1\le\chi(G)\le V(G)$$
2. $$\chi(G)(\chi(G)-1)\le 2|E(G)|$$
3. If G has a **clique**(a complete subgraph) of size $k$, then:$\chi(G)\ge k$
i.e. $\chi(G)\ge\omega(G)$, where $\omega(G)$ denotes the size of the largest clique in $G$.
4. A **greedy coloring** shows that $\chi(G) ≤ \Delta (G) + 1$, where $\Delta(G)$ is the maximum vertex degree
5. $\chi(G)=min\{\chi(G+uv), chi(G/uv)\}$ where $\{u,v\}\subset V(G)$ and $uv\in E(G)$
   
# Graph Planarity
### Definition:
A graph is called **Planar** if it can be drawn in the plane **without any edges crossing**, where an edge crossing is the intersection of the lines or arcs representing them at a point other than their common endpoint.
Such a drawing is called a **planar representation** of the graph.
Obviously:
    $K_n(n\ge 5)$ and $$K_{m,n}(m,n \ge 2)$ are non-planar.
### Euler's Formula
Let $G$ be a connected planar simple graph with $e$ edges and $v$ vertices, $r$ be the number of regions in a planar representation of G. 
Then $r = e − v + 2.$
####  Corollary of Euler's Formula:
If $G$ is a connected planar simple graph with $e$ edges and $v$ vertices, where $v ≥ 3$.
1.  $e ≤ 3v−6$
**proof**:
    Let $r_i$ represent the number of the regions with $i$ enges.
    $r=\sum^n_{i=1}r_i$, and each regions has at least 3 edges, each edge is used by two regions.
    $\therefore 2e=\sum_{i=3}(i\cdot r_i)=3r+\sum_{i=3}((i-3)\cdot r_i)\ge0$  
    $\therefore 2e\ge3r$
    $\therefore v-2=e+r\le\frac{5}{3}e,$
    Q.E.D
2. At least there is a point with degree $\le 5$
**proof**:
we suppose that all vertices with degree $\ge6$
then $2e=\sum_{v\in V}deg(v)\ge6v, contradict$

### Kuratowski's Theorem.
An **elementary subdivision** is the operation of removing an edge {u,v} from a graph, and adding a new vertex w together with edges {u,w} and {w,v}.
**Homeomorphic**:
    Graphs $G_1$ and $G_2$ are said to be homeomorphic if they can be obtained from the same graph by a sequence of elementary subdivisions.
**Theorem**:
A graph is nonplanar IFF it contains a subgraph **homeomorphic** to $K_{3,3}$ or $K_5$.
Kuratowski's Theorem can be **generalized**, for instance as **Wagner's Theorem:**
Every non-planar graph contains either the utility graph $K_{3,3}$ or the pentatope graph $K_5$ as a graph minor.