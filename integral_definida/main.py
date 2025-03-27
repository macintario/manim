from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        texts = [
            Title("Calcular la siguiente integral definida"),
            Title("Identificar la integral indefinida"),
            Title("Primero encontramos la primitiva \\newline (integral indefinida) de la función"),
            Title("Separando en términos"),
            Title("Primer término"),
            Title("Segundo término"),
            Title("Tercer término"),
            Title("Combinando resultados"),
            Title("Evaluamos la primitiva en los límites de integración \\newline  \( x  = 1 \) y  \(x = 2 \)"),
            Title("Calculamos en  \( x = 2 \):"),
            Title("Calculamos en  \( x = 1 \):"),
            Title("Restar los resultados"),
            Title("Respuesta"),
        ]

        equations = [
            MathTex("\\int_{1}^{2} \\left( 3x^2 + 2x - 5 \\right) \\, dx"),
            MathTex("\\int_{1}^{2} \\left( 3x^2 + 2x - 5 \\right) \\, dx"),
            MathTex("f(x) = 3x^2 + 2x - 5" ),
            MathTex(r"\int \left( 3x^2 + 2x - 5 \right) \, dx = \int 3x^2 \, dx + \int 2x \, dx - \int 5 \, dx"),
            MathTex(r"1. \displaystyle \int 3x^2 \, dx = 3 \cdot \frac{x^{2+1}}{2+1} + C = x^3 + C"),
            MathTex(r"2. \displaystyle \int 2x \, dx = 2 \cdot \frac{x^{1+1}}{1+1} + C = x^2 + C"),
            MathTex(r"3. \displaystyle \int 5 \, dx = 5x + C "),
            MathTex(r"\int \left( 3x^2 + 2x - 5 \right) \, dx = x^3 + x^2 - 5x + C"),
            MathTex(r"\int_{1}^{2} \left( 3x^2 + 2x - 5 \right) \, dx = \left[ x^3 + x^2 - 5x \right]_{1}^{2}"),
            MathTex(r"(2)^3 + (2)^2 - 5(2) = 8 + 4 - 10 = 2"),
            MathTex(r" (1)^3 + (1)^2 - 5(1) = 1 + 1 - 5 = -3 "),
            MathTex(r"\int_{1}^{2} \left( 3x^2 + 2x - 5 \right) \, dx = 2 - (-3) = 5"),
            MathTex(r" \boxed{5} "),
        ]

        # Add the first equation to the scene
        title = texts[0]
        self.add(title)
        self.add(equations[0])
        self.wait(2)
    # Loop through the equations and apply TransformMatchingTex
        for i in range(1, len(equations)):
            self.play(ReplacementTransform(texts[i - 1], texts[i], transform_mismatches=False))
            self.play(TransformMatchingTex(equations[i - 1], equations[i], transform_mismatches=True))
            self.wait(2)
        self.wait(5)
