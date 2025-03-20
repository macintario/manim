from manim import *

class parabola(Scene):
    def construct(self):
        a = Axes(x_range = (-6, 6), x_length = 6, y_range = (-2, 10), tips = True).add_coordinates()
        parabola = a.plot(lambda x: x**2+1, color = GREEN)
        self.play(Write(a))
        self.play(Write(parabola))
        self.wait(2)