# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyPointwiseFunction.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ApplyPointwiseFunction[¶](#applypointwisefunction "Link to this heading")
=========================================================================

Qualified name: `manim.animation.transform.ApplyPointwiseFunction`

*class* ApplyPointwiseFunction(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ApplyPointwiseFunction)[¶](#manim.animation.transform.ApplyPointwiseFunction "Link to this definition")
:   Bases: [`ApplyMethod`](manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod "manim.animation.transform.ApplyMethod")

    Animation that applies a pointwise function to a mobject.

    Examples

    Example: WarpSquare [¶](#warpsquare)

    [
    ](./WarpSquare-1.mp4)

    ```
    from manim import *

    class WarpSquare(Scene):
        def construct(self):
            square = Square()
            self.play(
                ApplyPointwiseFunction(
                    lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
                )
            )
            self.wait()

    ```

    ```

    class WarpSquare(Scene):
        def construct(self):
            square = Square()
            self.play(
                ApplyPointwiseFunction(
                    lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
                )
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
    :   * **function** (*types.MethodType*)
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **run\_time** (*float*)

    \_original\_\_init\_\_(*function*, *mobject*, *run\_time=3.0*, *\*\*kwargs*)[¶](#manim.animation.transform.ApplyPointwiseFunction._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **function** (*MethodType*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **run\_time** (*float*)

        Return type:
        :   None