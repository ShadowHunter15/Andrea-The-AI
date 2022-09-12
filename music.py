import os
import random
import time
path = "C:/Users/osdrw/Desktop/Programming/M"
os.chdir(path)
music = os.listdir()
def play_music(STR=None):
    #kill_task("vlc")
    if not STR:
        clip = random.choice(music)
        clip_name = clip.replace("_", " ")
        clip_name = clip_name.replace("-", " ")
        clip_name = " ".join(clip_name.split())
        start_clip(clip)
        return ("now playing " + clip_name[0:clip_name.index("mp4")])
    elif STR:
        STR = STR.lower()
        for clip in music:
            clip = clip.lower()
            clip_name = clip.replace("_", " ")
            clip_name = clip_name.replace("-", " ")
            clip_name = " ".join(clip_name.split())
            if STR in clip_name:
                start_clip(clip)
                try:
                    return ("now playing " + clip_name[0:clip_name.index("mp4")])
                except:
                    pass
    return ("Can't seem to find it sir.")
def start_clip(clip):
    time.sleep(2)
    os.startfile(path + "/" + clip)
