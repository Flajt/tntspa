import utils
from model import MyModel
from fasttext_vector import FastTextVector


input_texts = utils.read_lines("data/monument_600/train.en")
target_texts = utils.read_lines("data/monument_600/train.sparql")

fasttext_model = FastTextVector("data/wiki.en.bin")
model = MyModel(input_word_vector=fasttext_model, num_layers=2)
model.train(input_texts, target_texts, epochs=30)

model.save('output/my_model.h5')