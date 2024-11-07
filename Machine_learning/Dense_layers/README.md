# Summary

In the provided space below, briefly answer the following questions.

#### 1. Is accuracy the best metric to use on this data? Why or why not?
       Although accuracy provides a metric to evaluate the models performance, because this is a classification applicattion 
       a confusion matrix with precision, recall and an F-1 would be better suited.


#### 2. What activation functions did you choose for your output layers, and why?
       Softmax for 'Department' and sigmoid for 'Attrition' because the classification tasks were categorical and binary respectively

#### 3. Can you name a few ways that this model might be improved?
       Increased the number of training epochs from 10 to 50 and it increased the accuracy for the 'attrition output', but the 'department 
       output' remained the same. In an attempt to increase the accuracy for the 'department output' increased the number of nodes but
       the accuracy remained unchanged