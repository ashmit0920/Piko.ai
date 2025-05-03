# Source: https://docs.manim.community/en/stable/reference/manim.animation.indication.Wiggle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Wiggle[¶](#wiggle "Link to this heading")
=========================================

Qualified name: `manim.animation.indication.Wiggle`

*class* Wiggle(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/indication.html#Wiggle)[¶](#manim.animation.indication.Wiggle "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Wiggle a Mobject.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to wiggle.
        * **scale\_value** (*float*) – The factor by which the mobject will be temporarily scaled.
        * **rotation\_angle** (*float*) – The wiggle angle.
        * **n\_wiggles** (*int*) – The number of wiggles.
        * **scale\_about\_point** (*np.ndarray* *|* *None*) – The point about which the mobject gets scaled.
        * **rotate\_about\_point** (*np.ndarray* *|* *None*) – The point around which the mobject gets rotated.
        * **run\_time** (*float*) – The duration of the animation

    Examples

    Example: ApplyingWaves [¶](#applyingwaves)

    [
    ](./ApplyingWaves-2.mp4)

    ```
    from manim import *

    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("Wiggle").scale(3)
            self.play(Wiggle(tex))
            self.wait()

    ```

    ```

    class ApplyingWaves(Scene):
        def construct(self):
            tex = Tex("Wiggle").scale(3)
            self.play(Wiggle(tex))
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_rotate_about_point` |  |
    | `get_scale_about_point` |  |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *scale\_value=1.1*, *rotation\_angle=0.06283185307179587*, *n\_wiggles=6*, *scale\_about\_point=None*, *rotate\_about\_point=None*, *run\_time=2*, *\*\*kwargs*)[¶](#manim.animation.indication.Wiggle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **scale\_value** (*float*)
            * **rotation\_angle** (*float*)
            * **n\_wiggles** (*int*)
            * **scale\_about\_point** (*ndarray* *|* *None*)
            * **rotate\_about\_point** (*ndarray* *|* *None*)
            * **run\_time** (*float*)

        Return type:
        :   None