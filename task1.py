interval_string = input().strip()
result_set = set()
intervals = interval_string.split(',')

for interval in intervals:
    if '-' in interval:
        start, end = map(int, interval.split('-'))
        for num in range(start, end + 1):
            result_set.add(num)
    else:
        result_set.add(int(interval))

sorted_result = sorted(result_set)
print(' '.join(map(str, sorted_result)))