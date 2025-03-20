from manim import *
from reactive_manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class DefaultTemplate(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="es", tld="com"))

        tex = MathTex("ax^2","+","bx","+","c","=","0")
        self.add(tex)
        with self.voiceover(text="Despejando la incógnita en la ecuación cuadrática") as tracker:
            self.wait(1)
        tex2 = MathTex("ax^2","+","bx","=","-c")
        with self.voiceover(text="Restando el término independiente de ambos lados") as tracker:
            self.play(TransformMatchingTex(tex, tex2,transform_mismatches=True, run_time=tracker.duration) )
#            self.play(TransformInStages.from_copy(tex,tex2))
        self.wait(1)
        tex3 = MathTex("x^2","+",r"\dfrac{b}{a}","x","=",r"-\dfrac{c}{a}")
        with self.voiceover(text="Dividiendo por el coeficiente del término cuadrático") as tracker:
            self.play(TransformMatchingTex(tex2, tex3,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex4 = MathTex("x^2","+",r"\dfrac{b}{a}x","+",r"\left(\dfrac{b}{2a}\right)^2","=",r"-\dfrac{c}{a}","+",r"\left(\dfrac{b}{2a}\right)^2",font_size= 14)
        with self.voiceover(text="Completando el cuadrado perfecto") as tracker:
            self.play(TransformMatchingTex(tex3, tex4,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex5 = MathTex(r"\left(x+\dfrac{b}{2a}\right)^2","=",r"-\dfrac{c}{a}+\dfrac{b^2}{4a^2}",font_size= 14)
        with self.voiceover(text="Factorizando") as tracker:
            self.play(TransformMatchingTex(tex4, tex5,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex6 = MathTex(r"\left(x+\dfrac{b}{2a}\right)^2","=",r"-\dfrac{4ac}{4a^2}","+",r"\dfrac{b^2}{4a^2}",font_size= 14)
        with self.voiceover(text="Encontrando el máximo común divisor del lado derecho de la ecuación") as tracker:
            self.play(TransformMatchingTex(tex5, tex6,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex7 = MathTex(r"\left(x+\dfrac{b}{2a}\right)^2","=",r"\dfrac{b^2-4ac}{4a^2}",font_size= 14)
        with self.voiceover(text="Hacemos la resta del lado derecho de la ecuación") as tracker:
            self.play(TransformMatchingTex(tex6, tex7,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex8 = MathTex(r"\sqrt{\left(x+\dfrac{b}{2a}\right)^2}=\sqrt{\dfrac{b^2-4ac}{4a^2}}",font_size= 14)
        with self.voiceover(text="Obtenemos la raíz cuadrada") as tracker:
            self.play(TransformMatchingTex(tex7, tex8,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex9 = MathTex(r"x+\dfrac{b}{2a}","=",r"\pm",r"\dfrac{\sqrt{b^2-4ac}}{2a}",font_size= 14)
        with self.voiceover(text="Del lado derecho tenemos la raíz positiva y la negativa") as tracker:
            self.play(TransformMatchingTex(tex8, tex9,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex10 = MathTex(r"x=-\dfrac{b}{2a}\pm\dfrac{\sqrt{b^2-4ac}}{2a}",font_size= 14)
        with self.voiceover(text="Despejamos equis") as tracker:
            self.play(TransformMatchingTex(tex9, tex10,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        tex11 = MathTex(r"x",r"=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}",font_size= 16)
        with self.voiceover(text="simplificamos la fracción del lado derecho") as tracker:
            self.play(TransformMatchingTex(tex10, tex11,transform_mismatches=True, run_time=tracker.duration) )
        self.wait(1)
        with self.voiceover(text="Tenemos la fórmula general de la ecuación cuadrática") as tracker:
            self.wait(3)
