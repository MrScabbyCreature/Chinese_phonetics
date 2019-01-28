import pandas as pd
import numpy as np
from random import shuffle
from IPython.display import display as display_dataframe

print("Practice what?\n1) Left column(hanze->pinyin) \n2) Right column(meaning->hanze+pinyin)")
choice = input()

### left column
if choice == '1':
    df = pd.read_excel("left_row.xlsx")
    df['prob'] = 1.0
    def random_index():
        probability = np.random.random() * df['prob'].sum()
        index = 0
        for i in range(df.shape[0]):
            probability -= df['prob'][i]
            if probability <= 0:
                index = i
                break
        return index

    def ask_MCQ(index):
        hanze = df['hanze'][index]
        pinyin = df['pinyin'][index]
        meaning = df['meaning'][index]

        #getting random options
        randomized_choices = list(df['pinyin'])
        randomized_choices.remove(pinyin)
        shuffle(randomized_choices)
        choices = [pinyin] + randomized_choices[:3]
        shuffle(choices)

        #ask the question
        print("The pinyin of {} is:".format(hanze))
        for i in range(4):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == pinyin:
                print("Correct!")
                print("Also, the meaning is \"{}\"".format(meaning))
                return True
            else:
                print("Oops! The answer is {}".format(pinyin))
                print("Also, the meaning is \"{}\"".format(meaning))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

    def ask_blank(index):
        hanze = df['hanze'][index]
        pinyin = df['pinyin'][index]
        meaning = df['meaning'][index]

        #ask the question
        print("Write the pinyin of {} in your notebook:".format(hanze))
        print("Did you get it right?")
        choices = ['Yes!', 'No :(']
        for i in range(2):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == choices[0]:
                print("Nice!")
                print("Also, the meaning is \"{}\"".format(meaning))
                return True
            else:
                print("It's okay. The answer is {}.".format(pinyin))
                print("Also, the meaning is \"{}\"".format(meaning))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

    function = [ask_blank, ask_MCQ]
    prob_change = [[1.5, 0.5],
                   [1.1, 0.9]]

    #main loop
    while True:
        index = random_index()
        random_choice = (np.random.random() <= df['prob'][index])
        result = function[random_choice](index)
        if result is not None:
            df.loc[index, 'prob'] *= prob_change[random_choice][result]
        print("\n\n")
        # display_dataframe(df)


#right column
if choice == '2':
    pass
