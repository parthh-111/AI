import heapq

ROMANIA_MAP={
    'Arad':{'Zerind':75,'Sibiu':140,'Timisoara':118},
    'Zerind':{'Arad':75,'Oradea':71},
    'Oradea':{'Zerind':71,'Sibiu':151},
    'Sibiu':{'Arad':140,'Ordea':151,'Fagaras':99,'Rimnicu Vilcea':80},
    'Timisoara':{'Arad':118,'Lugoj':111},
    'Lugoj':{'Timisoara':111,'Mehadia':70},
    'Mehadia':{'Lugoj':70,'Dobreta':75},
    'Dobreta':{'Mehadia':75,'Craiova':120},
    'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},
    'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},
    'Fagaras':{'Sibiu':99,'Bucharest':211},
    'Pitesti':{'Rimnicu Vilcea':97,'Craiova':138,'Bucharest':101},
    'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
    'Giurgiu':{'Bucharest':90},
    'Urziceni':{'Bucharest':85,'Hirsova':98,'Valsui':142},
    'Hirsova':{'Urziceni':98,'Eforie':86},
    'Eforie':{'Hirsova':86},
    'Valsui':{'Urziceni':142,'lasi':92},
    'lasi':{'Valsui':92,'Neamt':87},
    'Neamt':{'lasi':87}
    }

def uniform_cost_search(graph,start,goal):
    priority_queue=[(0,start,[start])]
    visited=set()
    while priority_queue:
        cost,current_node,path=heapq.heappop(priority_queue)

        if current_node==goal:
            return path,cost
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor,edge_cost in graph.get(current_node,{}).items():
            if neighbor not in visited:
                total_cost=cost+edge_cost
                heapq.heappush(priority_queue,
                               (total_cost,neighbor,path+[neighbor]))
    return None,float('inf')

start_city="Arad"
goal_city="Bucharest"

optimal_path,total_cost=uniform_cost_search(
    ROMANIA_MAP,start_city,goal_city
    )

if optimal_path:
    print(f"Path found from {start_city} to {goal_city}:")
    print("=>".join(optimal_path))
    print("Total cost:",total_cost)
else:
    print("No path found")
        
