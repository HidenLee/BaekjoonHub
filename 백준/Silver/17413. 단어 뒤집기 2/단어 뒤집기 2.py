def generator(str1):
    i = 0
    N = len(str1)
    while i < N:
        if str1[i] == "<":
            tag_end_index = str1.find(">",i)
            yield str1[i:tag_end_index+1]
            i = tag_end_index + 1
        elif str1[i] == " ":
            yield str1[i]
            i += 1
        else:
            piece_start_index = i
            while i < N and not str1[i] in [" ","<",">"]:
                i += 1
            yield str1[piece_start_index:i][::-1]
print("".join(generator(input())))

