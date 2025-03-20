from manim import *

class DespejeFormulaCuadratica(Scene):
    def construct(self):
        # Título de la escena
        titulo = Tex("Despeje de la Fórmula Cuadrática").scale(0.8)
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Ecuación general de segundo grado
        ecuacion_general = MathTex("ax^2 + bx + c = 0").scale(0.8)
        self.play(Write(ecuacion_general))
        self.wait(1)

        # Paso 1: Aislar el término cuadrático
        paso1 = MathTex("ax^2 + bx = -c").scale(0.8)
        self.play(Transform(ecuacion_general, paso1))
        self.wait(1)

        # Paso 2: Dividir toda la ecuación por 'a'
        paso2 = MathTex("x^2 + \\frac{b}{a}x = -\\frac{c}{a}").scale(0.8)
        self.play(Transform(ecuacion_general, paso2))
        self.wait(1)

        # Paso 3: Completar el cuadrado
        paso3 = MathTex(
            "x^2 + \\frac{b}{a}x + \\left(\\frac{b}{2a}\\right)^2 = -\\frac{c}{a} + \\left(\\frac{b}{2a}\\right)^2"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso3))
        self.wait(1)

        # Paso 4: Simplificar el lado izquierdo
        paso4 = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2 = -\\frac{c}{a} + \\frac{b^2}{4a^2}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso4))
        self.wait(1)

        # Paso 5: Combinar términos del lado derecho
        paso5 = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2 = \\frac{b^2 - 4ac}{4a^2}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso5))
        self.wait(1)

        # Paso 6: Tomar la raíz cuadrada de ambos lados
        paso6 = MathTex(
            "x + \\frac{b}{2a} = \\pm \\sqrt{\\frac{b^2 - 4ac}{4a^2}}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso6))
        self.wait(1)

        # Paso 7: Simplificar la raíz cuadrada
        paso7 = MathTex(
            "x + \\frac{b}{2a} = \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso7))
        self.wait(1)

        # Paso 8: Despejar x
        paso8 = MathTex(
            "x = -\\frac{b}{2a} \\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, paso8))
        self.wait(1)

        # Paso 9: Combinar términos para obtener la fórmula cuadrática
        formula_cuadratica = MathTex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.8)
        self.play(Transform(ecuacion_general, formula_cuadratica))
        self.wait(2)

        # Destacar la fórmula cuadrática
        self.play(Indicate(formula_cuadratica))
        self.wait(2)

        # Limpiar la pantalla
        self.play(FadeOut(formula_cuadratica))
        self.wait(1)