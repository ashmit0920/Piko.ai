# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cube.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Cube[¶](#cube "Link to this heading")
=====================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cube`

*class* Cube(*side\_length=2*, *fill\_opacity=0.75*, *fill\_color=ManimColor('#58C4DD')*, *stroke\_width=0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cube)[¶](#manim.mobject.three_d.three_dimensions.Cube "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    A three-dimensional cube.

    Parameters:
    :   * **side\_length** (*float*) – Length of each side of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").
        * **fill\_opacity** (*float*) – The opacity of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube"), from 0 being fully transparent to 1 being
          fully opaque. Defaults to 0.75.
        * **fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").
        * **stroke\_width** (*float*) – The width of the stroke surrounding each face of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").

    Examples

    Example: CubeExample [¶](#cubeexample)

    ![../_images/CubeExample-1.png](../_images/CubeExample-1.png)

    ```
    from manim import *

    class CubeExample(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

            axes = ThreeDAxes()
            cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
            self.add(cube)

    ```

    ```

    class CubeExample(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

            axes = ThreeDAxes()
            cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
            self.add(cube)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.three_d.three_dimensions.Cube.generate_points "manim.mobject.three_d.three_dimensions.Cube.generate_points") | Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube"). |
    | [`init_points`](#manim.mobject.three_d.three_dimensions.Cube.init_points "manim.mobject.three_d.three_dimensions.Cube.init_points") | Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube"). |

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

    \_original\_\_init\_\_(*side\_length=2*, *fill\_opacity=0.75*, *fill\_color=ManimColor('#58C4DD')*, *stroke\_width=0*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Cube._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **side\_length** (*float*)
            * **fill\_opacity** (*float*)
            * **fill\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **stroke\_width** (*float*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cube.generate_points)[¶](#manim.mobject.three_d.three_dimensions.Cube.generate_points "Link to this definition")
    :   Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").

        Return type:
        :   None

    init\_points()[¶](#manim.mobject.three_d.three_dimensions.Cube.init_points "Link to this definition")
    :   Creates the sides of the [`Cube`](#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube").

        Return type:
        :   None