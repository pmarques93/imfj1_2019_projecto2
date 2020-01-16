# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()
    pygame.mouse.set_visible(False)

    # Define the size/resolution of our window
    res_x = 800
    res_y = 600

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("FPS Scene")
    scene.camera = Camera(False, res_x, res_y)

    # Sets Camera Position
    scene.camera.position -= vector3(0,-0.5,1)

    # Create a cube and place it in a scene
    cube1 = Object3d("Cube")
    cube1.scale = vector3(2, 2, 2)
    cube1.position = vector3(-2, 0, 3)
    cube1.mesh = Mesh.create_Cube((1, 1, 1))
    cube1.material = Material(color(0,1,0,1), "CubeMaterial")
    scene.add_object(cube1)

    # Create a cube and place it in a scene
    cube2 = Object3d("Cube2")
    cube2.scale = vector3(7, 7, 7)
    cube2.position = vector3(-2, 2, 10)
    cube2.mesh = Mesh.create_Cube((1, 1, 1))
    cube2.material = Material(color(1,1,0,1), "CubeMaterial")
    scene.add_object(cube2)

    # Create a pyramid and place it in a scene
    pyr1 = Object3d("Pyramid")
    pyr1.scale = vector3(2, 2, 2)
    pyr1.position = vector3(2, 0, 3)
    pyr1.mesh = Mesh.create_Pyramid((1, 1, 1))
    pyr1.material = Material(color(1,0,1,0), "PyramidMaterial")
    scene.add_object(pyr1)

    # Create a pyramid and place it in a scene
    pyr2 = Object3d("Pyramid")
    pyr2.scale = vector3(10, 10, 10)
    pyr2.position = vector3(10, 4, 8)
    pyr2.mesh = Mesh.create_Pyramid((1, 1, 1))
    pyr2.material = Material(color(1,1,1,0), "PyramidMaterial")
    scene.add_object(pyr2)

    # Timer
    delta_time = 0
    prev_time = time.time()

    # keys
    aKey = False
    dKey = False
    wKey = False
    sKey = False
    qKey = False
    eKey = False

    # keys list
    keys = [
        aKey, dKey, wKey, sKey, qKey, eKey
    ]
    
    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):   
                    aKey = True
                if (event.key == pygame.K_d):
                    dKey = True
                if (event.key == pygame.K_w):
                    wKey = True
                if (event.key == pygame.K_s):
                    sKey = True
                if (event.key == pygame.K_q):
                    qKey = True
                if (event.key == pygame.K_e):
                    eKey = True

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_a):   
                    aKey = False
                if (event.key == pygame.K_d):
                    dKey = False
                if (event.key == pygame.K_w):
                    wKey = False
                if (event.key == pygame.K_s):
                    sKey = False
                if (event.key == pygame.K_q):
                    qKey = False
                if (event.key == pygame.K_e):
                    eKey = False

        # walking keys
        if aKey:
            scene.camera.position += vector3(-0.02,0,0)
        if dKey:
            scene.camera.position += vector3(0.02,0,0)
        if wKey:
            scene.camera.position += vector3(0,0,0.02)
        if sKey:
            scene.camera.position += vector3(0,0,-0.02)

        # get mouse pos (to rotate camera)
        if (pygame.mouse.get_rel()[0]) < 0: #quando olha para a esquerda
            pass
        if (pygame.mouse.get_rel()[0]) > 0: #quando olha para a direita
            pass
        if (pygame.mouse.get_rel()[1]) > 0: #quando olha para a baixo
            pass
        if (pygame.mouse.get_rel()[1]) < 0: #quando olha para a baixo
            pass
            
        

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()

# Run the main function
main()
