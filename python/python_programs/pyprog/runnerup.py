
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s=sorted(list(set(arr)))[-2]
    print(s)
