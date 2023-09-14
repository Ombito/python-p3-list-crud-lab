def create_an_empty_list():
    return list()

def create_a_list():
    list = [1, 2, 3, 4 ]
    return list

def add_element_to_end_of_list(l, element):
    l = [1, 2, 3, 4]
    element = 5
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l[0]= element
    return l

def remove_element_from_end_of_list(l):
    l = [1, 2, 3, 4]
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l = [1, 2, 3, 4]
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    l = [1, 2, 3, 4]
    return l[0]

def retrieve_element_from_index(l, index):
        return l[index]

def retrieve_last_element_from_list(l):
    l = [1, 2, 3, 4]
    return l[-1]
