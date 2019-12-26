from collections import defaultdict
import heapq

def FindKFrequentElem(my_str, k_frequent):
    count_freq = defaultdict(int)
    for elem in my_str:
        count_freq[elem] += 1
    
    res = []
    for k,v in count_freq.items():
        if(len(res) < k_frequent):
            heapq.heappush(res, (v, k))
        elif(v > res[0][0]):
            heapq.heappushpop(res, (v, k))

    return res

########### MAIN ###########

my_str = [1,1,1,2,2,3]
k_frequent = 2

res = FindKFrequentElem(my_str, k_frequent)
for elem in res:
    print(elem[1])


########### STDOUT ###########

#2
#1
