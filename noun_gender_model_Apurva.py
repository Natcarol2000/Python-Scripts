import tensorboard
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize,wordpunct_tokenize
import re
import os
import io
import sys
from pathlib import Path
import numpy as np
import numpy
import tensorflow as tf
import datetime
import tensorflow_datasets as tfds
from tensorflow.keras.layers import Activation, Dense, Embedding,Dropout,LSTM
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorboard.plugins import projector

tf.config.list_physical_devices('GPU')

while True:
    try:
        file_to_open =Path(input("Please, insert your file path: "))
        with open(file_to_open,'r', encoding="utf-8") as f:
            words = f.read()
            break         
    except FileNotFoundError:
        print("\nFile not found. Better try again")
    except IsADirectoryError:
        print("\nIncorrect Directory path.Try again")

corpus=words.split('\n')

n = len(corpus)//2
print(n)

tlabel = []
tword = []
for i in range(0,n,2):
  tlabel.append(corpus[i])
  tword.append(corpus[i+1])

text = "\n".join(tword)
print("The total number of characters in the entire code : {}".format(len(text)))


#create characters to index mapping
chars = sorted(list(set(text)))
#set will make use of no repeating character present 
#we then convert that set into list by typecasting it and then sort the list 

char_index = dict((c,i) for i,c in enumerate(chars))
#char index will store the character as key and the integer as value 

index_char = dict((i,c) for i,c in enumerate(chars))
#index char will store the integer as key and character as value

index_char

print("Vocabulary size : {}".format(len(chars)))

data = pd.DataFrame(data = list(zip(tword, tlabel)), columns = ['word', 'label'])
data.head(10)

data.info()

y = data.label.value_counts()


y = data['label'].values
X = np.array(data["word"])


from sklearn.preprocessing import LabelEncoder
Y = data.label
le = LabelEncoder()

Y = le.fit_transform(Y)


Y = Y.reshape(-1,1)

len(X)

sequences = list()
for line in X:
	# integer encode line
	encoded_seq = [char_index[char] for char in line]
	# store
	sequences.append(encoded_seq)



padded_inputs = tf.keras.preprocessing.sequence.pad_sequences(
    sequences, padding="post"
)


ex = tf.keras.preprocessing.sequence.pad_sequences(sequences, padding="pre")


#And here is the train_test_split
X_train, X_test, y_train, y_test = train_test_split(padded_inputs, Y, test_size= 0.2, random_state = 0)

X_train

y_train = y_train.astype("int32")

y_train

X_train.shape

X_test

print(X_train.shape)
print(X_test)


max_len = 21

max_words = 57

from tensorflow.keras.optimizers import RMSprop

def RNN():
    inputs = tf.keras.Input(name='inputs',shape=[max_len])
    layer = Embedding(max_words,21,input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = tf.keras.Model(inputs=inputs,outputs=layer)
    return model

model = RNN()
model.summary()
model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])

num_epochs = 120
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
history=model.fit(X_train, y_train,batch_size=128, epochs= num_epochs, validation_split=0.2, callbacks=[tensorboard_callback], verbose=2)


import matplotlib.pyplot as plt



def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()
  
plot_graphs(history, "accuracy")
plot_graphs(history, "loss")


accr = model.evaluate(X_test,y_test)


print('Test set\nLoss: {:0.3f}\nAccuracy: {:0.3f}'.format(accr[0],accr[1]))



yhat = model.predict(X_test)
# connect predictions with outputs
for i in range(100):
    print("Word = " + str (X[i]) + " \t Pridected label probability = " + str (yhat[i]) + " \t Ground Truth " + str(y_test[i]))

vocab = []
for key in char_index.keys(): 
        vocab.append(key) 
print(vocab)

weights = model.get_layer('embedding').get_weights()[0]
print(weights.shape)

out_v = io.open('vecs.tsv', 'w', encoding='utf-8')
out_m = io.open('meta.tsv', 'w', encoding='utf-8')

for num, word in enumerate(vocab):
    if num == 0: continue # skip padding token from vocab
    vec = weights[num]
    out_m.write(word + "\n")
    out_v.write('\t'.join([str(x) for x in vec]) + "\n")
out_v.close()
out_m.close()

try:
    from google.colab import files
except ImportError:
    pass
else:
    files.download('vecs.tsv')
    files.download('meta.tsv')

