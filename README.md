# This code is for predicting age from radiologist report in bahasa

This code is using Python 3.7

1. Install pre-requisite from requirement.txt
```!pip3 install -r requirements.txt```

2. Clone this git repo ```git clone https://github.com/nnqomariyah/predict_age_from_radiologist_report.git```
3. Download the fasttext model from https://drive.google.com/file/d/1QSlKDlY5HkNDuQc3s_bmtEBlNk6DYf_V/view?usp=sharing, store it in the same folder as your main.py

4. run main.py ```python3 main.py```
5. put the radiologist report text in the input box, then press enter


## Example:

input text= ```YTH : Ts dr. Thorax AP : Perbandingan :24-03-2020 Cor tidak membesar.   Sinuses tajam dan diafragma normal Pulmo: Hili normal Corakan bronkovaskuler normal Tampak konsolidasi homogen dengan air bronchogram (+) di lapang tengah sampai bawah bilateral, berkurang. KESAN :   Pneumonia, dibandingkan foto sebelumnya konsolidasi tampak berkurang. Tidak tampak kardiomegali```

output of the program= ```PREDICTED AGE=  46.970093 years old```
