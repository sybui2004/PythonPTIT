def solve(text):
    arr_line = text.replace('!', '.').replace('?', '.').split('.')

    ans = []
    for line in arr_line:
        line = line.strip()
        if line: 
            words = line.lower().split()
            words[0] = words[0].capitalize()
            ans.append(' '.join(words))
    
    return ans

s = ""
while True: 
    try:
        s += input()
    except EOFError:
        break
solved_para = solve(s)
for i in solved_para:
    print(i)
