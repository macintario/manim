from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        equations = [
            MathTex("a","x","^","2","+","b","x","+","c","=","0"),
            MathTex("a","x","^","2","+","b","x","=","-","c"),
            MathTex("x","^","2","+","{ ","{","b","}","\over","{","a","} }","{x}","=","-","{ {c}\over{","a","} }"),
            MathTex("x","^","2","+","{ ","{","b","}","\over","{","a","}"," }","{x}","+\left(\dfrac{b}{2a}",r"\right)^2=","-",r"{ {c}\over{","a","} }",r"+\left(\dfrac{b}{2a}\right)^2",font_size=20),
            MathTex(r"\left( {x}+{ {b}\over{2a} }\right)^2=-\dfrac{c}{a}+\dfrac{b^2}{4a^2}",font_size=20),
            MathTex(r"\left(x+\dfrac{b}{2a}\right)^2=-{ {4ac}\over{4a^2} }+{ {b^2} \over{4a^2} }", font_size=20),
            MathTex(r"\left(x+\dfrac{b}{2a}\right)^2={ { {b^2}-4ac}\over{4a^2} }", font_size=20),
            MathTex(r"\sqrt{\left({x+\dfrac{b}{2a} }\right)^2}","=",r"\sqrt{{b^2-4ac}","\over","{4a^2}}", font_size=20),
            MathTex(r"{ x+\dfrac{b}{2a} }","=","\pm\dfrac{\sqrt{b^2-4ac}}{2a}", font_size=22),
            MathTex(r"x","=","-\dfrac{b}{2a}\pm\dfrac{\sqrt{b^2-4ac}}{2a}", font_size=24),
            MathTex(r"x","=","\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}", font_size=26),
        ]

        # Add the first equation to the scene

        self.add(equations[0])
        self.wait(2)

    # Loop through the equations and apply TransformMatchingTex
        for i in range(1, len(equations)):
            self.play(TransformMatchingTex(equations[i - 1], equations[i], transform_mismatches=False))
            self.wait(1)