# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Arrow3D.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Arrow3D[¶](#arrow3d "Link to this heading")
===========================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Arrow3D`

*class* Arrow3D(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *height=0.3*, *base\_radius=0.08*, *color=ManimColor('#FFFFFF')*, *resolution=24*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D)[¶](#manim.mobject.three_d.three_dimensions.Arrow3D "Link to this definition")
:   Bases: [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

    An arrow made out of a cylindrical line and a conical tip.

    Parameters:
    :   * **start** (*np.ndarray*) – The start position of the arrow.
        * **end** (*np.ndarray*) – The end position of the arrow.
        * **thickness** (*float*) – The thickness of the arrow.
        * **height** (*float*) – The height of the conical tip.
        * **base\_radius** (*float*) – The base radius of the conical tip.
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the arrow.
        * **resolution** (*int* *|* *Sequence**[**int**]*) – The resolution of the arrow line.

    Examples

    Example: ExampleArrow3D [¶](#examplearrow3d)

    ![../_images/ExampleArrow3D-1.png](../_images/ExampleArrow3D-1.png)

    ```
    from manim import *

    class ExampleArrow3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            arrow = Arrow3D(
                start=np.array([0, 0, 0]),
                end=np.array([2, 2, 2]),
                resolution=8
            )
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, arrow)

    ```

    ```

    class ExampleArrow3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            arrow = Arrow3D(
                start=np.array([0, 0, 0]),
                end=np.array([2, 2, 2]),
                resolution=8
            )
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, arrow)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Arrow3D.get_end "manim.mobject.three_d.three_dimensions.Arrow3D.get_end") | Returns the ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |

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

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *height=0.3*, *base\_radius=0.08*, *color=ManimColor('#FFFFFF')*, *resolution=24*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Arrow3D._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start** (*ndarray*)
            * **end** (*ndarray*)
            * **thickness** (*float*)
            * **height** (*float*)
            * **base\_radius** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **resolution** (*int* *|* *Sequence**[**int**]*)

        Return type:
        :   None

    get\_end()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D.get_end)[¶](#manim.mobject.three_d.three_dimensions.Arrow3D.get_end "Link to this definition")
    :   Returns the ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Returns:
        :   **end** – Ending point of the [`Line3D`](manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Return type:
        :   `numpy.array`