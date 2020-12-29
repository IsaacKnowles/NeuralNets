import Layer

class Network:

    """
    A neural network constructed from nodes and containing at least one input
    layer, one output layer, and one hidden layer, as well as the methods required
    for initializing the network and estimating the weights.

    Attributes:
    -----------
    input_layer : layer
        A non-empty dict of nodes serving as the input layer, with values initiated.

    output_layer : layer
        A non-empty list of nodes servings as the output layer, constant expected
        values init

    hidden_layers : dict<int,Layer>
        An index of the hidden layers

     Methods:
     --------
     initialize_nodes :
        For every Node in a hidden layer, generate a random number
        between 0 and 1 and assign it to each member of input_nodes for that Node.

    update_values :
        For every node except the input layer, apply the calculate_value method.
        This is essentially the forward propagation part of the NN estimation.

    update_weights :
        For each output node, calculate the error between the value of that nodes
        and its expected value. Then we set the weights in each node's input_nodes
        dictionary by multiplying that weight by the error.
    """
    def __init__(self,in_layer,out_layer):
        self.input_layer = in_layer
        self.output_layer = out_layer
        self.input_layer.next_layer = self.output_layer
        self.output_layer.prev_layer = self.input_layer
        self.layers = [in_layer,out_layer]

    def initialize_weights(self):
        layer = self.input_layer
        while True:
            for node in layer:
                layer.set_node_weights(node)

            layer = layer.next_layer
            if layer.is_output_layer:
                break

    def predict_output(self):
        layer = self.input_layer
        while True:
            i = 0
            #print(layer)
            for next_node in layer.next_layer:
                for node in layer.nodes:
                    next_node.value += node.value * node.weights[i]
                i += 1
            layer = layer.next_layer
            if layer.is_output_layer:
                break

    def back_prop(self):
        #print(self)
        layer = self.output_layer
        while True:

            #$print(layer)
            #print(layer.prev_layer)
            for prev_node in layer.prev_layer:
                i =0
                for node in layer:
                    prev_node.adjust_weight(node,i)
                i+=1
            if layer.is_input_layer:
                break
            else:
                layer = layer.prev_layer
                #print(layer)

    def append_hidden_layer(self,layer):
        """
        Adds a new hidden layer between the output layer and the hidden layer
        currently attached to the output layer, if one exists.
        """
        old_layer = self.output_layer.prev_layer
        self.output_layer.detach_prev_layer()
        success = self.output_layer.attach_prev_layer(layer)
        layer.attach_prev_layer(old_layer)
        old_layer.attach_next_layer(layer)

    def prepend_hidden_layer(self,layer):
        '''
        Adds a new hidden layer between the input layer and the hidden layer
        currently attached to the input layer, if one exists.
        '''
        old_layer = self.input_layer.next_layer
        #print(old_layer)
        self.input_layer.detach_next_layer()
        self.input_layer.attach_next_layer(layer)
        layer.attach_next_layer(old_layer)
        old_layer.attach_prev_layer(layer)
        layer.attach_prev_layer(self.input_layer)
        #print(layer)
        #print(layer.prev_layer)
        self._index_layers()

    def _index_layers(self):
        index_complete = False
        i = 0
        layer = self.input_layer
        self.layers = []
        while not index_complete:
            index_complete = layer.is_output_layer
            self.layers.append(layer)
            layer = layer.next_layer


    def __str__(self):
        for layer in self.layers:
            print(layer)
        return('')















'''
hidden_layer_spec : dictionary
    A non-empty, zero-indexed dictionary of hidden layers, with each key
    pointing to an integer representing the number of nodes to create in each
    layer.
'''
