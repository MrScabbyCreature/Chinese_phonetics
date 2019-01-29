import pandas as pd
import numpy as np
from random import shuffle
from IPython.display import display as display_dataframe

print("Practice what?\n1) Left column(hanze->pinyin) \n2) Right column(meaning->hanze+pinyin)")
choice = input()

### left column
if choice == '1':
    df = pd.read_excel("left_row.xlsx")
    if 'prob' not in df.columns:
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
        print("Show answer? (Y)")
        input()
        print("Answer is: {}".format(pinyin))
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
                print("It's okay. Next time!")
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
        df.to_excel("left_row.xlsx")
        # display_dataframe(df)


# right column
if choice == '2':
    df = pd.read_excel("right_row.xlsx")
    if 'prob1' not in df.columns or 'prob2' not in df.columns:
        df['prob1'] = 1.0
        df['prob2'] = 1.0
    def random_index(column):
        column = 'prob' + str(column)
        probability = np.random.random() * df[column].sum()
        index = 0
        for i in range(df.shape[0]):
            probability -= df[column][i]
            if probability <= 0:
                index = i
                break
        return index

    def ask_meaning_to_hanze_MCQ(index):
        hanze = df['hanze'][index]
        pinyin = df['pinyin'][index]
        meaning = df['meaning'][index]

        #getting random options
        randomized_choices = list(df['hanze'])
        randomized_choices.remove(hanze)
        shuffle(randomized_choices)
        choices = [hanze] + randomized_choices[:3]
        shuffle(choices)

        #ask the question
        print("The hanze of '{}' is:".format(meaning))
        for i in range(4):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == hanze:
                print("Correct!")
                print("Also, the pinyin is \"{}\"".format(pinyin))
                return True
            else:
                print("Oops! The answer is {}".format(hanze))
                print("Also, the pinyin is \"{}\"".format(pinyin))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

    def ask_meaning_to_pinyin_MCQ(index):
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
        print("The pinyin of '{}' is:".format(meaning))
        for i in range(4):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == pinyin:
                print("Correct!")
                print("Also, the hanze is \"{}\"".format(hanze))
                return True
            else:
                print("Oops! The answer is {}".format(pinyin))
                print("Also, the hanze is \"{}\"".format(hanze))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

    def ask_meaning_to_hanze_blank(index):
        hanze = df['hanze'][index]
        pinyin = df['pinyin'][index]
        meaning = df['meaning'][index]

        #ask the question
        print("Write the hanze of '{}' in your notebook:".format(meaning))
        print("Show answer? (Y)")
        input()
        print("Answer is: {}".format(hanze))
        print("Did you get it right?")
        choices = ['Yes!', 'No :(']
        for i in range(2):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == choices[0]:
                print("Nice!")
                print("Also, the pinyin is \"{}\"".format(pinyin))
                return True
            else:
                print("It's okay. Next time!")
                print("Also, the pinyin is \"{}\"".format(pinyin))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

    def ask_meaning_to_pinyin_blank(index):
        hanze = df['hanze'][index]
        pinyin = df['pinyin'][index]
        meaning = df['meaning'][index]

        #ask the question
        print("Write the pinyin of {} in your notebook:".format(meaning))
        print("Show answer? (Y)")
        input()
        print("Answer is: {}".format(pinyin))
        print("Did you get it right?")
        choices = ['Yes!', 'No :(']
        for i in range(2):
            print(str(i) + ") {}".format(choices[i]))
        answer = input()
        try:
            if choices[int(answer)] == choices[0]:
                print("Nice!")
                print("Also, the hanze is \"{}\"".format(hanze))
                return True
            else:
                print("It's okay. Next time!")
                print("Also, the hanze is \"{}\"".format(hanze))
                return False
        except Exception as e:
            print("Kya input karrela bhailog... -_-")

#     function = [ask_blank, ask_MCQ]
    hanze_functions = [ask_meaning_to_hanze_blank, ask_meaning_to_hanze_MCQ]
    pinyin_functions = [ask_meaning_to_pinyin_blank, ask_meaning_to_pinyin_MCQ]
    prob_change = [[1.5, 0.5],
                   [1.1, 0.9]]

    while True:
        #prob1 = meaning->hanze, prob2 = meaning->pinyin
        if np.random.random() < df['prob1'].sum() / (df['prob1'].sum() + df['prob2'].sum()):
            # meaning->hanze
            index = random_index(1) #1 for prob1
            random_choice = (np.random.random() <= df['prob1'][index])
            result = hanze_functions[random_choice](index)
            if result is not None:
                df.loc[index, 'prob1'] *= prob_change[random_choice][result]
        else:
            index = random_index(2) #1 for prob1
            random_choice = (np.random.random() <= df['prob2'][index])
            result = pinyin_functions[random_choice](index)
            if result is not None:
                df.loc[index, 'prob2'] *= prob_change[random_choice][result]
        print("\n\n")
        df.to_excel("right_row.xlsx")
        # display_dataframe(df)
