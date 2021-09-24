def solution(s):
    n = 2
    split_strings = [s[index : index + n] for index in range(0, len(s), n)]
    a = split_strings
    b = "".join(str(a[2]))
    #a = a[:-1] + b
    return print(b)




solution("asdfg")


