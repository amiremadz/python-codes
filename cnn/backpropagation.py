import math

# sigmoid example

w = [2,-3,-3] # assume some random weights and data
x = [-1, -2]

# forward pass
dot = w[0]*x[0] + w[1]*x[1] + w[2]
f = 1.0 / (1 + math.exp(-dot)) # sigmoid function

# backward pass through the neuron (backpropagation)
ddot = (1 - f) * f # gradient on dot variable, using the sigmoid gradient derivation
dx = [w[0] * ddot, w[1] * ddot] # backprop into x
dw = [x[0] * ddot, x[1] * ddot, 1.0 * ddot] # backprop into w
# we're done! we have the gradients on the inputs to the circuit

print(dx)
print(dw)

# staged computation

x = 3 # example values
y = -4

# forward pass

sigy = 1.0 / (1 + math.exp(-y)) # sigmoid in numerator   #(1)
num = x + sigy # numerator                               #(2)
sigx = 1.0 / (1 + math.exp(-x)) # sigmoid in denominator #(3)
xpy = x + y                                              #(4)
xpysqr = xpy**2                                          #(5)
den = sigx + xpysqr # denominator                        #(6)
invden = 1.0 / den                                       #(7)
f = num * invden # done!                                 #(8)
print(f)

# backprop f = num * invden
dnum = invden # gradient on numerator                    #(8)
dinvden = num                                            #(8)
# backprop invden = 1.0 / den
dden = (-1.0/ den**2) * dinvden                          #(7)
# backprop den = sigx + xpysqr
dsigx = dden                                             #(6)
dxpysqr = dden                                           #(6)
# backprop xpysqr = xpy**2
dxpy = (2 * dxpy) * dxpysqr                              #(5)
# backprop xpy = x + y
dx = dxpy                                                #(4)
dy = dxpy                                                #(4)
# backprop sigx = 1.0 / (1 + math.exp(-x))
dx += sigx * (1 - sigx) * dsigx# Notice += !!            #(3)
# backprop num = x + sigy
dx = dnum                                                #(2)
dsigy = dnum                                             #(2)
# backprop sigy = 1.0 / (1 + math.exp(-y))
dy += sigy * (1 - sigy) * dsigy                          #(1)

print(dx)
print(dy)

