# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Square.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Square[¶](#square "Link to this heading")
=========================================

Qualified name: `manim.mobject.geometry.polygram.Square`

*class* Square(*side\_length=2.0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Square)[¶](#manim.mobject.geometry.polygram.Square "Link to this definition")
:   Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    A rectangle with equal side lengths.

    Parameters:
    :   * **side\_length** (*float*) – The length of the sides of the square.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle").

    Examples

    Example: SquareExample [¶](#squareexample)

    ![../_images/SquareExample-1.png](../_images/SquareExample-1.png)

    ```
    from manim import *

    class SquareExample(Scene):
        def construct(self):
            square_1 = Square(side_length=2.0).shift(DOWN)
            square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
            square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
            self.add(square_1, square_2, square_3)

    ```

    ```

    class SquareExample(Scene):
        def construct(self):
            square_1 = Square(side_length=2.0).shift(DOWN)
            square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
            square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
            self.add(square_1, square_2, square_3)


    ```

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `side_length` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*side\_length=2.0*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.Square._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **side\_length** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None