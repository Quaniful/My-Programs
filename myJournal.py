import datetime
import calendar


def entry():
  user_input = input("Writing ...\n\n\n")
  return user_input


writings = ''''''
writeMore = True

while writeMore is True:
  writings += '\n\n' + entry()

  more = input(
      "'1' -->  Continue Writing\nPress any key if you're done.\n\n --> ")
  writeMore = True if more == '1' else False

seperator = '======================================================================'
day = calendar.day_name[datetime.datetime.today().weekday()]
date = datetime.date.today().strftime('%Y-%m-%d')
time = datetime.datetime.now().time().strftime('%H:%M')
drawing = r"""
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\
   //                 |                 \\
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
"""

print(seperator)
print(day)
print(date)
print(time)
print(writings)
print(r"{}".format(drawing))
print(seperator)

# Add entry to today's journal file: time, content
fname = date + '.txt'

with open('journal/{}'.format(fname), 'a') as f:
  f.writelines(['\n', seperator, '\n', day, '\n', date, '\n',
                time, writings, r"{}".format(drawing), seperator])

drawing2 = r"""
(\
\'\
 \'\     __________
 / '|   ()_________)
 \ '/    \ ~~~~~~~~ \
   \       \ ~~~~~~   \
   ==).      \__________\
  (__)       ()__________)
"""

with open('journal/diary.txt', 'a') as f:
    f.writelines(['\n', seperator, '\n', day, '\n', date, '\n',
                time, writings, '\n', r"{}".format(drawing2), seperator])
