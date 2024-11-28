class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Step 1: Build the graph and compute in-degrees
        graph = defaultdict(list)
        for u, v in relations:
            weight = time[v-1]
            graph[u].append((v, weight))
        
        # Step 2: Topological sort using Kahn's algorithm
        in_degree = [0] + [1] * (n)
        for u, v in relations:
            in_degree[v] += 1
        # print (in_degree)
        for i in range(1, n+1):
            if in_degree[i] == 1:
                weight = time[i-1]
                graph[0].append((i,weight))
        
        # print (graph)
        topo_order = [0]
        queue = deque([i for i in range(n+1) if in_degree[i] == 1])
        # print (queue)
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor, _ in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 1:
                    queue.append(neighbor)
                    # print (queue)

        
        
        # Step 3: Initialize distances and parent pointers
        distances = [-float('inf')] * (n+1)
        start = 0
        distances[start] = 0  # Starting node has sum 0
        parent = {start: None}  # To track the path
        # print (topo_order)
        # Step 4: Relax edges in topological order
        for node in topo_order:
            for neighbor, weight in graph[node]:
                # print (neighbor, weight, node, distances[node] + weight, distances[neighbor])
                if distances[node] + weight > distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    parent[neighbor] = node
                    # print (parent)
        
        # Step 5: Find the maximum sum and reconstruct the path
        max_sum = max(distances)
        max_node = distances.index(max_sum)
        
        # Reconstruct the path
        path = []
        while max_node is not None:
            path.append(max_node)
            max_node = parent.get(max_node)
        
        path.reverse()
        return max_sum