# Source: https://docs.manim.community/en/stable/reference/manim.mobject.matrix.IntegerMatrix.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

IntegerMatrix[¶](#integermatrix "Link to this heading")
=======================================================

Qualified name: `manim.mobject.matrix.IntegerMatrix`

*class* IntegerMatrix(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/matrix.html#IntegerMatrix)[¶](#manim.mobject.matrix.IntegerMatrix "Link to this definition")
:   Bases: [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

    A mobject that displays a matrix with integer entries on the screen.

    Examples

    Example: IntegerMatrixExample [¶](#integermatrixexample)

    ![../_images/IntegerMatrixExample-1.png](../_images/IntegerMatrixExample-1.png)

    ```
    from manim import *

    class IntegerMatrixExample(Scene):
        def construct(self):
            m0 = IntegerMatrix(
                [[3.7, 2], [42.2, 12]],
                left_bracket="(",
                right_bracket=")")
            self.add(m0)

    ```

    ```

    class IntegerMatrixExample(Scene):
        def construct(self):
            m0 = IntegerMatrix(
                [[3.7, 2], [42.2, 12]],
                left_bracket="(",
                right_bracket=")")
            self.add(m0)


    ```

    Will round if there are decimal entries in the matrix.

    Parameters:
    :   * **matrix** (*Iterable*) – A numpy 2d array or list of lists
        * **element\_to\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default Integer

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
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)[¶](#manim.mobject.matrix.IntegerMatrix._original__init__ "Link to this definition")
    :   Will round if there are decimal entries in the matrix.

        Parameters:
        :   * **matrix** (*Iterable*) – A numpy 2d array or list of lists
            * **element\_to\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default Integer