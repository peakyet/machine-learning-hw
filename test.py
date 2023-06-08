##########################################
## Check whether or not the Pytorch is installed correctly.
# import torch
# print("Checking Pytorch")
# x = torch.rand(5,3)
# print(x)
# print(torch.cuda.is_available())

## Check Gym environment

# import gymnasium as gym
# # env = gym.make("ALE/SpaceInvaders-v5", render_mode="human")
# env = gym.make("CartPole-v1", render_mode="human")
# observation, info = env.reset()

# for _ in range(1000):
#     action = env.action_space.sample()  # agent policy that uses the observation and info
#     observation, reward, terminated, truncated, info = env.step(action)
#     image = env.render("rgb_array")
#     print(f"image: {image}")

#     if terminated or truncated:
#         observation, info = env.reset()
    
#     env.render()

# env.close()

#######################################

# importing pyglet module

import pyglet

import pyglet.window.key

 # width of window

width = 500

 # height of window

height = 500

 # caption i.e title of the window

title = "Geeksforgeeks"

 # creating a window

window = pyglet.window.Window(width, height, title)

 # text

text = "GeeksforGeeks"

 # creating a label with font = times roman

# font size = 36

# aligning it to the center

label = pyglet.text.Label(text,

                          font_name ='Times New Roman',

                          font_size = 36,

                          x = window.width//2, y = window.height//2,

                          anchor_x ='center', anchor_y ='center')

 # on draw event

@window.event

def on_draw():

         # clearing the window

    window.clear()

         # drawing the label on the window

    label.draw()

          # key press event   

@window.event

def on_key_press(symbol, modifier):

         # key "E" get press

    if symbol == pyglet.window.key.E:

                 # close the window

        window.close()

 # dispatching window events

window.dispatch_events()

 # start running the application

pyglet.app.run()
