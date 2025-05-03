# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cylinder.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Cylinder[¶](#cylinder "Link to this heading")
=============================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cylinder`

*class* Cylinder(*radius=1*, *height=2*, *direction=array([0., 0., 1.])*, *v\_range=[0, 6.283185307179586]*, *show\_ends=True*, *resolution=(24, 24)*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder)[¶](#manim.mobject.three_d.three_dimensions.Cylinder "Link to this definition")
:   Bases: [`Surface`](manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

    A cylinder, defined by its height, radius and direction,

    Parameters:
    :   * **radius** (*float*) – The radius of the cylinder.
        * **height** (*float*) – The height of the cylinder.
        * **direction** (*np.ndarray*) – The direction of the central axis of the cylinder.
        * **v\_range** (*Sequence**[**float**]*) – The height along the height axis (given by direction) to start and end on.
        * **show\_ends** (*bool*) – Whether to show the end caps or not.
        * **resolution** (*Sequence**[**int**]*) – The number of samples taken of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder"). A tuple can be used
          to define different resolutions for `u` and `v` respectively.

    Examples

    Example: ExampleCylinder [¶](#examplecylinder)

    ![../_images/ExampleCylinder-1.png](../_images/ExampleCylinder-1.png)

    ```
    from manim import *

    class ExampleCylinder(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            cylinder = Cylinder(radius=2, height=3)
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, cylinder)

    ```

    ```

    class ExampleCylinder(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            cylinder = Cylinder(radius=2, height=3)
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, cylinder)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_bases`](#manim.mobject.three_d.three_dimensions.Cylinder.add_bases "manim.mobject.three_d.three_dimensions.Cylinder.add_bases") | Adds the end caps of the cylinder. |
    | [`func`](#manim.mobject.three_d.three_dimensions.Cylinder.func "manim.mobject.three_d.three_dimensions.Cylinder.func") | Converts from cylindrical coordinates to cartesian. |
    | [`get_direction`](#manim.mobject.three_d.three_dimensions.Cylinder.get_direction "manim.mobject.three_d.three_dimensions.Cylinder.get_direction") | Returns the direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder"). |
    | [`set_direction`](#manim.mobject.three_d.three_dimensions.Cylinder.set_direction "manim.mobject.three_d.three_dimensions.Cylinder.set_direction") | Sets the direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder"). |

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

    \_original\_\_init\_\_(*radius=1*, *height=2*, *direction=array([0., 0., 1.])*, *v\_range=[0, 6.283185307179586]*, *show\_ends=True*, *resolution=(24, 24)*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Cylinder._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **radius** (*float*)
            * **height** (*float*)
            * **direction** (*ndarray*)
            * **v\_range** (*Sequence**[**float**]*)
            * **show\_ends** (*bool*)
            * **resolution** (*Sequence**[**int**]*)

        Return type:
        :   None

    add\_bases()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.add_bases)[¶](#manim.mobject.three_d.three_dimensions.Cylinder.add_bases "Link to this definition")
    :   Adds the end caps of the cylinder.

        Return type:
        :   None

    func(*u*, *v*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.func)[¶](#manim.mobject.three_d.three_dimensions.Cylinder.func "Link to this definition")
    :   Converts from cylindrical coordinates to cartesian.

        Parameters:
        :   * **u** (*float*) – The height.
            * **v** (*float*) – The azimuthal angle.

        Returns:
        :   Points defining the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder").

        Return type:
        :   `numpy.ndarray`

    get\_direction()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.get_direction)[¶](#manim.mobject.three_d.three_dimensions.Cylinder.get_direction "Link to this definition")
    :   Returns the direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder").

        Returns:
        :   **direction** – The direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder").

        Return type:
        :   `numpy.array`

    set\_direction(*direction*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.set_direction)[¶](#manim.mobject.three_d.three_dimensions.Cylinder.set_direction "Link to this definition")
    :   Sets the direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder").

        Parameters:
        :   **direction** (`numpy.array`) – The direction of the central axis of the [`Cylinder`](#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder").

        Return type:
        :   None