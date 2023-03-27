# Searching Algorithm
- This is a first lab I have to complete when learning the basis of artificial intelligence. 
## Knowledge
- Searching algorithm is classified into two main categories. It includes:
```
 Uninformed search 
    - not provided about how to close the states are
    - be able to generate "successor" and know target state discrimination
    - each of seaching strategy is an (graph/tree) instance of general searching problem
    - include: DFS (Depth first search), BFS (Breadth first search), UCS (Uniform Cost Search)

Informed search 
    - beside the definition, a, it also use particular knowledge about proble
    - has an ability to find more effectively than Uniformed search
    - use heuristic function to evalutate remaining cost to reach goal state
    - include: A*, Greedy best-first search,... 
```
## Before Running
- make sure that you download python env
- installed pygame module
## Running
- go to directory which contains file ending in `.py` (source code)
- then, just simply typing following command `python .\main.py --algo<a> --start<b> --goal<c>`
    -  a is algorithm you want to run (BFS, DFS, UCS, AStar)
    -  b is starting position  
    -  c is goal position
  ## Demo
  - https://www.youtube.com/watch?v=4f7ubTI8c2U&feature=youtu.be
