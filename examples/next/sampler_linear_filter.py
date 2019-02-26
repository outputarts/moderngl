import os

import moderngl.next as mgl
import numpy as np
from PIL import Image

from window import Example, run_example

from common.simple_object_renderer import SimpleObjectRenderer


class SimpleColorTriangle(Example):
    gl_version = (3, 3)
    aspect_ratio = 1.0
    title = "Sampler Wrap Modes"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.renderer = SimpleObjectRenderer(self.ctx)

        self.vertices = np.array([
            (-0.9, -0.9),
            (-0.9, 0.9),
            (0.9, -0.9),
            (0.9, 0.9),
        ], dtype='f4')

        self.texcoords = np.array([
            (-2.0, -2.0),
            (-2.0, 3.0),
            (3.0, -2.0),
            (3.0, 3.0),
        ], dtype='f4')

        img = Image.frombytes('RGB', (8, 8), os.urandom(192))
        self.texture = self.ctx.texture(img)
        self.sampler = self.ctx.sampler(self.texture)
        self.sampler.wrap = mgl.REPEAT_X | mgl.REPEAT_Y
        self.sampler.filter = mgl.LINEAR

    def render(self, time: float, frame_time: float):
        self.ctx.clear(1.0, 1.0, 1.0)
        self.sampler.use()

        self.renderer.render(mgl.TRIANGLE_STRIP, vertices=self.vertices, texcoords=self.texcoords)

        # grid
        self.renderer.render(mgl.LINES, vertices=np.array([
            (i * 0.18, -0.9, i * 0.18, 0.9, -0.9, i * 0.18, 0.9, i * 0.18) for i in range(-5, 7, 2)
        ], 'f4').reshape(-1, 2), texture=False, color=(0.0, 0.0, 0.0, 1.0))


if __name__ == '__main__':
    run_example(SimpleColorTriangle)
