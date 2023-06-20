# Program to test the $1 recognizer for the first task in the assignment
# You can see the gestures that can be recognized when you start the application the prediction is in the left corner on the bottom
# You can draw on the window using the right mouse button
import pyglet
import dollar_recognicer

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
IMAGE = pyglet.image.load('Images/recognizer/Gestures.jpeg')

circles = []
prediction = ''

def main():
    recognizer = dollar_recognicer.Dollar_Recognizer(5)
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
            # because pyglet and the recognicer samples have different 0-Points the y-values must be inverted
            logged_points.append(dollar_recognicer.Point(x, WINDOW_HEIGHT - y))
    @win.event
    # if the left mouse button is released the recognition begins
    def on_mouse_release(x, y, button, modifiers):
        global logged_points
        global circles
        global prediction
        if(button == 1):
            if(len(logged_points) > 0):
                new_prediction = recognizer.recognize(logged_points)
                prediction = new_prediction.name
                logged_points = []
            circles = []
    @win.event
    def on_draw():
        win.clear()
        IMAGE.blit(WINDOW_WIDTH/2 - IMAGE.width / 2, WINDOW_HEIGHT - IMAGE.height)
        prediction_text = f'Gesture: {prediction}'
        label = pyglet.text.Label(prediction_text, font_name='Times New Roman', font_size=24, x=0, y=5)
        label.draw()
        for circle in circles:
            circle.draw()
            

    pyglet.app.run()

main()