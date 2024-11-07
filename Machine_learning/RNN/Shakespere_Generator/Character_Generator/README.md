## Shakespere Generator

**The purpose of this model is to showcase the many to many variation of the Recurring Neural Network (RNN) Algorithm utilizing the Gated Recurrent Units (GRU)**
**In this variety of RNN the input has the same size as the ouput, which avoids the use of an encoder-decoder scheme. Directing the model to**
**predict the next character instead of the next word allows for a drastic reduction on the size of the input vector from thousands of**
**words to just 65 characters.**

#### Size of vocabulary
    vocabulary = sorted(set(text))
    len(vocabulary) = 65

**The sizes of the inputs and outputs is equal because a preset number of characters is selected plus one target character**

#### Example:
             Input size  = 6 
            'Example'
            
            input = ['E','x','a','m','p','l']
            ouput = [x','a','m','p','l','e']

**As you can see the input vector composed of 6 characters is used to predict the output vector which consists of the next character minus the first character**
**keeping the vector size the same.**

**To carry out this task we have employed the tensorflow's repository of shakespere texts to train the model.**
