# Source: https://docs.manim.community/en/stable/reference/manim.mobject.table.MathTable.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MathTable[¶](#mathtable "Link to this heading")
===============================================

Qualified name: `manim.mobject.table.MathTable`

*class* MathTable(*table*, *element\_to\_mobject=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/table.html#MathTable)[¶](#manim.mobject.table.MathTable "Link to this definition")
:   Bases: [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

    A specialized [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with LaTeX.

    Examples

    Example: MathTableExample [¶](#mathtableexample)

    ![../_images/MathTableExample-1.png](../_images/MathTableExample-1.png)

    ```
    from manim import *

    class MathTableExample(Scene):
        def construct(self):
            t0 = MathTable(
                [["+", 0, 5, 10],
                [0, 0, 5, 10],
                [2, 2, 7, 12],
                [4, 4, 9, 14]],
                include_outer_lines=True)
            self.add(t0)

    ```

    ```

    class MathTableExample(Scene):
        def construct(self):
            t0 = MathTable(
                [["+", 0, 5, 10],
                [0, 0, 5, 10],
                [2, 2, 7, 12],
                [4, 4, 9, 14]],
                include_outer_lines=True)
            self.add(t0)


    ```

    Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
    Every entry in table is set in a Latex align environment.

    Parameters:
    :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table have to be valid input
          for [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
        * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
        * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").

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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *\*\*kwargs*)[¶](#manim.mobject.table.MathTable._original__init__ "Link to this definition")
    :   Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
        Every entry in table is set in a Latex align environment.

        Parameters:
        :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table have to be valid input
              for [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
            * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
            * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").