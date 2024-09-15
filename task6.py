from collections import deque, defaultdict

n = int(input())
execution_time = [0] * (n + 1)
graph = defaultdict(list)
in_degree = [0] * (n + 1)
for i in range(1, n + 1):
    data = list(map(int, input().strip().split()))
    execution_time[i] = data[0]
    dependencies = data[1:]
    for dep in dependencies:
        graph[dep].append(i)
        in_degree[i] += 1

queue = deque()
finish_time = [0] * (n + 1)
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)
        finish_time[i] = execution_time[i]

while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        finish_time[neighbor] = max(finish_time[neighbor], finish_time[current] + execution_time[neighbor])
        in_degree[neighbor] -= 1
        
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

result = max(finish_time)
print(result)