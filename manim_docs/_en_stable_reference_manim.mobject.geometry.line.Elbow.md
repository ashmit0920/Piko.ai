# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Elbow.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Elbow[¶](#elbow "Link to this heading")
=======================================

Qualified name: `manim.mobject.geometry.line.Elbow`

*class* Elbow(*width=0.2*, *angle=0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/line.html#Elbow)[¶](#manim.mobject.geometry.line.Elbow "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    Two lines that create a right angle about each other: L-shape.

    Parameters:
    :   * **width** (*float*) – The length of the elbow’s sides.
        * **angle** (*float*) – The rotation of the elbow.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")
        * **seealso::** (*..*) – [`RightAngle`](manim.mobject.geometry.line.RightAngle.html#manim.mobject.geometry.line.RightAngle "manim.mobject.geometry.line.RightAngle")

    Examples

    Example: ElbowExample [¶](#elbowexample)

    ![../_images/ElbowExample-1.png](../_images/ElbowExample-1.png)

    ```
    from manim import *

    class ElbowExample(Scene):
        def construct(self):
            elbow_1 = Elbow()
            elbow_2 = Elbow(width=2.0)
            elbow_3 = Elbow(width=2.0, angle=5*PI/4)

            elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
            self.add(elbow_group)

    ```

    ```

    class ElbowExample(Scene):
        def construct(self):
            elbow_1 = Elbow()
            elbow_2 = Elbow(width=2.0)
            elbow_3 = Elbow(width=2.0, angle=5*PI/4)

            elbow_group = Group(elbow_1, elbow_2, elbow_3).arrange(buff=1)
            self.add(elbow_group)


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
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*width=0.2*, *angle=0*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.Elbow._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **width** (*float*)
            * **angle** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None