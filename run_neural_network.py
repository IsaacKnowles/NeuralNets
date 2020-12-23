from Network import Network
from Layer import Layer
from Node import Node

input_layer = Layer(True, False)
input_layer.add_node(Node(1))
input_layer.add_node(Node(1))

output_layer = Layer(False, True)
output_layer.add_node(Node(None,1))
output_layer.add_node(Node(None,1))

nn = Network(input_layer,output_layer)

hidden_layer = Layer(False, False)
hidden_layer.add_node(Node())
hidden_layer.add_node(Node())
hidden_layer.add_node(Node())

nn.prepend_hidden_layer(hidden_layer)


# INitialize the input and hidden layer weights.
nn.initialize_weights()

#
nn.predict_output()
