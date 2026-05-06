import pyray as rl
import sys
import os

rl.init_window(1280, 720, "RayEngine")
rl.set_target_fps(60)

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    sidebar_width = 200
    bottombar_height = 150

    # Tools panel (full height on right)
    rl.gui_panel(rl.Rectangle(1280 - sidebar_width - 2, 0, sidebar_width, 720), "Tools")

    # Bottom panel (Output)
    rl.gui_panel(rl.Rectangle(0, 720 - bottombar_height, 1280 - sidebar_width, bottombar_height), "Output")
    
    # Viewport (main area)
    rl.gui_panel(rl.Rectangle(0, 0, 1280 - sidebar_width, 720 - bottombar_height), "Viewport")

    rl.end_drawing()

rl.close_window()
