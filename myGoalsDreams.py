import pandas as pd
from datetime import date
from PIL import Image

mytesla = Image.open('goalsANDdreams\myTesla.png')
mytesla.show()

print(date.today())

myDreams = """
DREAMS:
My purpose is to run a company that creates the best trading algorithms in the world and feel happy and fulfilled.

I have a business.

I see myself confident, patient - somebody to look up to - successful, wise and has a great character.

I am connected with my creator, I'm grateful for my life.

I love and accept myself for who I am.

Im super rich $$$,$$$,$$$,$$$

Im surrounded by people I love.

I live where I want to.

Ive got tons of energy, my body is at the greatest shape its ever been.

I have done my degrees.

I look good, I feel good.

""".title()

myGoals = """
SHORT TERM GOALS:
    Economic:
        *Develop a trading software with Shay that makes tons of money and put it to action:
            *Finish the analyst recommendations model - backtest, optimization, wrap up.
            *Start building an earnings model
        *Pass the July exams: economics, statistics & financing
            *Watch all lectures in both courses
            *Do all homework
            *Do all the previous exams
                *All by July 10-15

    Things:
        *Go to the two Tony Robbins seminars in the next 12 months
        *Put tefilin on every day, stay connected and be grateful to God
        *Go over your goals every morning and write what you're going to do today to make it a winning day.
        *Train my back to be straight: use back exercises and UPRIGHT
        *Listen to motivational stuff 5-7 times a week

    Self development:
        *Accept yourself, forgive yourself, love yourself
        *Practice mindfulness every day
        *Live healthy: eat well, do sports, sleep well
        *Master my craft: finance, computer science (data science), mathematics, statistics and probability
        *Create a financial plan
        *Raise my self esteem
        *Develop better communication skills
        *Practice confident body language and tonality
        *Read 2 books a month


""".title()

series_dictionary = {
    'Date': date.today(),
    'Dreams': myDreams,
    'Goals': myGoals
}

print(myDreams)
print(myGoals)

todays_goalsANDdreams = pd.Series(series_dictionary)

filename = 'goalsANDdreams/' + str(date.today()) + '.goalsANDdreams' + '.csv'
todays_goalsANDdreams.to_csv(filename)