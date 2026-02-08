from manim import *


class first_animation(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.add(square)
        self.wait(1)
        self.play(Transform(square,circle))
        self.play(square.animate.shift(2*UP), run_time=2.5)
        self.play(square.animate.set_fill(GREEN, opacity = 1))
        
        
