N = int(input())
votes = list(map(int, input().split()))

impeachment_votes = sum(votes)

if impeachment_votes >= (2/3) * N:
    print("impeachment")
else:
    print("acusacao arquivada")