#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    hash_table_insert(ht, weights[0],0)
    current_index = 1
    while current_index < length:
        current_weight = weights[current_index]
        hash_table_insert(ht, current_weight, current_index)
        limit_pair = limit - current_weight
        has_pair = hash_table_retrieve(ht, limit_pair)
        if has_pair:
            if current_index == 1:
                return (current_index, 0)
            elif has_pair > current_index:
                return (has_pair, current_index)
            else:
                return (current_index, has_pair)
        current_index += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
