from xgboost import XGBRegressor
import pandas as pd
import fasttext


ft = fasttext.load_model('drive/MyDrive/NNQ/cc.id.300.bin')
str1=input()
myvec=ft.get_sentence_vector(str1)

model=XGBRegressor(objective='reg:squarederror')
model.load_model('predictage.txt')
print("PREDICTED AGE= ",model.predict([1,sum(myvec)])[0], 'years old')
