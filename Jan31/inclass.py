# 2. Special Pythagorean triplet

# for a in range(1, 1001):
#     for b in range(a + 1, a + 1001):
#         if a + b > 1000:
#             break
#         c = 1000 - a - b
#         # a2 + b2 = c2
#         if (a ** 2 + b ** 2 == c ** 2):
#             print(f'The number is {a}+{b}+{c} = 1000')

str1 = "bbcc"
str2 = "ccbbe"
# # commonStr = {}

# common = ''.join(set(str1).intersection(str2))
# print(common)
# commonStr = list(common)
# print(commonStr)
# Function to concatenated string with uncommon
# characters of two strings


def uncommonConcat(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    common = list(set1 & set2)

    result = [ch for ch in str1 if ch not in common] + \
        [ch for ch in str2 if ch not in common]

    print(''.join(result))


if __name__ == "__main__":
    str1 = "bbcc"
    str2 = "ccbbe"
    uncommonConcat(str1, str2)
