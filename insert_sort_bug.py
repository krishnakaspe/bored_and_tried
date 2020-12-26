def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        print(i,j,l[j],key)
        while (j >= 0) and (l[j] > key):
           print('iteration')
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

#m = int(input().strip())
ar = [4, 1, 3, 5, 6, 2]
#[int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
#THERE was one equal symbol missing in while loop (j>=0) 
#this was causing the issue
#https://www.hackerrank.com/challenges/correctness-invariant/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
