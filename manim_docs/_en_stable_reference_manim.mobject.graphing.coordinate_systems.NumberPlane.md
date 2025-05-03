# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.NumberPlane.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

NumberPlane[¶](#numberplane "Link to this heading")
===================================================

Qualified name: `manim.mobject.graphing.coordinate\_systems.NumberPlane`

*class* NumberPlane(*x\_range=(-7.111111111111111, 7.111111111111111, 1)*, *y\_range=(-4.0, 4.0, 1)*, *x\_length=None*, *y\_length=None*, *background\_line\_style=None*, *faded\_line\_style=None*, *faded\_line\_ratio=1*, *make\_smooth\_after\_applying\_functions=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane)[¶](#manim.mobject.graphing.coordinate_systems.NumberPlane "Link to this definition")
:   Bases: [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes")

    Creates a cartesian plane with background lines.

    Parameters:
    :   * **x\_range** (*Sequence**[**float**]* *|* *None*) – The `[x_min, x_max, x_step]` values of the plane in the horizontal direction.
        * **y\_range** (*Sequence**[**float**]* *|* *None*) – The `[y_min, y_max, y_step]` values of the plane in the vertical direction.
        * **x\_length** (*float* *|* *None*) – The width of the plane.
        * **y\_length** (*float* *|* *None*) – The height of the plane.
        * **background\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*) – Arguments that influence the construction of the background lines of the plane.
        * **faded\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*) – Similar to `background_line_style`, affects the construction of the scene’s background lines.
        * **faded\_line\_ratio** (*int*) – Determines the number of boxes within the background lines: `2` = 4 boxes, `3` = 9 boxes.
        * **make\_smooth\_after\_applying\_functions** (*bool*) – Currently non-functional.
        * **kwargs** (*dict**[**str**,* *Any**]*) – Additional arguments to be passed to [`Axes`](manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes "manim.mobject.graphing.coordinate_systems.Axes").

    Note

    If `x_length` or `y_length` are not defined, they are automatically calculated such that
    one unit on each axis is one Manim unit long.

    Examples

    Example: NumberPlaneExample [¶](#numberplaneexample)

    ![../_images/NumberPlaneExample-1.png](../_images/NumberPlaneExample-1.png)

    ```
    from manim import *

    class NumberPlaneExample(Scene):
        def construct(self):
            number_plane = NumberPlane(
                background_line_style={
                    "stroke_color": TEAL,
                    "stroke_width": 4,
                    "stroke_opacity": 0.6
                }
            )
            self.add(number_plane)

    ```

    ```

    class NumberPlaneExample(Scene):
        def construct(self):
            number_plane = NumberPlane(
                background_line_style={
                    "stroke_color": TEAL,
                    "stroke_width": 4,
                    "stroke_opacity": 0.6
                }
            )
            self.add(number_plane)


    ```

    Example: NumberPlaneScaled [¶](#numberplanescaled)

    ![../_images/NumberPlaneScaled-1.png](../_images/NumberPlaneScaled-1.png)

    ```
    from manim import *

    class NumberPlaneScaled(Scene):
        def construct(self):
            number_plane = NumberPlane(
                x_range=(-4, 11, 1),
                y_range=(-3, 3, 1),
                x_length=5,
                y_length=2,
            ).move_to(LEFT*3)

            number_plane_scaled_y = NumberPlane(
                x_range=(-4, 11, 1),
                x_length=5,
                y_length=4,
            ).move_to(RIGHT*3)

            self.add(number_plane)
            self.add(number_plane_scaled_y)

    ```

    ```

    class NumberPlaneScaled(Scene):
        def construct(self):
            number_plane = NumberPlane(
                x_range=(-4, 11, 1),
                y_range=(-3, 3, 1),
                x_length=5,
                y_length=2,
            ).move_to(LEFT*3)

            number_plane_scaled_y = NumberPlane(
                x_range=(-4, 11, 1),
                x_length=5,
                y_length=4,
            ).move_to(RIGHT*3)

            self.add(number_plane)
            self.add(number_plane_scaled_y)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_vector` |  |
    | `prepare_for_nonlinear_transform` |  |

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

    \_get\_lines()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines)[¶](#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines "Link to this definition")
    :   Generate all the lines, faded and not faded.
        :   Two sets of lines are generated: one parallel to the X-axis, and parallel to the Y-axis.

        Returns:
        :   The first (i.e the non faded lines) and second (i.e the faded lines) sets of lines, respectively.

        Return type:
        :   Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")]

    \_get\_lines\_parallel\_to\_axis(*axis\_parallel\_to*, *axis\_perpendicular\_to*, *freq*, *ratio\_faded\_lines*)[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines_parallel_to_axis)[¶](#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines_parallel_to_axis "Link to this definition")
    :   Generate a set of lines parallel to an axis.

        Parameters:
        :   * **axis\_parallel\_to** ([*NumberLine*](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be parallel.
            * **axis\_perpendicular\_to** ([*NumberLine*](manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be perpendicular.
            * **ratio\_faded\_lines** (*int*) – The ratio between the space between faded lines and the space between non-faded lines.
            * **freq** (*float*) – Frequency of non-faded lines (number of non-faded lines per graph unit).

        Returns:
        :   The first (i.e the non-faded lines parallel to axis\_parallel\_to) and second
            :   (i.e the faded lines parallel to axis\_parallel\_to) sets of lines, respectively.

        Return type:
        :   Tuple[[`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup"), [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")]

    \_init\_background\_lines()[[source]](../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._init_background_lines)[¶](#manim.mobject.graphing.coordinate_systems.NumberPlane._init_background_lines "Link to this definition")
    :   Will init all the lines of NumberPlanes (faded or not)

        Return type:
        :   None

    \_original\_\_init\_\_(*x\_range=(-7.111111111111111, 7.111111111111111, 1)*, *y\_range=(-4.0, 4.0, 1)*, *x\_length=None*, *y\_length=None*, *background\_line\_style=None*, *faded\_line\_style=None*, *faded\_line\_ratio=1*, *make\_smooth\_after\_applying\_functions=True*, *\*\*kwargs*)[¶](#manim.mobject.graphing.coordinate_systems.NumberPlane._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **x\_range** (*Sequence**[**float**]* *|* *None*)
            * **y\_range** (*Sequence**[**float**]* *|* *None*)
            * **x\_length** (*float* *|* *None*)
            * **y\_length** (*float* *|* *None*)
            * **background\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
            * **faded\_line\_style** (*dict**[**str**,* *Any**]* *|* *None*)
            * **faded\_line\_ratio** (*int*)
            * **make\_smooth\_after\_applying\_functions** (*bool*)
            * **kwargs** (*dict**[**str**,* *Any**]*)