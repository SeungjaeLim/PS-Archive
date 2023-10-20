from collections import Counter

def maximize_sequence(seq, R):
    cnt = Counter(seq) - Counter(R)
    ans = ''
    idx = 0
    
    while cnt:
        for i in range(9, -1, -1):
            num = str(i)
            if cnt[num] < 1:
                continue
            
            t = seq.find(num, idx)  
            check = cnt - Counter(seq[t:])  
            
            if check:  
                continue
            else:
                ans += num
                idx = t + 1
                cnt[num] -= 1
                if cnt[num] == 0:
                    del cnt[num]
                break  
    
    return ans

seq = input().strip()
R = input().strip()
print(maximize_sequence(seq, R))
