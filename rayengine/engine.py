import pyray as rl
import sys
import os

# Init
rl.init_window(1280, 720, "RayEngine")
rl.set_target_fps(60)

# ----------------------
# Dark Mode Theme
# ----------------------

rl.gui_set_style(rl.DEFAULT, rl.TEXT_SIZE, 18)

rl.gui_set_style(rl.DEFAULT, rl.BACKGROUND_COLOR, rl.color_to_int(rl.Color(30, 30, 30, 255)))
rl.gui_set_style(rl.DEFAULT, rl.BASE_COLOR_NORMAL, rl.color_to_int(rl.Color(45, 45, 45, 255)))
rl.gui_set_style(rl.DEFAULT, rl.BASE_COLOR_FOCUSED, rl.color_to_int(rl.Color(60, 60, 60, 255)))
rl.gui_set_style(rl.DEFAULT, rl.BASE_COLOR_PRESSED, rl.color_to_int(rl.Color(90, 90, 90, 255)))

rl.gui_set_style(rl.DEFAULT, rl.TEXT_COLOR_NORMAL, rl.color_to_int(rl.Color(220, 220, 220, 255)))
rl.gui_set_style(rl.DEFAULT, rl.TEXT_COLOR_FOCUSED, rl.color_to_int(rl.Color(255, 255, 255, 255)))

rl.gui_set_style(rl.DEFAULT, rl.BORDER_COLOR_NORMAL, rl.color_to_int(rl.Color(70, 70, 70, 255)))

# Variables
tile_dropdown_active = 0

# Rendering Loop
while not rl.window_should_close():

    rl.begin_drawing()

    # dark background instead of white
    rl.clear_background(rl.Color(25, 25, 25, 255))

    sidebar_width = 200
    bottombar_height = 150

    # Tools panel
    rl.gui_panel(
        rl.Rectangle(1280 - sidebar_width - 2, 0, sidebar_width, 720),
        "Tools"
    )

    # Output Panel
    rl.gui_panel(
        rl.Rectangle(0, 720 - bottombar_height, 1280 - sidebar_width, bottombar_height),
        "Output"
    )


    # Viewport
    rl.gui_panel(
        rl.Rectangle(0, 0, 1280 - sidebar_width, 720 - bottombar_height),
        "Viewport"
    )

    if rl.gui_button(rl.Rectangle(1100, 50, 100, 30), "#22#Pencil"):
        print("Pencil")
    if rl.gui_button(rl.Rectangle(1100, 90, 100, 30), "#23#BigPencil"):
        print("BigPencil")
    if rl.gui_button(rl.Rectangle(1100, 130, 100, 30), "#28#Erase"):
        print("Erase")
    if rl.gui_button(rl.Rectangle(1100, 675, 150, 30), "#2#Save"):
        print("Save")

    mouse = rl.get_mouse_position()

    rl.draw_text(
        f"Mouse: {int(mouse.x)}, {int(mouse.y)}",
        10,
        30,
        20,
        rl.WHITE
    )

    rl.end_drawing()

rl.close_window()
