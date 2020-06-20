import pandas as pd
import datetime

ascii = """
       _,    _   _    ,_
  .o888P     Y8o8Y     Y888o.
 d88888      88888      88888b
d888888b_  _d88888b_  _d888888b
8888888888888888888888888888888
8888888888888888888888888888888
YJGS8P"Y888P"Y888P"Y888P"Y8888P
 Y888   '8'   Y8P   '8'   888Y
  '8o          V          o8'
    `                     `
"""

dreams = """
*My purpose is to run a company that creates the best trading algorithms in the world and feel happy and fulfilled.
*I have a business and it's totally successful by all measures, we created the most amazing company culture.
*I want a bunch of smart, sophisticated, honest and good people to work for me, I wanna inspire all of them to be great.
*I want people to feel amazing about working for my company and make tons and tons of money there.
*I see myself confident, patient - somebody to look up to - successful, wise and has a great character.
*I am connected with my creator, I'm grateful for everything that happens for me, I'm super thankful every day.
*I live my life free of worry and stress, there's nothing good that can come from these, I choose to throw them out of my life.
*My values guide me forward.
*I'm proud of who I am, I will always be proud of who I am.
*I love and accept myself for who I am.
*I'm super rich $$$,$$$,$$$,$$$
*I'm surrounded by people I love.
*I've got tons of energy, my body is at the greatest shape its ever been.
*I promote the things I believe in.
*I help others, I know how to raise people up.
*I have a degrees in economics, computer science and mathematics.
*I look good, I feel good.
*At the 3rd stage of my life, when its time to give back, I will be ready to do some philantrophy and create a better world.
*I have a house in Israel and a house in the United States.
*I also have a vacation house at my favorite spot in the world :)
*I'm driving the coolest tesla hehe :)
"""

goals = """
_Business:
    *Close down all my debts
        * Bank 9400
        * Moran 1000
    *Develop a trading software with Shay that makes tons of money and put it to action:
        *Build an earnings model that uses option strategies
        *Finish the analyst recommendations model - backtest, optimization, wrap up.
_Things:
    *Go to the two Tony Robbins seminars in the next 12 months
    *Put tefilin on every day, stay connected and be grateful to God
    *Go over your goals every morning and write what you're going to do today to make it a winning day.
    *Train my back to be straight: use back exercises and UPRIGHT
    *Listen to motivational stuff 5-7 times a week
    *Pass the end of July exams: economics, statistics & financing
        *Watch all lectures in both courses
        *Do all homework
        *Do all the previous exams
    *Go watch an NBA game, preferably the Lakers with LeBron on the court!
_Self Development:
    *Accept yourself, forgive yourself, love yourself
    *Practice mindfulness every day
    *Live healthy: eat well, do sports, sleep well
    *Master my craft: finance, computer science (data science), mathematics, statistics and probability
    *Create a financial plan
    *Raise my self esteem
    *Develop better communication skills
    *Practice confident body language and tonality
    *Read 2 books a month
"""

dreams = dreams.split('\n')
goals = goals.split('\n')

file = './docs/' + str(datetime.datetime.now()).split(' ')[0] + '.txt'

with open(file, 'w') as f:
    def s(s): return s * 100 + '\n'

    f.write(ascii)

    f.write(s('-'))

    f.write('These are my dreams, I vow to fight for them and to protect them with my life' + '\n')
    f.write(s('-'))
    for dream in dreams:
        f.writelines(dream)
        f.write('\n')

    f.write(s('-'))
    f.write('These are my goals that I must complete, these actions will take me to my dreams' + '\n')
    f.write(s('-'))
    for goal in goals:
        f.writelines(goal)
        f.write('\n')
