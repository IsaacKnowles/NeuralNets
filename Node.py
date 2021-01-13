import random

class Node:
    """
    A class representing a node in a neural network. Nodes just store values.

    Attributes:
    ----------
    value: double
        The current value of the Node

    expected_value : double
        An optional, expected value for the node. Only valid for output nodes.

    layer: int
        The layer in which the node resides, and which it may share with other
        nodes.

    input_nodes: dict
        A dictionary keyed by the nodes in the previous layer (if applicable),
        and with values corresponding to the weight on each of those nodes.

    Methods:
    ---------
    calculate_value(no parameters)
        Sets the value of the node as the dot product of the values of each nodes
        in input_nodes and the vector of their weights.

    get_value(no parameters)
        Returns the current value of the node.

    """
    def __init__(self, value = 0, expected_value = None):
        self.value = value
        self.expected_value = expected_value
        self.error = 0
        self.weights = 0

    def calculate_value(self):
        if len(input_nodes.keys()) > 0:
            self.value = 0
            for k in input_nodes.keys():
                self.value += inputs_node[k] * k.get_value()
        else:
            print("No input nodes for this node.")

    def set_value(self,v):
        self.value = v

    def get_value(self):
        return(this.value)

    def set_expected_values(self,v):
        self.expected_value = v

    def get_expected_value(self):
        return(self.expected_value)

    def set_weight(self,i,w):
        self.weights = w

    def set_weights(self,w_list):
        self.weights = w_list

    def adjust_weight(self,node,i):
        error = node.value - node.expected_value
        w = self.weights[i] * error
        self.set_weight(i,w)
        self.set_expected_value()

    def __str__(self):
        return(str(self.value) + " " + str(self.weights))
