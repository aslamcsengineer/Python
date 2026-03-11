#tower of hanoi

#rule 1 bigger disk always below smaller disk
#move only one disk at a time

def toh(n,src,dest,temp):
    if (n>=1):
        toh(n-1, src, temp, dest)
        print(f"Move {src} -> {dest}")
        toh(n-1,temp,dest,src)
toh(8,1,3,2)

#O(2^n)