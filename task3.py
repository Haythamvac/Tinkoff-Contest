from collections import Counter

press_sequence = input().strip()  
required_chars = input().strip()  
max_length = int(input().strip())  

required_set = set(required_chars)
required_count = len(required_set)
char_count = Counter(press_sequence)

for char in required_set:
    if char_count[char] == 0:
        print("-1")
        break
else:
    n = len(press_sequence)
    result = ""

    for start in range(n):
        if press_sequence[start] not in required_set:
            continue

        seen = set()
        end = start

        while end < n and end - start < max_length:
            if press_sequence[end] in required_set:
                seen.add(press_sequence[end])

            if len(seen) == required_count:
                current_password = press_sequence[start:end + 1]
                if (len(current_password) > len(result) or 
                    (len(current_password) == len(result) and current_password > result)):
                    result = current_password

            end += 1

    print(result if result else "-1")