# First install  pip install pykinect
# then install pip install pygame

# Then deploy the kinect and run this code:-

import thread
import pygame
from pykinect import nui

DEPTH_WINSIZE = 320,240

screen_lock = thread.allocate()
screen = None

tmp_s = pygame.Surface(DEPTH_WINSIZE, 0, 16)


def depth_frame_ready(frame):
    with screen_lock:
        frame.image.copy_bits(tmp_s._pixels_address)
        arr2d = (pygame.surfarray.pixels2d(tmp_s) >> 7) & 255
        pygame.surfarray.blit_array(screen, arr2d)

        pygame.display.update()


def main():
    """Initialize and run the game."""
    pygame.init()

    # Initialize PyGame
    global screen
    screen = pygame.display.set_mode(DEPTH_WINSIZE, 0, 8)
    screen.set_palette(tuple([(i, i, i) for i in range(256)]))
    pygame.display.set_caption('PyKinect Depth Map Example')

    with nui.Runtime() as kinect:
        kinect.depth_frame_ready += depth_frame_ready  
        kinect.depth_stream.open(nui.ImageStreamType.Depth, 2, nui.ImageResolution.Resolution320x240, nui.ImageType.Depth)

        # Main game loop
        while True:
            event = pygame.event.wait()

            if event.type == pygame.QUIT:
                break

if __name__ == '__main__':
    main()