# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform.ApplyMatrix.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ApplyMatrix[¶](#applymatrix "Link to this heading")
===================================================

Qualified name: `manim.animation.transform.ApplyMatrix`

*class* ApplyMatrix(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform.html#ApplyMatrix)[¶](#manim.animation.transform.ApplyMatrix "Link to this definition")
:   Bases: [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction")

    Applies a matrix transform to an mobject.

    Parameters:
    :   * **matrix** (*np.ndarray*) – The transformation matrix.
        * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **about\_point** (*np.ndarray*) – The origin point for the transform. Defaults to `ORIGIN`.
        * **kwargs** – Further keyword arguments that are passed to [`ApplyPointwiseFunction`](manim.animation.transform.ApplyPointwiseFunction.html#manim.animation.transform.ApplyPointwiseFunction "manim.animation.transform.ApplyPointwiseFunction").

    Examples

    Example: ApplyMatrixExample [¶](#applymatrixexample)

    [
    ](./ApplyMatrixExample-1.mp4)

    ```
    from manim import *

    class ApplyMatrixExample(Scene):
        def construct(self):
            matrix = [[1, 1], [0, 2/3]]
            self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))

    ```

    ```

    class ApplyMatrixExample(Scene):
        def construct(self):
            matrix = [[1, 1], [0, 2/3]]
            self.play(ApplyMatrix(matrix, Text("Hello World!")), ApplyMatrix(matrix, NumberPlane()))


    ```

    Methods

    |  |  |
    | --- | --- |
    | `initialize_matrix` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `path_arc` |  |
    | `path_func` |  |
    | `run_time` |  |

    \_original\_\_init\_\_(*matrix*, *mobject*, *about\_point=array([0., 0., 0.])*, *\*\*kwargs*)[¶](#manim.animation.transform.ApplyMatrix._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **matrix** (*ndarray*)
            * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **about\_point** (*ndarray*)

        Return type:
        :   None