# Source: https://docs.manim.community/en/stable/reference/manim.mobject.table.IntegerTable.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

IntegerTable[¶](#integertable "Link to this heading")
=====================================================

Qualified name: `manim.mobject.table.IntegerTable`

*class* IntegerTable(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/table.html#IntegerTable)[¶](#manim.mobject.table.IntegerTable "Link to this definition")
:   Bases: [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

    A specialized [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").

    Examples

    Example: IntegerTableExample [¶](#integertableexample)

    ![../_images/IntegerTableExample-1.png](../_images/IntegerTableExample-1.png)

    ```
    from manim import *

    class IntegerTableExample(Scene):
        def construct(self):
            t0 = IntegerTable(
                [[0,30,45,60,90],
                [90,60,45,30,0]],
                col_labels=[
                    MathTex(r"\frac{\sqrt{0}}{2}"),
                    MathTex(r"\frac{\sqrt{1}}{2}"),
                    MathTex(r"\frac{\sqrt{2}}{2}"),
                    MathTex(r"\frac{\sqrt{3}}{2}"),
                    MathTex(r"\frac{\sqrt{4}}{2}")],
                row_labels=[MathTex(r"\sin"), MathTex(r"\cos")],
                h_buff=1,
                element_to_mobject_config={"unit": r"^{\circ}"})
            self.add(t0)

    ```

    ```

    class IntegerTableExample(Scene):
        def construct(self):
            t0 = IntegerTable(
                [[0,30,45,60,90],
                [90,60,45,30,0]],
                col_labels=[
                    MathTex(r"\frac{\sqrt{0}}{2}"),
                    MathTex(r"\frac{\sqrt{1}}{2}"),
                    MathTex(r"\frac{\sqrt{2}}{2}"),
                    MathTex(r"\frac{\sqrt{3}}{2}"),
                    MathTex(r"\frac{\sqrt{4}}{2}")],
                row_labels=[MathTex(r"\sin"), MathTex(r"\cos")],
                h_buff=1,
                element_to_mobject_config={"unit": r"^{\circ}"})
            self.add(t0)


    ```

    Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
    Will round if there are decimal entries in the table.

    Parameters:
    :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table has to be valid input
          for [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
        * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.Integer'>*, *\*\*kwargs*)[¶](#manim.mobject.table.IntegerTable._original__init__ "Link to this definition")
    :   Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with element\_to\_mobject set to [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
        Will round if there are decimal entries in the table.

        Parameters:
        :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2d array or list of lists. Content of the table has to be valid input
              for [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
            * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`Integer`](manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer "manim.mobject.text.numbers.Integer").
            * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").