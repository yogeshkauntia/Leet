def letterCombinations(digits):
    memo = {'1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' '],
            '' : []}

    def _letterCombinations(d):

        if d not in memo:
            memo[d] = []
            for x in memo[d[0]]:
                for y in _letterCombinations(d[1:]):
                    memo[d].append(x + y)

        return memo[d]

    return _letterCombinations(digits)




