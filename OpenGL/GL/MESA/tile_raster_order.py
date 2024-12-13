'''OpenGL extension MESA.tile_raster_order

This module customises the behaviour of the 
OpenGL.raw.GL.MESA.tile_raster_order to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the sampling-from-the-framebuffer behavior provided
	by GL_ARB_texture_barrier to allow setting the rasterization order of the
	scene, so that overlapping blits can be implemented.  This can be used for
	scrolling or window movement within in 2D scenes, without first copying to
	a temporary.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/tile_raster_order.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.MESA.tile_raster_order import *
from OpenGL.raw.GL.MESA.tile_raster_order import _EXTENSION_NAME

def glInitTileRasterOrderMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION