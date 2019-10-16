def countSets(arr, s):
    '''
    Count the number of subsets of list arr, totalling to sum s
    '''

    mem = {}
    for idx in range(len(arr)+1):
        mem['0-' + str(idx)] = 1

    def _recCountSets(arr, total, i=0):

        if str(total)+ '-' + str(i) in mem:
            return mem[str(total)+ '-' + str(i)]

        elif total < 0 or i >= len(arr):
            return 0

        elif total < arr[i]:
            k = _recCountSets(arr, total, i+1)

        else:
            k = _recCountSets(arr, total - arr[i], i+1) + _recCountSets(arr, total, i+1)

        mem[str(total)+ '-' + str(i)]=k

        return mem[str(total)+ '-' + str(i)]

    return _recCountSets(arr, s)
