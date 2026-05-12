# RayEngine
This is RayEngine! A game engine being made with pyray.

Features (to come):
1. In the output window will be a command line in you selected project
2. there will be commands like cd, ls, load {name} <- {name} can be image.png, player.json, almost anything
3. loading a png file with its size being a multiple of 16 it will be split up into 16x16 tiles then the tile set will be put in the tileset dropdown in the tools sidebar
4. for example, player.json will contain tile name, animation frames, movesets, imagepaths, ext. then simply doing load player.json will load the player as a tile <- see rayengine/TestProject/json/player.json for extra
5. runtime.py (or runtime.c) will be updated by the engine on what you add (i think)
6. saving a level will save as .json
7. to set a path between levels it will use a node editor with ribbon lines (like visual scripting) but you load the level.json


Requirements:

pip install pyray

Ubuntu/Debian:
sudo apt install python3-tk
Fedora/Bazzite:
sudo dnf install python3-tkinter

Ill probably make a itch.io soon or patreon
DM me on discord! propro_9
