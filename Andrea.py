import os
import time
import playsound
import pyttsx3
import ctypes
import speech_recognition as sr
from datetime import datetime
from gtts import gTTS
from music import play_music
import random
import requests
from vosk import Model, KaldiRecognizer
import pyaudio
import PressKeys
import wall
import Constants
import TicTacToeAI

#start variables
#end of start variables

model = Model(r"C:\Users\osdrw\Desktop\Programming\AndreaTheAI\model")
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
Gender = 1
Engine = pyttsx3.init()
Engine.setProperty("voice", Engine.getProperty("voices")[Gender].id)
Engine.setProperty("rate", 145)
Master = "Omar"
def PlayXO():
    speak("I will wreck you")
    SET = Constants.SET
    depth = 0
    speak(
    """Choose difficulty: 

        Easy: 1,
        Medium: 2,
        Hard: 3,
    """)
    try:
        depth = SET[can(get_audio())]
    except:
        PlayXO()
    TicTacToeAI.depth[0] = depth
    board = ["1","2","3","4","5","6","7","8","9"]
    def display_board():
            print("")
            print(" | " + board[0] + " | " +board[1] + " | " + board[2] + " | ")
            print(" | " + board[3] + " | " +board[4] + " | " + board[5] + " | ")
            print(" | " + board[6] + " | " +board[7] + " | " + board[8] + " | ")
            print("")
    display_board()
    def wincheck(mark):
            return((board[0]==mark and board[1]== mark and board[2]==mark )or #for row1 
                (board[3]==mark and board[4]==mark and board[5]==mark )or
                (board[6]==mark and board[7]==mark and board[8]==mark )or
                (board[0]==mark and board[3]==mark and board[6]== mark )or
                (board[1]==mark and board[4]==mark and board[7]==mark )or
                (board[2]==mark and board[5]==mark and board[8]==mark )or
                (board[0]==mark and board[4]==mark and board[8]==mark )or
                (board[2]==mark and board[4]==mark and board[6]==mark ))
    def make_turn(turn, pos):
        if turn:
            letter = "O"
        else:
            letter = "X"
        board[pos-1] = letter
        display_board()
    turn = random.randint(0, 1)
    #display_board()
    while True:
        if turn:
            player = "O"
        else:
            player = "X"
        if player == "O":
            try:
                speak("your turn")
                move = can(get_audio())
                move = move.split()
                pos= SET[move[-1]]
            except:
                continue
        else:
            pos = TicTacToeAI.bestMove(board)
            speak("I choose " + str(pos))
        if board[pos-1] in ["X", "O"]:
            speak("Taken, choose another")
            continue
        make_turn(turn, pos)
        if wincheck(player):
            speak(player + " wins!")
            if player == "X":
                speak("Lol, get good sucker")
            else:
                speak("That was just luck")
            return 
        for i in ["1","2","3","4","5","6","7","8","9"]:
            if i in board:
                break
            else:
                if i == "9":
                    speak("Draw")
                    return
        turn = not turn
        print("-" * 20)
def can(x):
    if x:
        return x[x.index(': "')+3:-3]

def get_audio():
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            res = recognizer.Result()
            if len(can(res)) > 1:
                return res

def internet_on():
        try:
            _ = requests.head(url='http://www.google.com/', timeout=5)
            return True
        except requests.ConnectionError:
            return False
print("Done")
Greet = "Hello {name}, I am Andrea your personal assistant, how can I help you?".format(name = Master)
def speak(Str):
    if internet_on():
        tts = gTTS(text=Str, lang="en")
        audio = "audio_" + str(random.randint(0, 100000000)) + ".mp3"
        tts.save(audio)
        playsound.playsound(audio)
        print(Str)
        os.remove(audio)
    else:
        Engine.say(Str)
        Engine.runAndWait()
        print(Str)
def kill_task(STR):
    file = open("C:/Users/osdrw/Desktop/Programming/Python/Task Killer/processes.txt", "w")
    file.write(os.popen("wmic process get description, processid").read())
    file.close()
    file = open("C:/Users/osdrw/Desktop/Programming/Python/Task Killer/processes.txt", "r")
    for i, j in enumerate(file.readlines()):
        if STR + ".exe" in j:
            os.kill(int(j.split()[1]), -1)
            file.close()
            break
def get_Time():
    now = datetime.now()
    current_time = now.strftime("%H, %M, %S")
    return current_time
def check_respones(arr, STR):
    for i in arr:
        if i in STR:
            return True
    return False
def pastPapermode():
    SET = Constants.SET
    speak("past paper mode now active")
    while True:
        paper = can(get_audio())
        paper = paper.split()
        if "exit" in paper:
            speak("quitting past paper mode")
            break
        try:
            year, season, version = paper[1:3], paper[0], paper[3:]
            year = SET[" ".join(year)]
            print(version)
            if len(version) > 1:
                version = SET[" ".join(version)]-1980
            else:
                print(version)
                version = SET[version[0]]
            print(version)
            if season == "november":
                season = "Oct_Nov"
            if season == "june":
                season = "May_June"
            if season == "february" or season == "january":
                season = "Jan_Feb"
            path = "C:/Users/Studying/Desktop/2Kewl4Skewl/AS/Biology - 9700/" + str(year) + "/" + season
            os.chdir(path)
            print(path)
            for i in os.listdir():
                if "ms" in i:
                    curr = i.split("_ms_")
                    if str(version) == (curr[1].split("."))[0]:
                        os.startfile(path + "/" + i)
                        break
            time.sleep(2)
            speak("Done")
        except :
            pass
def process_input(STR):
    if check_respones(["x o", "xo", "toe", "tic"], STR):
        PlayXO()
    if check_respones("yourself", STR):
        pass
        #kill
    if check_respones(["past", "pass", "mode", "enter"], STR):
        speak("entering past paper mode.")
        pastPapermode()
    if check_respones(["wallpaper", "wall paper", "change"], STR):
        wall.random_wallpaper()
        speak("Here's a nice one sir")
    STR = STR.lower()
    if check_respones(["look", "lock", "log", "luck"], STR):
        ctypes.windll.user32.LockWorkStation()
    if "music" in STR:
        speak("what do you want to play sir?")
        speak(play_music(can(get_audio())))
    if "hi" == STR or "hello" == STR:
        speak("Hello sir")
    if "how are" in STR:
        speak("I'm Great")
    if "thank" in STR:
        speak("Anytime sir.")
    if "andr" in STR:
        if "hi" in STR or "hello" in STR:
            speak("Hi sir")
        else:
            if len(STR.split()) == 1:
                speak("yes sir")
    if "time" in STR:
        speak(get_Time())
speak(Greet)
while True:
    x = get_audio()
    process_input(can(x))
