#############################################################################
#
# Copyright (c) 2008 by Casey Duncan and contributors
# All Rights Reserved.
#
# This software is subject to the provisions of the MIT License
# A copy of the license should accompany this distribution.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#
#############################################################################
""" Magnet.py

	Demos the magnet controller. Electrons orbit protons.
"""

__version__ = '$Id: magnet.py 104 2008-11-08 06:49:41Z andrew.charles $'

from pyglet import image
from pyglet.gl import *

import os, math

from lepton import Particle, ParticleGroup, default_system , ParticleSystem
from lepton.renderer import BillboardRenderer
from lepton.texturizer import SpriteTexturizer
from lepton.emitter import StaticEmitter
from lepton.controller import Movement
import whael.Utilities.Constant as CONST

class Sun:
    #protons = ParticleGroup(renderer=BillboardRenderer(SpriteTexturizer(self.texture.id)),
    #                       controllers=[
    #                            Movement(),
    #                        ])
    #proton_emitter = StaticEmitter(
    #    template=Particle(
    #        size=(30, 30, 100),
    #        color=(1.0, 0.4, 0, 0.2),
    #    ),
    #    size=[(200, 200, 100)],
    #    deviation=Particle(
    #        rotation=(0, 0, math.pi / 10),
    #    ))

    def initial(self):
        self.otherp = ParticleSystem()
        self.texture = image.load('assets/flare3.png').get_texture()
        protons = ParticleGroup(renderer=BillboardRenderer(SpriteTexturizer(self.texture.id)),
                                controllers=[
                                    Movement(),
                                ])
        proton_emitter = StaticEmitter(template=Particle(size=(30, 30, 100), color=(1.0, 0.4, 0, 0.2), ), size=[(200, 200, 100)],
                                       deviation=Particle(rotation=(0, 0, math.pi / 10), ))
        aura = ParticleGroup(renderer=BillboardRenderer(SpriteTexturizer(self.texture.id)),
                                controllers=[
                                    Movement(),
                                ])
        aura_emitter = StaticEmitter(template=Particle(size=(10, 10, 100), color=(0.0, 0.4, 0, 0.2), ),
                                       size=[(1000, 1000, 1000)],
                                       deviation=Particle(rotation=(0, 0, math.pi / 10), ))
        self.otherp.add_group(protons)
        self.otherp.add_group(aura)
        proton_emitter.emit(2, protons)
        aura_emitter.emit(1,aura)

    def sep(self):
        pyglet.clock.schedule_interval(self.otherp.update, (1.0 / 30.0))

    def getDefault(self):
        return default_system

    def drawSun(self,time,width,height,offset):
        # adjust the time of the sun's translation here

        #implement delay for the moon
        if (offset < height) == 0:
            offset=0

        # it would need to transverse within 15 minutes
        glTranslatef(50 + offset, offset, 0)
        self.draw()

    def draw(self):
        #glBindTexture(self.texture.target, self.texture.id)
        self.otherp.draw()
        glLoadIdentity()


