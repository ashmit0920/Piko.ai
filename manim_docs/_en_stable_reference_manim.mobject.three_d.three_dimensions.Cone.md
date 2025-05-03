# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Cone.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Cone[¶](#cone "Link to this heading")
=====================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Cone`

*class* Cone(*base\_radius=1*, *height=1*, *direction=array([0., 0., 1.])*, *show\_base=False*, *v\_range=[0, 6.283185307179586]*, *u\_min=0*, *checkerboard\_colors=False*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone)[¶](#manim.mobject.three_d.three_dimensions.Cone "Link to this definition")
:   Bases: [`Surface`](manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface "manim.mobject.three_d.three_dimensions.Surface")

    A circular cone.
    Can be defined using 2 parameters: its height, and its base radius.
    The polar angle, theta, can be calculated using arctan(base\_radius /
    height) The spherical radius, r, is calculated using the pythagorean
    theorem.

    Parameters:
    :   * **base\_radius** (*float*) – The base radius from which the cone tapers.
        * **height** (*float*) – The height measured from the plane formed by the base\_radius to
          the apex of the cone.
        * **direction** (*np.ndarray*) – The direction of the apex.
        * **show\_base** (*bool*) – Whether to show the base plane or not.
        * **v\_range** (*Sequence**[**float**]*) – The azimuthal angle to start and end at.
        * **u\_min** (*float*) – The radius at the apex.
        * **checkerboard\_colors** (*bool*) – Show checkerboard grid texture on the cone.
        * **kwargs** (*Any*)

    Examples

    Example: ExampleCone [¶](#examplecone)

    ![../_images/ExampleCone-1.png](../_images/ExampleCone-1.png)

    ```
    from manim import *

    class ExampleCone(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
            self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
            self.add(axes, cone)

    ```

    ```

    class ExampleCone(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
            self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
            self.add(axes, cone)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`func`](#manim.mobject.three_d.three_dimensions.Cone.func "manim.mobject.three_d.three_dimensions.Cone.func") | Converts from spherical coordinates to cartesian. |
    | [`get_direction`](#manim.mobject.three_d.three_dimensions.Cone.get_direction "manim.mobject.three_d.three_dimensions.Cone.get_direction") | Returns the current direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone"). |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Cone.get_end "manim.mobject.three_d.three_dimensions.Cone.get_end") | Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends. |
    | [`get_start`](#manim.mobject.three_d.three_dimensions.Cone.get_start "manim.mobject.three_d.three_dimensions.Cone.get_start") | Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts. |
    | [`set_direction`](#manim.mobject.three_d.three_dimensions.Cone.set_direction "manim.mobject.three_d.three_dimensions.Cone.set_direction") | Changes the direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone"). |

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

    \_original\_\_init\_\_(*base\_radius=1*, *height=1*, *direction=array([0., 0., 1.])*, *show\_base=False*, *v\_range=[0, 6.283185307179586]*, *u\_min=0*, *checkerboard\_colors=False*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Cone._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **base\_radius** (*float*)
            * **height** (*float*)
            * **direction** (*ndarray*)
            * **show\_base** (*bool*)
            * **v\_range** (*Sequence**[**float**]*)
            * **u\_min** (*float*)
            * **checkerboard\_colors** (*bool*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    func(*u*, *v*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone.func)[¶](#manim.mobject.three_d.three_dimensions.Cone.func "Link to this definition")
    :   Converts from spherical coordinates to cartesian.

        Parameters:
        :   * **u** (*float*) – The radius.
            * **v** (*float*) – The azimuthal angle.

        Returns:
        :   Points defining the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

        Return type:
        :   `numpy.array`

    get\_direction()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_direction)[¶](#manim.mobject.three_d.three_dimensions.Cone.get_direction "Link to this definition")
    :   Returns the current direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

        Returns:
        :   **direction** – The direction of the apex.

        Return type:
        :   `numpy.array`

    get\_end()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_end)[¶](#manim.mobject.three_d.three_dimensions.Cone.get_end "Link to this definition")
    :   Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends.

        Return type:
        :   *ndarray*

    get\_start()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone.get_start)[¶](#manim.mobject.three_d.three_dimensions.Cone.get_start "Link to this definition")
    :   Returns the point, where the stroke that surrounds the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts.

        Return type:
        :   *ndarray*

    set\_direction(*direction*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Cone.set_direction)[¶](#manim.mobject.three_d.three_dimensions.Cone.set_direction "Link to this definition")
    :   Changes the direction of the apex of the [`Cone`](#manim.mobject.three_d.three_dimensions.Cone "manim.mobject.three_d.three_dimensions.Cone").

        Parameters:
        :   **direction** (*ndarray*) – The direction of the apex.

        Return type:
        :   None