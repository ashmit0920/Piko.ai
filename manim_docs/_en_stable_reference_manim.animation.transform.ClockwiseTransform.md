# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ClockwiseTransform.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ClockwiseTransform[¶](#clockwisetransform "Link to this heading")
=================================================================

Qualified name: `manim.animation.transform.ClockwiseTransform`

*class* ClockwiseTransform(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ClockwiseTransform)[¶](#manim.animation.transform.ClockwiseTransform "Link to this definition")
:   Bases: [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform")

    Transforms the points of a mobject along a clockwise oriented arc.

    See also

    [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform"), [`CounterclockwiseTransform`](manim.animation.transform.CounterclockwiseTransform.html#manim.animation.transform.CounterclockwiseTransform "manim.animation.transform.CounterclockwiseTransform")

    Examples

    Example: ClockwiseExample [¶](#clockwiseexample)

    [
    ](./ClockwiseExample-1.mp4)

    ```
    from manim import *

    class ClockwiseExample(Scene):
        def construct(self):
            dl, dr = Dot(), Dot()
            sl, sr = Square(), Square()

            VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
            VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)

            self.add(dl, dr)
            self.wait()
            self.play(
                ClockwiseTransform(dl, sl),
                Transform(dr, sr)
            )
            self.wait()

    ```

    ```

    class ClockwiseExample(Scene):
        def construct(self):
            dl, dr = Dot(), Dot()
            sl, sr = Square(), Square()

            VGroup(dl, sl).arrange(DOWN).shift(2*LEFT)
            VGroup(dr, sr).arrange(DOWN).shift(2*RIGHT)

            self.add(dl, dr)
            self.wait()
            self.play(
                ClockwiseTransform(dl, sl),
                Transform(dr, sr)
            )
            self.wait()


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **path\_arc** (*float*)

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *path\_arc=-3.141592653589793*, *\*\*kwargs*)[¶](#manim.animation.transform.ClockwiseTransform._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **path\_arc** (*float*)

        Return type:
        :   None