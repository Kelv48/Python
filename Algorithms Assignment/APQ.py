#122318693
#Used chatgpt and copilot

class Element_heap():
    """ A key, value and index. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __str__(self):
        return str(self._key) + " " + str(self._value) + " " + str(self._index) + " "

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

class APQHeap():
    #Partially from lab solution
    def __init__(self):
        self.elements = []  # Renamed _body to elements
        self.num_elements = 0  # Renamed _size to num_elements

    def __str__(self):
        """ Return a breadth-first string of the values. """
        output_str = ""  # Renamed ans to output_str
        for element in self.elements:  # Renamed i to element
            output_str += "k" + str(element._key) + " " + "i" + str(element._index) + " " + "v" + str(element._value) + " "
        return output_str

    def add(self, key, value):
        """ Add Element(key,value) to the heap. """
        element = Element_heap(key, value, self.num_elements)  # Renamed elt to element
        self.elements.append(element)
        self._up_heap(self.num_elements)
        self.num_elements += 1
        return element

    def min(self):
        """ Return the min priority key,value. """
        if self.elements:
            return self.elements[0]
        else:
            return None  # Changed "None" to None

    def remove_min(self):
        """ Remove and return the min priority key,value. """
        if self.elements:
            min_element = self.elements[0]  # Renamed output to min_element
            if self.num_elements > 1:
                self.elements[0] = self.elements.pop()
                self.elements[0]._index = 0
                if self.num_elements > 1:
                    self.num_elements -= 1
                    self._down_heap(0)
            else:
                self.num_elements -= 1
                self.elements.pop()
            return (min_element._key, min_element._value)  # Modified return statement
        else:
            return None  # Changed "None" to None

    def update_key(self, element, new_key):
        if element._key < new_key:
            element._key = new_key
            self._down_heap(element._index)
        else:
            element._key = new_key
            self._up_heap(element._index)

    def get_key(self, element):
        return self.elements[element._index]._key

    def is_empty(self):
        return self.num_elements == 0

    def length(self):
        return self.num_elements

    def _up_heap(self, position):
        """ Bubble the item in position in the heap up to its correct place. """
        current_position = position
        while True:
            parent_position = (current_position - 1) // 2
            if parent_position < 0:
                break
            else:
                if self.elements[current_position]._key < self.elements[parent_position]._key:
                    self.elements[current_position], self.elements[parent_position] = self.elements[parent_position], self.elements[current_position]
                    self.elements[current_position]._index, self.elements[parent_position]._index = self.elements[parent_position]._index, self.elements[current_position]._index
                    current_position = parent_position
                else:
                    break

    def _down_heap(self, position):
        """ Bubble the item in position in the heap down to its correct place. """
        current_position = position
        while True:
            child_indices = [current_position * 2 + 1, current_position * 2 + 2]
            if child_indices[0] >= self.num_elements:
                child_indices[0] = None
            if child_indices[1] >= self.num_elements:
                child_indices[1] = None

            if child_indices[0] and not child_indices[1]:
                min_child = child_indices[0]
            elif child_indices[1] and not child_indices[0]:
                min_child = child_indices[1]
            elif not child_indices[0] and not child_indices[1]:
                break
            else:
                child_keys = {child_indices[0]: self.elements[child_indices[0]]._key, child_indices[1]: self.elements[child_indices[1]]._key}
                min_child = min(child_keys, key=lambda k: child_keys[k])

            if self.elements[current_position]._key > self.elements[min_child]._key:
                self.elements[current_position], self.elements[min_child] = self.elements[min_child], self.elements[current_position]
                self.elements[current_position]._index, self.elements[min_child]._index = self.elements[min_child]._index, self.elements[current_position]._index
                current_position = min_child
            else:
                break

class Element_array():
    """ A key, value, and index. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __str__(self):
        return str(self._key) + " " + str(self._value) + " " + str(self._index)

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None


class APQArray():
    def __init__(self):
        self.elements = []  # Renamed _body to elements
        self.num_elements = 0  # Renamed _size to num_elements

    def __str__(self):
        return str([str(element) for element in self.elements]) 

    def size(self):  # Renamed len to size
        return len(self.elements)

    def add(self, key, item):
        element = Element_array(key, item, len(self.elements)) 
        self.elements.append(element)
        self.num_elements += 1
        return element

    def min(self):
        minimum_element = self.elements[0] 
        for element in self.elements:
            if element._key < minimum_element._key:
                minimum_element = element
        return minimum_element

    def remove_min(self):
        min_element = self.min()  # Renamed m to min_element
        self.elements[min_element._index], self.elements[-1] = self.elements[-1], self.elements[min_element._index]
        self.elements[min_element._index]._index, self.elements[-1]._index = self.elements[-1]._index, self.elements[min_element._index]._index
        self.elements.pop()
        self.num_elements -= 1
        return (min_element._key, min_element._value)

    def update_key(self, element, new_key):
        self.elements[element._index]._key = new_key

    def get_key(self, element):
        return self.elements[element._index]._key

    def remove(self, element):
        self.elements[element._index], self.elements[-1] = self.elements[-1], self.elements[element._index]
        self.elements[element._index]._index, self.elements[-1]._index = self.elements[-1]._index, self.elements[element._index]._index
        print(f"removing ( {self.elements.pop()} )")  # Renamed elt to element

    def is_empty(self):  # Renamed isEmpty to is_empty
        return self.num_elements == 0

    def length(self):
        return self.num_elements

