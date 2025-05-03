# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Torus.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Torus[¶](#torus "Link to this heading")
=======================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Torus`

*class* Torus(*major\_radius=3*, *minor\_radius=1*, *u\_range=(0, 6.283185307179586)*, *v\_range=(0, 6.283185307179586)*, *resolution=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Torus)[¶](#manim.mobject.three_d.three_dimensions.Torus "Link to this definition")
:   Bases: [`Surface`](manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

    A torus.

    Parameters:
    :   * **major\_radius** (*float*) – Distance from the center of the tube to the center of the torus.
        * **minor\_radius** (*float*) – Radius of the tube.
        * **u\_range** (*Sequence**[**float**]*) – The range of the `u` variable: `(u_min, u_max)`.
        * **v\_range** (*Sequence**[**float**]*) – The range of the `v` variable: `(v_min, v_max)`.
        * **resolution** (*tuple**[**int**,* *int**]* *|* *None*) – The number of samples taken of the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus"). A tuple can be
          used to define different resolutions for `u` and `v` respectively.

    Examples

    Example: ExampleTorus [¶](#exampletorus)

    ![../_images/ExampleTorus-1.png](../_images/ExampleTorus-1.png)

    ```
    from manim import *

    class ExampleTorus(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            torus = Torus()
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, torus)

    ```

    ```

    class ExampleTorus(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            torus = Torus()
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, torus)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`func`](#manim.mobject.three_d.three_dimensions.Torus.func "manim.mobject.three_d.three_dimensions.Torus.func") | The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus") being plotted. |

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

    \_original\_\_init\_\_(*major\_radius=3*, *minor\_radius=1*, *u\_range=(0, 6.283185307179586)*, *v\_range=(0, 6.283185307179586)*, *resolution=None*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Torus._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **major\_radius** (*float*)
            * **minor\_radius** (*float*)
            * **u\_range** (*Sequence**[**float**]*)
            * **v\_range** (*Sequence**[**float**]*)
            * **resolution** (*tuple**[**int**,* *int**]* *|* *None*)

        Return type:
        :   None

    func(*u*, *v*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Torus.func)[¶](#manim.mobject.three_d.three_dimensions.Torus.func "Link to this definition")
    :   The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus") being plotted.

        Returns:
        :   The z values defining the [`Torus`](#manim.mobject.three_d.three_dimensions.Torus "manim.mobject.three_d.three_dimensions.Torus").

        Return type:
        :   `numpy.ndarray`

        Parameters:
        :   * **u** (*float*)
            * **v** (*float*)