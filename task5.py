from collections import defaultdict  

start_time = input().strip()  
n = int(input().strip())  
servers = defaultdict(lambda: {'accessed': False, 'attempts': 0})  
team_results = defaultdict(lambda: {'accessed_count': 0, 'penalty': 0})  

def parse_time_to_seconds(hhmmss):  
    """ Parse the time from hh:mm:ss to seconds since start of the day. """  
    h, m, s = map(int, hhmmss.split(':'))  
    return h * 3600 + m * 60 + s  

start_seconds = parse_time_to_seconds(start_time)  

for _ in range(n):  
    request = input().strip()  
    parts = request.split()  
    team_name = parts[0].strip('"')  
    request_time = parts[1]  
    server_id = parts[2]  
    result = parts[3]  

    request_seconds = parse_time_to_seconds(request_time)  
    
    if request_seconds < start_seconds:  
        request_seconds += 24 * 3600  
    elapsed_time = request_seconds - start_seconds  

    if result == "ACCESSED":  
        penalty_time = elapsed_time // 60  
        team_results[team_name]['accessed_count'] += 1  
        team_results[team_name]['penalty'] += penalty_time + (servers[server_id]['attempts'] * 20)  
        servers[server_id]['accessed'] = True  

    elif result in ('DENIED', 'FORBIDEN'):  
        if not servers[server_id]['accessed']:  
            servers[server_id]['attempts'] += 1  

results_list = []  

for team, data in team_results.items():  
    results_list.append((data['accessed_count'], data['penalty'], team))  
  
results_list.sort(key=lambda x: (-x[0], x[1], x[2]))  
rank = 1  
for idx, (accessed_count, penalty, team) in enumerate(results_list):  
    if idx > 0 and (results_list[idx-1][0] != accessed_count or results_list[idx-1][1] != penalty):  
        rank = idx + 1  
    print(f"{rank} \"{team}\" {accessed_count} {penalty}")  