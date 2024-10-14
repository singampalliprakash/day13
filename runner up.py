"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up."""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b=[]
    for i in arr:
        if i not in b:
            b.append(i)
    b.sort()
    print(b[-2])        
    
