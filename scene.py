# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from optparse import TitledHelpFormatter
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):
    # Draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    # Draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4,
        scene_width, scene_height, width=0, fill="cyan1")

    # Draw sun
    diameter = 100
    x = 600
    y = 350
    draw_oval(canvas, x, y, x + diameter, y + diameter, outline="yellow", 
    fill="yellow")

    draw_oval(canvas, 200, 400, 600, 300, outline="ghostWhite", fill="ghostWhite")
    draw_oval(canvas, 150, 450, 450, 350, outline="ghostWhite", fill="ghostWhite")


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width,scene_height /
        4, width=0, fill="green1")

    # Tree 1
    tree_center_x = 450
    tree_bottom = 100
    tree_height = 600
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Tree 2
    tree_center_x = 300
    tree_bottom = 70
    tree_height = 400
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Tree 3
    tree_center_x = 150
    tree_bottom = 100
    tree_height = 600
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw Flowers
    diameter = 12
    space = 30
    interval = diameter + space
    x = 15
    y = 25
    for i in range(18):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="orange",
        fill="orange")
        x += interval

    diameter = 12
    space = 30
    interval = diameter + space
    x = 25
    y = 15
    for i in range(18):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="orange",
        fill="orange")
        x += interval

    diameter = 12
    space = 30
    interval = diameter + space
    x = 15
    y = 15
    for i in range(18):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="orange",
        fill="orange")
        x += interval

    diameter = 12
    space = 30
    interval = diameter + space
    x = 25
    y = 25
    for i in range(18):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="orange",
        fill="orange")
        x += interval
    
    diameter = 12
    space = 30
    interval = diameter + space
    x = 20
    y = 20
    for i in range(18):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="gold1",
        fill="gold1")
        x += interval






def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 20
    trunk_height = height / 5
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, 
    bottom, outline="darkOrchid3", width=1, fill="darkOrchid3")

    skirt_width = height / 6
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = (bottom + height) / 1.5


    draw_polygon(canvas, center_x, skirt_top, skirt_right,
    trunk_top, skirt_left, trunk_top, outline="deepPink1", width=0, fill="deepPink1")



# Call the main function so that
# this program will start executing.
main()