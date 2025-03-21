num_cnt = int(input())
num_arr = list(map(int, input().split()))

max_num = num_arr[0]
min_num = num_arr[0]

for i in range(1,num_cnt):
    if max_num < num_arr[i]:
        max_num = num_arr[i]
    if min_num > num_arr[i]:
        min_num = num_arr[i]

print(min_num, max_num)



## 다른 풀이
num_cnt = int(input())
num_arr = list(map(int, input().split()))
print(min(num_arr), max(num_arr))