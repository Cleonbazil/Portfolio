## Shakespere Generator

**The purpose of this model is to showcase the many to many variation of the Recurring Neural Network (RNN) Algorithm utilizing the Long Short Term**
**Memory(LSTM), in this variety of RNN the input has the same size as the ouput, which avoids the use of an encoder-decoder scheme. Directing the model to**
**predict the next word instead of the next character dramtically increased the size of the input vector from 65 in the character generator to  approximately**  **18,000 .**

**The corpus was preprocessed and tokenized in this step special characters and stopwords were removed, which might have hindered model performance, this warrants further investigation. Another aspect of the text processing which might also have affected performacde was the length of the input sequence wich was 4, in an atttempt to allow the model have a thourough training phase.**

**Below we have the model insatanciation, although it was not very big its size proved to much for my computers capacity. The model was trained for 1000 epochs 
and it took approxiamtely 48 hours to train yielding an accuracy of about 25% wich is far from ideal.**

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 4, 4)              72936     
                                                                 
 lstm (LSTM)                 (None, 4, 100)            42000     
                                                                 
 lstm_1 (LSTM)               (None, 100)               80400     
                                                                 
 dense (Dense)               (None, 100)               10100     
                                                                 
 dense_1 (Dense)             (None, 18234)             1841634   
                                                                 
=================================================================
Total params: 2047070 (7.81 MB)
Trainable params: 2047070 (7.81 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________


**The model evaluation results are shown below:**

#### Original text
origin_text = '  From fairest creatures we desire increase'
#### Number of predicted words
number_of_words = 40

#### Predicted text
**F r o m   f a i r e s t   c r e a t u r e s   w e   d e s i r e   i n c r e a s e   a n d   a n d   a n d   a b u n d a n t   l i b e r a l   a n d   a n d   a n d   t a r r y   w o u l d   a b u n d a n t   a n d   a n d   a n d   a n d   a n d   a b u n d a n t   a n d   t a r r y   a n d   a n d   a b u n d a n t   a n d   a n d   a n d   a n d   a n d   a n d   a n d   a n d   a n d   w o u l d   a b u n d a n t   a n d   a n d   w o u l d   a n d   a n d   a b u n d a n t   a n d**









