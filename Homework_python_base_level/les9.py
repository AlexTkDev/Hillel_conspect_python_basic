#                     ------------------------ EX 1 -----------------------

def popular_words(text, words):
    # text_list = text.lower().split()
    # word_count = {word: 0 for word in words}
    # for word in text_list:
    #     if word in word_count:
    #         word_count[word] += 1

#or
    text_list = text.lower().split()
    word_count = {word: text_list.count(word) for word in words}

    return word_count


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')


#                     ------------------------ EX 2 -----------------------

from typing import Union


def difference(*args) -> Union[int, float]:
    # if len(args) == 0:
    #     return 0
    #
    # min_elem = min(args)
    # max_elem = max(args)
    # result = (max_elem - min_elem)
    # return round(result, 2)

#or
    if args:
        result = round(max(args) - min(args), 2)
        return result

    return 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
