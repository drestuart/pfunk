'''
Created on Jan 23, 2013

@author: dstu
'''

import Ragnarok as R
import os
import pygame

class OurHero(R.DrawableObj):
    '''
    classdocs
    '''


    def __init__(self, draw_order, update_order):

        super(OurHero, self).__init__(draw_order, update_order)
        
        texturePath = os.path.join("textures", "kuriboshoe.jpeg")
        self.sprite = R.Sprite()
        self.sprite.load_texture(texturePath)
        
        self.sprite.coords = R.Ragnarok.get_world().get_backbuffer_size() / 2.0
        self.sprite.scale = (.35, .35)
        
    def update(self, milliseconds):
        #Get the location of the mouse.
        mouse_pos = pygame.mouse.get_pos()

        #Set the location of the sun and its rays to the current mouse location.
        self.sprite.coords.X = mouse_pos[0]
        self.sprite.coords.Y = mouse_pos[1]
        
        self.sprite.update(milliseconds)
        
        super(OurHero, self).update(milliseconds)
        
    def draw(self, milliseconds, surface):
        #All we have to do now is call the draw methods of the
        #sun and sun_rays sprites to get them to draw on the screen.
        self.sprite.draw(milliseconds, surface)

        #(Optional) Call the draw method of the base class (DrawableObj).
        super(OurHero, self).draw(milliseconds, surface)
