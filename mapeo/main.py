from manim import *

class Mapeo(Scene):

    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble("\\usepackage{mathrsfs}")

        grid = NumberPlane((-20, 20), (-10, 10))
        # Complex map
        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, .5)
        c_grid.add_coordinates()
        complex_map_words = MathTex("""En\; el\; plano\;  \\mathbb{C}: \\\\   Mapeo;\; {z \\rightarrow z^2}""", tex_template=myTemplate)
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5, background=True)
        self.play(FadeIn(complex_map_words), run_time = 2)
        self.play(
            FadeOut(grid),
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid)
        )
        self.wait()
        self.play(
            moving_c_grid.animate.apply_complex_function(lambda z: z**2),
            run_time=6,
        )
        self.wait(2)