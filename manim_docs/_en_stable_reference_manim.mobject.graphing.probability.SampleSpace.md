# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.probability.SampleSpace.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SampleSpace[¶](#samplespace "Link to this heading")
===================================================

Qualified name: `manim.mobject.graphing.probability.SampleSpace`

*class* SampleSpace(*height=3*, *width=3*, *fill\_color=ManimColor('#444444')*, *fill\_opacity=1*, *stroke\_width=0.5*, *stroke\_color=ManimColor('#BBBBBB')*, *default\_label\_scale\_val=1*)[[source]](../_modules/manim/mobject/graphing/probability.html#SampleSpace)[¶](#manim.mobject.graphing.probability.SampleSpace "Link to this definition")
:   Bases: [`Rectangle`](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    A mobject representing a twodimensional rectangular
    sampling space.

    Examples

    Example: ExampleSampleSpace [¶](#examplesamplespace)

    ![../_images/ExampleSampleSpace-1.png](../_images/ExampleSampleSpace-1.png)

    ```
    from manim import *

    class ExampleSampleSpace(Scene):
        def construct(self):
            poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
            poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
            poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
            poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
            poly_group = VGroup(poly1, poly2, poly3).arrange()
            self.add(poly_group)

    ```

    ```

    class ExampleSampleSpace(Scene):
        def construct(self):
            poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
            poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
            poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
            poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
            poly_group = VGroup(poly1, poly2, poly3).arrange()
            self.add(poly_group)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `add_braces_and_labels` |  |
    | `add_label` |  |
    | `add_title` |  |
    | `complete_p_list` |  |
    | `divide_horizontally` |  |
    | `divide_vertically` |  |
    | `get_bottom_braces_and_labels` |  |
    | `get_division_along_dimension` |  |
    | `get_horizontal_division` |  |
    | `get_side_braces_and_labels` |  |
    | `get_subdivision_braces_and_labels` |  |
    | `get_top_braces_and_labels` |  |
    | `get_vertical_division` |  |

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

    \_original\_\_init\_\_(*height=3*, *width=3*, *fill\_color=ManimColor('#444444')*, *fill\_opacity=1*, *stroke\_width=0.5*, *stroke\_color=ManimColor('#BBBBBB')*, *default\_label\_scale\_val=1*)[¶](#manim.mobject.graphing.probability.SampleSpace._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.