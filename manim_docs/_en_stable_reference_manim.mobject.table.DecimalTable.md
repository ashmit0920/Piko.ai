# Source: https://docs.manim.community/en/stable/reference/manim.mobject.table.DecimalTable.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DecimalTable[¶](#decimaltable "Link to this heading")
=====================================================

Qualified name: `manim.mobject.table.DecimalTable`

*class* DecimalTable(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/table.html#DecimalTable)[¶](#manim.mobject.table.DecimalTable "Link to this definition")
:   Bases: [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table")

    A specialized [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") mobject for use with [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber") to display decimal entries.

    Examples

    Example: DecimalTableExample [¶](#decimaltableexample)

    ![../_images/DecimalTableExample-1.png](../_images/DecimalTableExample-1.png)

    ```
    from manim import *

    class DecimalTableExample(Scene):
        def construct(self):
            x_vals = [-2,-1,0,1,2]
            y_vals = np.exp(x_vals)
            t0 = DecimalTable(
                [x_vals, y_vals],
                row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
                h_buff=1,
                element_to_mobject_config={"num_decimal_places": 2})
            self.add(t0)

    ```

    ```

    class DecimalTableExample(Scene):
        def construct(self):
            x_vals = [-2,-1,0,1,2]
            y_vals = np.exp(x_vals)
            t0 = DecimalTable(
                [x_vals, y_vals],
                row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
                h_buff=1,
                element_to_mobject_config={"num_decimal_places": 2})
            self.add(t0)


    ```

    Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with `element_to_mobject` set to [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
    By default, `num_decimal_places` is set to 1.
    Will round/truncate the decimal places based on the provided `element_to_mobject_config`.

    Parameters:
    :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2D array, or a list of lists. Content of the table must be valid input
          for [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
        * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
        * **element\_to\_mobject\_config** (*dict*) – Element to mobject config, here set as {“num\_decimal\_places”: 1}.
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

    \_original\_\_init\_\_(*table*, *element\_to\_mobject=<class 'manim.mobject.text.numbers.DecimalNumber'>*, *element\_to\_mobject\_config={'num\_decimal\_places': 1}*, *\*\*kwargs*)[¶](#manim.mobject.table.DecimalTable._original__init__ "Link to this definition")
    :   Special case of [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table") with `element_to_mobject` set to [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
        By default, `num_decimal_places` is set to 1.
        Will round/truncate the decimal places based on the provided `element_to_mobject_config`.

        Parameters:
        :   * **table** (*Iterable**[**Iterable**[**float* *|* *str**]**]*) – A 2D array, or a list of lists. Content of the table must be valid input
              for [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
            * **element\_to\_mobject** (*Callable**[**[**float* *|* *str**]**,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") class applied to the table entries. Set as [`DecimalNumber`](manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber "manim.mobject.text.numbers.DecimalNumber").
            * **element\_to\_mobject\_config** (*dict*) – Element to mobject config, here set as {“num\_decimal\_places”: 1}.
            * **kwargs** – Additional arguments to be passed to [`Table`](manim.mobject.table.Table.html#manim.mobject.table.Table "manim.mobject.table.Table").