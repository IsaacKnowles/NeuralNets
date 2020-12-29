import random
from Node import Node

class Layer:
    '''
    Layers are groups of nodes that can be reached in the same number of steps
    following links from any of the nodes found in another layer.
    Attributes:
    ----------
    is_input_layer : bool
        Indicating whether this is the input layer.

    is_output_layer : bool
        Indicating whether this is the output layer.

    prev_layer : Layer
        Link to previous layer

    next_layer : Layer
        Link to next layer
    '''

    def __init__(self, is_in, is_out, prev=None, next=None, nodes=[]):
        self.is_input_layer= is_in
        self.is_output_layer= is_out
        self.prev_layer= prev
        self.next_layer= next
        self.nodes = nodes if len(nodes) > 0 else []

    def add_node(self, node):
        self.nodes.append(node)
        #print(self.nodes)

    def get_num_nodes(self):
        return(len(self.nodes))

    def detach_prev_layer(self):
        self.prev_layer= None

    def attach_prev_layer(self, layer):
        if not self.is_input_layer:
            self.prev_layer= layer
            return(True)
        else:
            print("Cannot attach previous layer to input layer")
            return(False)

    def detach_next_layer(self):
        self.next_layer= None

    def attach_next_layer(self, layer):
        if not self.is_output_layer:
            self.next_layer= layer
            return(True)
        else:
            print("Cannot attach next layer to output layer")
            return(False)

    def set_node_weights(self, node, weights = None):
        if self.is_output_layer:
            print("Nodes in output layers do not get weights")
            return(False)
        num_nodes = self.next_layer.get_num_nodes()
        if not weights or num_nodes != len(weights):
            print("Weight list is not commensurable with number of nodes.")
            print("Weights will be initialized with random values.")
            weights = [random.random() for x in range(num_nodes)]
        node.set_weights(weights)

    def __iter__(self):
        for n in self.nodes:
            yield(n)

    def __str__(self):
        if self.is_input_layer:
            print('Input Layer')
        elif self.is_output_layer:
            print("Output Layer")
        else:
            print("Hidden Layer")
        node_id = 0
        retval = [str(n) for n in self.nodes]
        return(retval.__str__())

    """
        num_nodes=self.get_num_nodes()
        num_nodes_next_layer=self.next_layer.get_num_nodes()
        if not weights:  # just set weights ranndomly
            for n in nodes:
                for i in num_weights:


        index_complete=False
        i=0
        layer=self.input_layer.next_layer
        self._hidden_layers={}
        while not index_complete:
            _hidden_layers[0]=layer
            layer=layer.next_layer
            if layer.is_output_layer:
                index_complete=True
    """
