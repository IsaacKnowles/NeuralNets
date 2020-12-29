import sys
from Network import Network
from Layer import Layer
from Node import Node

input_layer = Layer(True, False)
output_layer = Layer(False, True)
nn = Network(input_layer,output_layer)

nn.input_layer.add_node(Node(1))
nn.input_layer.add_node(Node(1))
output_layer.add_node(Node(0,0))
#output_layer.add_node(Node(0,1))


hidden_layer = Layer(False, False)
hidden_layer.add_node(Node())
hidden_layer.add_node(Node())
hidden_layer.add_node(Node())

print("Adding layer")
nn.prepend_hidden_layer(hidden_layer)
#print(nn.input_layer.next_layer.next_layer)
#print(nn)
#sys.exit()


# INitialize the input and hidden layer weights.
nn.initialize_weights()

#
nn.predict_output()
#print(nn)

nn.back_prop()
