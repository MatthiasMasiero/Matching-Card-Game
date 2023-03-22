from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
  session['card'] = ''
  return render_template("index.html")
  
@app.route('/start', methods=["GET", "POST"])
def start():
  nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
  numsShuffled = random.sample(nums, len(nums))
  session['cards'] = numsShuffled
  session['current'] = '0'
  print(numsShuffled)
  
  # if numsShuffled[0] == numsShuffled[1]:
  #   print('they match')
  # numsShuffled[0]
  return render_template("game.html", values=session['cards'])

# works when you click it to see if the numbers match
@app.route('/play', methods=["GET", "POST"])
def play():
    id = request.form['selectedCard']
    session['current'] = id
    print(session['current'])
    if session['card'] == "":
        session['card'] = id
    elif session['card'] == id:
        print("MATCH")
        session['cards'].remove(int(id))
        session['cards'].remove(int(id))
        session['card'] = ""
    else:
        session['card'] = ""
    
    print(id)
    return render_template("game.html", values=session['cards']) 
  
app.run(host='0.0.0.0', port=81, debug=True)
# if numss[1] == numss[2]:
#   print('they match')
  
# make it so if the session['card'] variable is empty it adds to it at the end if it already has something then reset it to zero can be done with if statement checking it with an empty string
# the return rendertemplate at the end shouldnt be done when there is a one pair down page open so see if it can work without that
# TODO: maybe use jinja to remove the buttons
#make it so you cant click the same button twice in a row
#mak the buttons just invisible with css

# @app.route('/card1', methods=["GET", "POST"])
# def card1():
#   print (session['cards'][0])
#   if session['card'] == session['cards'][0]:
#     print('Thats a Match')
#     if session['card'] == session['cards'][1]:
#       return render_template('34.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][2]:
#       return render_template('24.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][3]:
#       return render_template('23.html')
#       session['card'] = ''
#   else:
#     if session['card'] == '':
#       session['card'] = (session['cards'][0])
#     else:
#       session['card'] = ''
#     return render_template("game.html", card1=session['cards'][0])
#   # print(card1)
#   # return render_template("game.html")

# @app.route('/card2', methods=["GET", "POST"])
# def card2():
#   print (session['cards'][1])
#   if session['card'] == session['cards'][1]:
#     print('Thats a Match')
#     if session['card'] == session['cards'][0]:
#       return render_template('34.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][2]:
#       return render_template('14.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][3]:
#       return render_template('13.html')
#       session['card'] = ''
#   else:
#     if session['card'] == '':
#       session['card'] = (session['cards'][1])
#     else:
#       session['card'] = ''
#     return render_template("game.html", card1=session['cards'][1])

  
# @app.route('/card3', methods=["GET", "POST"])
# def card3():
#   print (session['cards'][2])
#   if session['card'] == session['cards'][2]:
#     print('Thats a Match')
#     if session['card'] == session['cards'][0]:
#       return render_template('24.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][1]:
#       return render_template('14.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][3]:
#       return render_template('12.html')
#       session['card'] = ''
#   else:
#     if session['card'] == '':
#       session['card'] = (session['cards'][2])
#     else:
#       session['card'] = ''
#     return render_template("game.html", card1=session['cards'][2])

  
# @app.route('/card4', methods=["GET", "POST"])
# def card4():
#   print (session['cards'][3])
#   if session['card'] == session['cards'][3]:
#     print('Thats a Match')
#     if session['card'] == session['cards'][0]:
#       return render_template('23.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][1]:
#       return render_template('13.html')
#       session['card'] = ''
#     elif session['card'] == session['cards'][2]:
#       return render_template('12.html')
#       session['card'] = ''
#   else:
#     if session['card'] == '':
#       session['card'] = (session['cards'][3])
#     else:
#       session['card'] = ''
#     return render_template("game.html", card1=session['cards'][3])


  


  
# while len(nums) > 0:
#   chosenNum = random.choice(nums) 
#   print(chosenNum)
#   nums = nums.pop(chosenNum)
# chosenNum2 = random.choice(nums)
# nums.pop(random.choice(nums))
# chosenNum3 = random.choice(nums)
# nums.pop(chosenNum3)
# chosenNum4 = random.choice(nums)
# nums.pop(chosenNum4)

# print(nums)
# https://note.nkmk.me/en/python-random-choice-sample-choices/
  
# app.run(host='0.0.0.0', port=81, debug=True)