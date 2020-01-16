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
    scene.camera.position -= vector3(0,-1,1)
    
    #empty list for objects
    objectList = []
    
    # Create a cube and place it in a scene
    cube1 = Object3d("Cube")
    cube1.scale = vector3(2, 2, 2)
    cube1.position = vector3(-2, 1, 11)
    cube1.mesh = Mesh.create_Cube((1, 1, 1))
    cube1.material = Material(color(0,1,0,1), "CubeMaterial")
    scene.add_object(cube1)

    # Create a cube and place it in a scene
    cube2 = Object3d("Cube2")
    cube2.scale = vector3(7, 7, 7)
    cube2.position = vector3(-2, 3.5, 18)
    cube2.mesh = Mesh.create_Cube((1, 1, 1))
    cube2.material = Material(color(1,1,0,1), "CubeMaterial")
    scene.add_object(cube2)

    # Create a pyramid and place it in a scene
    pyr1 = Object3d("Pyramid")
    pyr1.scale = vector3(2, 2, 2)
    pyr1.position = vector3(2, 1, 11)
    pyr1.mesh = Mesh.create_Pyramid((1, 1, 1))
    pyr1.material = Material(color(1,0,1,0), "PyramidMaterial")
    scene.add_object(pyr1)

    # Create a pyramid and place it in a scene
    pyr2 = Object3d("Pyramid")
    pyr2.scale = vector3(10, 10, 10)
    pyr2.position = vector3(10, 5, 16)
    pyr2.mesh = Mesh.create_Pyramid((1, 1, 1))
    pyr2.material = Material(color(1,1,1,0), "PyramidMaterial")
    scene.add_object(pyr2)

    objectList.append(cube1)
    objectList.append(cube2)
    objectList.append(pyr1)
    objectList.append(pyr2)

    #angle
    angle = 15

    #axis
    axis = vector3(0,0,0)   

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
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_ESCAPE:
                    return
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

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())

        #locks mouse and its position
        pygame.event.set_grab(True)
        mp = pygame.mouse.get_rel()

        # get mouse pos (to rotate camera)
        if (mp[0]) < 0:#quando olha para a esquerda
            axis = vector3(0,1,0)   
            scene.camera.rotation = q * scene.camera.rotation

        if (mp[0]) > 0: #quando olha para a direita
            axis = vector3(0,-1,0)   
            scene.camera.rotation = q * scene.camera.rotation
            
        if (mp[1]) > 0: #quando olha para a cima
            axis = vector3(-1, 0,0)   
            scene.camera.rotation = q * scene.camera.rotation

        if (mp[1]) < 0: #quando olha para a baixo
            axis = vector3(1, 0,0)   
            scene.camera.rotation = q * scene.camera.rotation
        
        if (mp[0]) > 0 and (mp[1]) < 0: #quando olha para direita e para cima
            axis = vector3(1,-1,0)   
            scene.camera.rotation = q * scene.camera.rotation

        if (mp[0]) > 0 and (mp[1]) > 0: #quando olha para direita e para baixo
            axis = vector3(-1,-1,0)   
            scene.camera.rotation = q * scene.camera.rotation

        if (mp[0]) < 0 and (mp[1]) > 0: #quando olha para esquerda e para baixo
            axis = vector3(-1,1,0)   
            scene.camera.rotation = q * scene.camera.rotation
        
        if (mp[0]) < 0 and (mp[1]) < 0: #quando olha para esquerda e para cima
            axis = vector3(1,1,0)   
            scene.camera.rotation = q * scene.camera.rotation

        
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
