def heap_create(heap, N):
    for i in range((N-1)//2, -1, -1):
        sift_down(heap, i, N)
    return


def sift_down(heap, pos, N):
    while 2*pos+1 < N:
        j = pos
        if heap[j] < heap[2*pos+1]:
            j = 2*pos+1
        if 2*pos+2 < N and heap[j] < heap[2*pos+2]:
            j = 2*pos+2
        if pos == j:
            return
        heap[pos], heap[j] = heap[j], heap[pos]
        pos = j


def heapsort(heap):
    heap_create(heap, len(heap))
    print(*heap)
    for i in range(len(heap)-1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        sift_down(heap, 0, i)
        print(*heap)
    return