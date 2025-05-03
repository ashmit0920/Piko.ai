# Source: https://docs.manim.community/en/stable/reference/manim.mobject.matrix.DecimalMatrix.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DecimalMatrix[¶](#decimalmatrix "Link to this heading")
=======================================================

Qualified name: `manim.mobject.matrix.DecimalMatrix`

*class* DecimalMatrix(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/matrix.html#DecimalMatrix)[¶](#manim.mobject.matrix.DecimalMatrix "Link to this definition")
:   Bases: [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

    A mobject that displays a matrix with decimal entries on the screen.

    Examples

    Example: DecimalMatrixExample [¶](#decimalmatrixexample)

    ![../_images/DecimalMatrixExample-1.png](../_images/DecimalMatrixExample-1.png)

    ```
    from manim import *

    class DecimalMatrixExample(Scene):
        def construct(self):
            m0 = DecimalMatrix(
                [[3.456, 2.122], [33.2244, 12]],
                element_to_mobject_config={"num_decimal_places": 2},
                left_bracket="\\{",
                right_bracket="\\}")
            self.add(m0)

    ```

    ```

    class DecimalMatrixExample(Scene):
        def construct(self):
            m0 = DecimalMatrix(
                [[3.456, 2.122], [33.2244, 12]],
                element_to_mobject_config={"num_decimal_places": 2},
                left_bracket="\\{",
                right_bracket="\\}")
            self.add(m0)


    ```

    Will round/truncate the decimal places as per the provided config.

    Parameters:
    :   * **matrix** (*Iterable*) – A numpy 2d array or list of lists
        * **element\_to\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber
        * **element\_to\_mobject\_config** (*dict**[**str**,* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}

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

    \_original\_\_init\_\_(*matrix*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[¶](#manim.mobject.matrix.DecimalMatrix._original__init__ "Link to this definition")
    :   Will round/truncate the decimal places as per the provided config.

        Parameters:
        :   * **matrix** (*Iterable*) – A numpy 2d array or list of lists
            * **element\_to\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber
            * **element\_to\_mobject\_config** (*dict**[**str**,* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – Config for the desired mobject, by default {“num\_decimal\_places”: 1}