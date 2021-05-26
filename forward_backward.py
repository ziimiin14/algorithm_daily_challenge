import numpy as np
import math
import torch

class y_func(torch.nn.Module):
    def __init__(self):
        super(y_func,self).__init__()
        self.a = torch.nn.Parameter(torch.randn(()))
    
    def forward(self,x):
        return self.a*x**3


# Initialize some data 
x = torch.linspace(-5,5,20000)
# x = x.view(-1,1)
# True value
y = torch.randint(0,2,(20000,))
y = y.float()




# Initilize model
model = y_func()

# Initialize loss function
criterion = torch.nn.MSELoss() # mean squared error
optimizer = torch.optim.SGD(model.parameters(),lr=1e-2)




for i in range(2000000):

    # Forward pass the model 
    y_pred = torch.sigmoid(model(x))


    # Compute loss
    loss = criterion(y_pred,y)

    if i %100 == 99:
        print(i, loss.item())

    # zero the gradients
    optimizer.zero_grad()
    # Perform Backward pass
    loss.backward()
    # Update weights
    optimizer.step()
