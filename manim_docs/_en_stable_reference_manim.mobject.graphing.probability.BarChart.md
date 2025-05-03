# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.BarChart.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

BarChart[¶](#barchart "Link to this heading")
=============================================

Qualified name: `manim.mobject.graphing.probability.BarChart`

*class* BarChart(*values*, *bar\_names=None*, *y\_range=None*, *x\_length=None*, *y\_length=None*, *bar\_colors=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']*, *bar\_width=0.6*, *bar\_fill\_opacity=0.7*, *bar\_stroke\_width=3*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart)[¶](#manim.mobject.graphing.probability.BarChart "Link to this definition")
:   Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

    Creates a bar chart. Inherits from [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes"), so it shares its methods
    and attributes. Each axis inherits from [`NumberLine`](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine"), so pass in `x_axis_config`/`y_axis_config`
    to control their attributes.

    Parameters:
    :   * **values** (*MutableSequence**[**float**]*) – A sequence of values that determines the height of each bar. Accepts negative values.
        * **bar\_names** (*Sequence**[**str**]* *|* *None*) – A sequence of names for each bar. Does not have to match the length of `values`.
        * **y\_range** (*Sequence**[**float**]* *|* *None*) – The y\_axis range of values. If `None`, the range will be calculated based on the
          min/max of `values` and the step will be calculated based on `y_length`.
        * **x\_length** (*float* *|* *None*) – The length of the x-axis. If `None`, it is automatically calculated based on
          the number of values and the width of the screen.
        * **y\_length** (*float* *|* *None*) – The length of the y-axis.
        * **bar\_colors** (*Iterable**[**str**]*) – The color for the bars. Accepts a sequence of colors (can contain just one item).
          If the length of``bar\_colors`` does not match that of `values`,
          intermediate colors will be automatically determined.
        * **bar\_width** (*float*) – The length of a bar. Must be between 0 and 1.
        * **bar\_fill\_opacity** (*float*) – The fill opacity of the bars.
        * **bar\_stroke\_width** (*float*) – The stroke width of the bars.

    Examples

    Example: BarChartExample [¶](#barchartexample)

    ![../_images/BarChartExample-1.png](../_images/BarChartExample-1.png)

    ```
    from manim import *

    class BarChartExample(Scene):
        def construct(self):
            chart = BarChart(
                values=[-5, 40, -10, 20, -3],
                bar_names=["one", "two", "three", "four", "five"],
                y_range=[-20, 50, 10],
                y_length=6,
                x_length=10,
                x_axis_config={"font_size": 36},
            )

            c_bar_lbls = chart.get_bar_labels(font_size=48)

            self.add(chart, c_bar_lbls)

    ```

    ```

    class BarChartExample(Scene):
        def construct(self):
            chart = BarChart(
                values=[-5, 40, -10, 20, -3],
                bar_names=["one", "two", "three", "four", "five"],
                y_range=[-20, 50, 10],
                y_length=6,
                x_length=10,
                x_axis_config={"font_size": 36},
            )

            c_bar_lbls = chart.get_bar_labels(font_size=48)

            self.add(chart, c_bar_lbls)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`change_bar_values`](#manim.mobject.graphing.probability.BarChart.change_bar_values "manim.mobject.graphing.probability.BarChart.change_bar_values") | Updates the height of the bars of the chart. |
    | [`get_bar_labels`](#manim.mobject.graphing.probability.BarChart.get_bar_labels "manim.mobject.graphing.probability.BarChart.get_bar_labels") | Annotates each bar with its corresponding value. |

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

    \_add\_x\_axis\_labels()[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._add_x_axis_labels)[¶](#manim.mobject.graphing.probability.BarChart._add_x_axis_labels "Link to this definition")
    :   Essentially :meth`:~.NumberLine.add\_labels`, but differs in that
        the direction of the label with respect to the x\_axis changes to UP or DOWN
        depending on the value.

        UP for negative values and DOWN for positive values.

    \_create\_bar(*bar\_number*, *value*)[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._create_bar)[¶](#manim.mobject.graphing.probability.BarChart._create_bar "Link to this definition")
    :   Creates a positioned bar on the chart.

        Parameters:
        :   * **bar\_number** (*int*) – Determines the x-position of the bar.
            * **value** (*float*) – The value that determines the height of the bar.

        Returns:
        :   A positioned rectangle representing a bar on the chart.

        Return type:
        :   [Rectangle](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    \_original\_\_init\_\_(*values*, *bar\_names=None*, *y\_range=None*, *x\_length=None*, *y\_length=None*, *bar\_colors=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']*, *bar\_width=0.6*, *bar\_fill\_opacity=0.7*, *bar\_stroke\_width=3*, *\*\*kwargs*)[¶](#manim.mobject.graphing.probability.BarChart._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **values** (*MutableSequence**[**float**]*)
            * **bar\_names** (*Sequence**[**str**]* *|* *None*)
            * **y\_range** (*Sequence**[**float**]* *|* *None*)
            * **x\_length** (*float* *|* *None*)
            * **y\_length** (*float* *|* *None*)
            * **bar\_colors** (*Iterable**[**str**]*)
            * **bar\_width** (*float*)
            * **bar\_fill\_opacity** (*float*)
            * **bar\_stroke\_width** (*float*)

    \_update\_colors()[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart._update_colors)[¶](#manim.mobject.graphing.probability.BarChart._update_colors "Link to this definition")
    :   Initialize the colors of the bars of the chart.

        Sets the color of `self.bars` via `self.bar_colors`.

        Primarily used when the bars are initialized with `self._add_bars`
        or updated via `self.change_bar_values`.

    change\_bar\_values(*values*, *update\_colors=True*)[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart.change_bar_values)[¶](#manim.mobject.graphing.probability.BarChart.change_bar_values "Link to this definition")
    :   Updates the height of the bars of the chart.

        Parameters:
        :   * **values** (*Iterable**[**float**]*) – The values that will be used to update the height of the bars.
              Does not have to match the number of bars.
            * **update\_colors** (*bool*) – Whether to re-initalize the colors of the bars based on `self.bar_colors`.

        Examples

        Example: ChangeBarValuesExample [¶](#changebarvaluesexample)

        ![../_images/ChangeBarValuesExample-1.png](../_images/ChangeBarValuesExample-1.png)

        ```
        from manim import *

        class ChangeBarValuesExample(Scene):
            def construct(self):
                values=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

                chart = BarChart(
                    values,
                    y_range=[-10, 10, 2],
                    y_axis_config={"font_size": 24},
                )
                self.add(chart)

                chart.change_bar_values(list(reversed(values)))
                self.add(chart.get_bar_labels(font_size=24))

        ```

        ```

        class ChangeBarValuesExample(Scene):
            def construct(self):
                values=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

                chart = BarChart(
                    values,
                    y_range=[-10, 10, 2],
                    y_axis_config={"font_size": 24},
                )
                self.add(chart)

                chart.change_bar_values(list(reversed(values)))
                self.add(chart.get_bar_labels(font_size=24))


        ```

    get\_bar\_labels(*color=None*, *font\_size=24*, *buff=0.25*, *label\_constructor=<class 'manim.mobject.text.tex\_mobject.Tex'>*)[[source]](../_modules/manim/mobject/graphing/probability.html#BarChart.get_bar_labels)[¶](#manim.mobject.graphing.probability.BarChart.get_bar_labels "Link to this definition")
    :   Annotates each bar with its corresponding value. Use `self.bar_labels` to access the
        labels after creation.

        Parameters:
        :   * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*) – The color of each label. By default `None` and is based on the parent’s bar color.
            * **font\_size** (*float*) – The font size of each label.
            * **buff** (*float*) – The distance from each label to its bar. By default 0.4.
            * **label\_constructor** (*type**[*[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")*]*) – The Mobject class to construct the labels, by default [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex").

        Examples

        Example: GetBarLabelsExample [¶](#getbarlabelsexample)

        ![../_images/GetBarLabelsExample-1.png](../_images/GetBarLabelsExample-1.png)

        ```
        from manim import *

        class GetBarLabelsExample(Scene):
            def construct(self):
                chart = BarChart(values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], y_range=[0, 10, 1])

                c_bar_lbls = chart.get_bar_labels(
                    color=WHITE, label_constructor=MathTex, font_size=36
                )

                self.add(chart, c_bar_lbls)

        ```

        ```

        class GetBarLabelsExample(Scene):
            def construct(self):
                chart = BarChart(values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], y_range=[0, 10, 1])

                c_bar_lbls = chart.get_bar_labels(
                    color=WHITE, label_constructor=MathTex, font_size=36
                )

                self.add(chart, c_bar_lbls)


        ```