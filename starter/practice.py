word = "test 123"
print (word[1])

#word.count() + ''

# count(word)

list1 = [1, 2, 3, 4, 5]
print (list1[2:])

a, b = 0, 1
while b < 10:
    print(b, end=',')
    a, b = b, a + b


def cheeseshop(kind, *arguments, **keywords):
    print("\n-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("_" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("nguyen", "it's cute", "It's nice",
           "whatever", key1=1, key2="a number")

def test(first, **third):
    print("first one is", first)
    # for e in second:
    #     print(e)

    for k in third:
        print(k, "is", third[k])

test("mot", adsd12bc="abc")
