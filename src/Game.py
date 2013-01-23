'''
Created on Jan 23, 2013

@author: dstu
'''

import Ragnarok as r
import pygame
from OurHero import OurHero

engine = r.Ragnarok(r.Vector2(800, 600), "pFunk")


class Game(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def run(self):
        
        world = engine.get_world()
        world.clear_color = (0, 0, 0)
        
        exit_manager = ExitManager()
        hero = OurHero(1,1)
        
        world.add_obj(exit_manager)
        world.add_obj(hero)
        
        pygame.mouse.set_visible(False)
        engine.preferred_fps = 60
        engine.print_frames = False
        
        engine.run()
        
class ExitManager(r.UpdatableObj):
    """
    In this case, allows the Esc button to exit the game.
    """
    
    def update(self, milliseconds):
        if r.Ragnarok.get_world().Keyboard.is_clicked(pygame.K_ESCAPE):
            engine.exit()
        