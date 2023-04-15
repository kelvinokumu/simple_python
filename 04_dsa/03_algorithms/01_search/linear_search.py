# The search operation is used to find out the index position of a given data item in a list of data
# items. If the searched item is available in the given list of data items, then the search algorithm
# returns the index position where it is located; otherwise, it returns that the item is not found.
# Here, the index position is the location of the desired item in the given list.

def search(unordered_list, term):
    for i, item in enumerate(unordered_list):
        if term == unordered_list[i]:
            return i
    return None


list1 = [60, 1, 88, 10, 11, 600]
search_term = 10
index_position = search(list1, search_term)
print(index_position)

list2 = ['packt', 'publish', 'data']
search_term2 = 'data'
Index_position2 = search(list2, search_term2)
print(Index_position2)
