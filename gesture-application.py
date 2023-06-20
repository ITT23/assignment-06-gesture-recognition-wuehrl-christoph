# This application controls your media player with gestures based on the $1 recognizer
# The different gestures and there effect are displayed when your start the application
# To draw in the window you have to press only the left mouse button
import pyglet
import dollar_recognicer
from pynput.keyboard import Key, Controller

KEYBOARD = Controller()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGE = pyglet.image.load('Images/controller/Gestures.jpeg')
# Photo by Lee  Campbell on Unsplash (https://unsplash.com/photos/1w1OMV8CEeM)
BACKGROUND = pyglet.image.load('Images/controller/Background.jpeg')

circles = []

def main():
    recognizer = dollar_recognicer.Dollar_Recognizer(3)
    win = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    @win.event
    def on_mouse_press(x, y, button, modifiers):
        global logged_points
        if(button == 1):
            logged_points = []
    # points are gathered an displayed when the mouse is dragged with the left mouse button hold
    @win.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        global logged_points
        global circles
        if(buttons == 1):
            circles.append(pyglet.shapes.Circle(x, y, 3, color=(255,255,255)))
            # because pyglet and the recognizer samples have different 0-Points the y-values must be inverted
            logged_points.append(dollar_recognicer.Point(x, WINDOW_HEIGHT - y))
    # if the left mouse button is released the recognition begins
    @win.event
    def on_mouse_release(x, y, button, modifiers):
        global logged_points
        global circles
        if(button == 1):
            if(len(logged_points) > 0):
                prediction = recognizer.recognize(logged_points)
                control_media_player(prediction.name)
                logged_points = []
            circles = []
    @win.event
    def on_draw():
        win.clear()
        BACKGROUND.blit(0, WINDOW_HEIGHT - BACKGROUND.height)
        IMAGE.blit(WINDOW_WIDTH/2 - IMAGE.width / 2, WINDOW_HEIGHT - IMAGE.height)
        for circle in circles:
            circle.draw()
        
        
        

    pyglet.app.run()


# function to translate the prediction
def control_media_player(label):
    if(label == 'x'):
        start_stop()
    elif(label == 'caret'):
        volume_up()
    elif(label == 'v'):
        volume_down()

#methods to control the media player
def volume_up():
    KEYBOARD.press(Key.media_volume_up)
    KEYBOARD.release(Key.media_volume_up)

def volume_down():
    KEYBOARD.press(Key.media_volume_down)
    KEYBOARD.release(Key.media_volume_down)

def start_stop():
    KEYBOARD.press(Key.media_play_pause)
    KEYBOARD.release(Key.media_play_pause)


main()