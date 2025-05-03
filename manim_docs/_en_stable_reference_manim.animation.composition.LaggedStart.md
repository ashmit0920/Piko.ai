# Source: https://docs.manim.community/en/stable/reference/manim.animation.composition.LaggedStart.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LaggedStart[¶](#laggedstart "Link to this heading")
===================================================

Qualified name: `manim.animation.composition.LaggedStart`

*class* LaggedStart(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/composition.html#LaggedStart)[¶](#manim.animation.composition.LaggedStart "Link to this definition")
:   Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

    Adjusts the timing of a series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") according to `lag_ratio`.

    Parameters:
    :   * **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")) – Sequence of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.
        * **lag\_ratio** (*float*) –

          Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
          `n.nn` means the next animation will play when `nnn%` of the current animation has played.
          Defaults to 0.05, meaning that the next animation will begin when 5% of the current
          animation has played.

          This does not influence the total runtime of the animation. Instead the runtime
          of individual animations is adjusted so that the complete animation has the defined
          run time.

    Examples

    Example: LaggedStartExample [¶](#laggedstartexample)

    [
    ](./LaggedStartExample-1.mp4)

    ```
    from manim import *

    class LaggedStartExample(Scene):
        def construct(self):
            title = Text("lag_ratio = 0.25").to_edge(UP)

            dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
            dot2 = Dot(point=LEFT * 2, radius=0.16)
            dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
            line_25 = DashedLine(
                start=LEFT + UP * 2,
                end=LEFT + DOWN * 2,
                color=RED
            )
            label = Text("25%", font_size=24).next_to(line_25, UP)
            self.add(title, dot1, dot2, dot3, line_25, label)

            self.play(LaggedStart(
                dot1.animate.shift(RIGHT * 4),
                dot2.animate.shift(RIGHT * 4),
                dot3.animate.shift(RIGHT * 4),
                lag_ratio=0.25,
                run_time=4
            ))

    ```

    ```

    class LaggedStartExample(Scene):
        def construct(self):
            title = Text("lag_ratio = 0.25").to_edge(UP)

            dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
            dot2 = Dot(point=LEFT * 2, radius=0.16)
            dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
            line_25 = DashedLine(
                start=LEFT + UP * 2,
                end=LEFT + DOWN * 2,
                color=RED
            )
            label = Text("25%", font_size=24).next_to(line_25, UP)
            self.add(title, dot1, dot2, dot3, line_25, label)

            self.play(LaggedStart(
                dot1.animate.shift(RIGHT * 4),
                dot2.animate.shift(RIGHT * 4),
                dot3.animate.shift(RIGHT * 4),
                lag_ratio=0.25,
                run_time=4
            ))


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*animations*, *lag\_ratio=0.05*, *\*\*kwargs*)[¶](#manim.animation.composition.LaggedStart._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
            * **lag\_ratio** (*float*)