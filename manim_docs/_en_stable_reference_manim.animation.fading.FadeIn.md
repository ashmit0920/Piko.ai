# Source: https://docs.manim.community/en/stable/reference/manim.animation.fading.FadeIn.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

FadeIn[¶](#fadein "Link to this heading")
=========================================

Qualified name: `manim.animation.fading.FadeIn`

*class* FadeIn(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/fading.html#FadeIn)[¶](#manim.animation.fading.FadeIn "Link to this definition")
:   Bases: `_Fade`

    Fade in [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") s.

    Parameters:
    :   * **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to be faded in.
        * **shift** – The vector by which the mobject shifts while being faded in.
        * **target\_position** – The position from which the mobject starts while being faded in. In case
          another mobject is given as target position, its center is used.
        * **scale** – The factor by which the mobject is scaled initially before being rescaling to
          its original size while being faded in.

    Examples

    Example: FadeInExample [¶](#fadeinexample)

    [
    ](./FadeInExample-1.mp4)

    ```
    from manim import *

    class FadeInExample(Scene):
        def construct(self):
            dot = Dot(UP * 2 + LEFT)
            self.add(dot)
            tex = Tex(
                "FadeIn with ", "shift ", r" or target\_position", " and scale"
            ).scale(1)
            animations = [
                FadeIn(tex[0]),
                FadeIn(tex[1], shift=DOWN),
                FadeIn(tex[2], target_position=dot),
                FadeIn(tex[3], scale=1.5),
            ]
            self.play(AnimationGroup(*animations, lag_ratio=0.5))

    ```

    ```

    class FadeInExample(Scene):
        def construct(self):
            dot = Dot(UP * 2 + LEFT)
            self.add(dot)
            tex = Tex(
                "FadeIn with ", "shift ", r" or target\_position", " and scale"
            ).scale(1)
            animations = [
                FadeIn(tex[0]),
                FadeIn(tex[1], shift=DOWN),
                FadeIn(tex[2], target_position=dot),
                FadeIn(tex[3], scale=1.5),
            ]
            self.play(AnimationGroup(*animations, lag_ratio=0.5))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `create_starting_mobject` |  |
    | `create_target` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*mobjects*, *\*\*kwargs*)[¶](#manim.animation.fading.FadeIn._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **mobjects** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

        Return type:
        :   None