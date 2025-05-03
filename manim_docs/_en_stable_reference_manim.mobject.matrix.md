# Source: https://docs.manim.community/en/stable/reference/manim.mobject.matrix.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

matrix[¶](#module-manim.mobject.matrix "Link to this heading")
==============================================================

Mobjects representing matrices.

Examples

Example: MatrixExamples [¶](#matrixexamples)

![../_images/MatrixExamples-1.png](../_images/MatrixExamples-1.png)

```
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket=r"\{",
            right_bracket=r"\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)

```

```

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([["\\pi", 0], [-1, 1]])
        m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
            left_bracket="(",
            right_bracket=")")
        m2 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12.33]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket=r"\{",
            right_bracket=r"\}")
        m3 = MobjectMatrix(
            [[Circle().scale(0.3), Square().scale(0.3)],
            [MathTex("\\pi").scale(2), Star().scale(0.3)]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
        self.add(g)


```

Classes

|  |  |
| --- | --- |
| [`DecimalMatrix`](manim.mobject.matrix.DecimalMatrix.html#manim.mobject.matrix.DecimalMatrix "manim.mobject.matrix.DecimalMatrix") | A mobject that displays a matrix with decimal entries on the screen. |
| [`IntegerMatrix`](manim.mobject.matrix.IntegerMatrix.html#manim.mobject.matrix.IntegerMatrix "manim.mobject.matrix.IntegerMatrix") | A mobject that displays a matrix with integer entries on the screen. |
| [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix") | A mobject that displays a matrix on the screen. |
| [`MobjectMatrix`](manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix "manim.mobject.matrix.MobjectMatrix") | A mobject that displays a matrix of mobject entries on the screen. |

Functions

get\_det\_text(*matrix*, *determinant=None*, *background\_rect=False*, *initial\_scale\_factor=2*)[[source]](../_modules/manim/mobject/matrix.html#get_det_text)[¶](#manim.mobject.matrix.get_det_text "Link to this definition")
:   Helper function to create determinant.

    Parameters:
    :   * **matrix** ([*Matrix*](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")) – The matrix whose determinant is to be created
        * **determinant** (*int* *|* *str* *|* *None*) – The value of the determinant of the matrix
        * **background\_rect** (*bool*) – The background rectangle
        * **initial\_scale\_factor** (*float*) – The scale of the text det w.r.t the matrix

    Returns:
    :   A VGroup containing the determinant

    Return type:
    :   [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Examples

    Example: DeterminantOfAMatrix [¶](#determinantofamatrix)

    ![../_images/DeterminantOfAMatrix-1.png](../_images/DeterminantOfAMatrix-1.png)

    ```
    from manim import *

    class DeterminantOfAMatrix(Scene):
        def construct(self):
            matrix = Matrix([
                [2, 0],
                [-1, 1]
            ])

            # scaling down the `det` string
            det = get_det_text(matrix,
                        determinant=3,
                        initial_scale_factor=1)

            # must add the matrix
            self.add(matrix)
            self.add(det)

    ```

    ```

    class DeterminantOfAMatrix(Scene):
        def construct(self):
            matrix = Matrix([
                [2, 0],
                [-1, 1]
            ])

            # scaling down the `det` string
            det = get_det_text(matrix,
                        determinant=3,
                        initial_scale_factor=1)

            # must add the matrix
            self.add(matrix)
            self.add(det)


    ```

matrix\_to\_mobject(*matrix*)[[source]](../_modules/manim/mobject/matrix.html#matrix_to_mobject)[¶](#manim.mobject.matrix.matrix_to_mobject "Link to this definition")

matrix\_to\_tex\_string(*matrix*)[[source]](../_modules/manim/mobject/matrix.html#matrix_to_tex_string)[¶](#manim.mobject.matrix.matrix_to_tex_string "Link to this definition")