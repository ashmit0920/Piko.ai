# Source: https://docs.manim.community/en/stable/reference/manim.animation.fading.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

fading[¶](#module-manim.animation.fading "Link to this heading")
================================================================

Fading in and out of view.

Example: Fading [¶](#fading)

[
](./Fading-1.mp4)

```
from manim import *

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

```

```

class Fading(Scene):
    def construct(self):
        tex_in = Tex("Fade", "In").scale(3)
        tex_out = Tex("Fade", "Out").scale(3)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))


```

Classes

|  |  |
| --- | --- |
| [`FadeIn`](manim.animation.fading.FadeIn.html#manim.animation.fading.FadeIn "manim.animation.fading.FadeIn") | Fade in [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |
| [`FadeOut`](manim.animation.fading.FadeOut.html#manim.animation.fading.FadeOut "manim.animation.fading.FadeOut") | Fade out [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s. |