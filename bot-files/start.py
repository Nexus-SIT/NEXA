import multiprocessing
from eyeroll import run_eye_animation
from speak import voice_to_text,speak
from capture import start_cam,get_base64
from main import core_Ai
def func1():
    run_eye_animation()

def func2():
    start_cam()

def func3():
    while True:
        voice_text=voice_to_text()
        if voice_text:
            imgbase64=get_base64()
            if imgbase64:
                response=core_Ai(voice_text,imgbase64)
                speak(response)
        
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=func1)
    p2 = multiprocessing.Process(target=func2)
    p3=multiprocessing.Process(target=func3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()