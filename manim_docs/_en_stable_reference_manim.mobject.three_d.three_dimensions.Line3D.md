# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Line3D.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Line3D[¶](#line3d "Link to this heading")
=========================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Line3D`

*class* Line3D(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *color=None*, *resolution=24*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D)[¶](#manim.mobject.three_d.three_dimensions.Line3D "Link to this definition")
:   Bases: [`Cylinder`](manim.mobject.three_d.three_dimensions.Cylinder.html#manim.mobject.three_d.three_dimensions.Cylinder "manim.mobject.three_d.three_dimensions.Cylinder")

    A cylindrical line, for use in ThreeDScene.

    Parameters:
    :   * **start** (*np.ndarray*) – The start point of the line.
        * **end** (*np.ndarray*) – The end point of the line.
        * **thickness** (*float*) – The thickness of the line.
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*) – The color of the line.
        * **resolution** (*int* *|* *Sequence**[**int**]*) – The resolution of the line.
          By default this value is the number of points the line will sampled at.
          If you want the line to also come out checkered, use a tuple.
          For example, for a line made of 24 points with 4 checker points on each
          cylinder, pass the tuple (4, 24).

    Examples

    Example: ExampleLine3D [¶](#exampleline3d)

    ![../_images/ExampleLine3D-1.png](../_images/ExampleLine3D-1.png)

    ```
    from manim import *

    class ExampleLine3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, line)

    ```

    ```

    class ExampleLine3D(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(axes, line)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.three_d.three_dimensions.Line3D.get_end "manim.mobject.three_d.three_dimensions.Line3D.get_end") | Returns the ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |
    | [`get_start`](#manim.mobject.three_d.three_dimensions.Line3D.get_start "manim.mobject.three_d.three_dimensions.Line3D.get_start") | Returns the starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D"). |
    | [`parallel_to`](#manim.mobject.three_d.three_dimensions.Line3D.parallel_to "manim.mobject.three_d.three_dimensions.Line3D.parallel_to") | Returns a line parallel to another line going through a given point. |
    | [`perpendicular_to`](#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to "manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to") | Returns a line perpendicular to another line going through a given point. |
    | [`pointify`](#manim.mobject.three_d.three_dimensions.Line3D.pointify "manim.mobject.three_d.three_dimensions.Line3D.pointify") | Gets a point representing the center of the [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
    | [`set_start_and_end_attrs`](#manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs "manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs") | Sets the start and end points of the line. |

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

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *thickness=0.02*, *color=None*, *resolution=24*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Line3D._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start** (*np.ndarray*)
            * **end** (*np.ndarray*)
            * **thickness** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
            * **resolution** (*int* *|* *Sequence**[**int**]*)

    get\_end()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.get_end)[¶](#manim.mobject.three_d.three_dimensions.Line3D.get_end "Link to this definition")
    :   Returns the ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Returns:
        :   **end** – Ending point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Return type:
        :   `numpy.array`

    get\_start()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.get_start)[¶](#manim.mobject.three_d.three_dimensions.Line3D.get_start "Link to this definition")
    :   Returns the starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Returns:
        :   **start** – Starting point of the [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D").

        Return type:
        :   `numpy.array`

    *classmethod* parallel\_to(*line*, *point=array([0., 0., 0.])*, *length=5*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.parallel_to)[¶](#manim.mobject.three_d.three_dimensions.Line3D.parallel_to "Link to this definition")
    :   Returns a line parallel to another line going through
        a given point.

        Parameters:
        :   * **line** ([*Line3D*](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")) – The line to be parallel to.
            * **point** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The point to pass through.
            * **length** (*float*) – Length of the parallel line.
            * **kwargs** – Additional parameters to be passed to the class.

        Returns:
        :   Line parallel to `line`.

        Return type:
        :   [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

        Examples

        Example: ParallelLineExample [¶](#parallellineexample)

        ![../_images/ParallelLineExample-1.png](../_images/ParallelLineExample-1.png)

        ```
        from manim import *

        class ParallelLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.parallel_to(line1, color=YELLOW)
                self.add(ax, line1, line2)

        ```

        ```

        class ParallelLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.parallel_to(line1, color=YELLOW)
                self.add(ax, line1, line2)


        ```

    *classmethod* perpendicular\_to(*line*, *point=array([0., 0., 0.])*, *length=5*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.perpendicular_to)[¶](#manim.mobject.three_d.three_dimensions.Line3D.perpendicular_to "Link to this definition")
    :   Returns a line perpendicular to another line going through
        a given point.

        Parameters:
        :   * **line** ([*Line3D*](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")) – The line to be perpendicular to.
            * **point** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The point to pass through.
            * **length** (*float*) – Length of the perpendicular line.
            * **kwargs** – Additional parameters to be passed to the class.

        Returns:
        :   Line perpendicular to `line`.

        Return type:
        :   [`Line3D`](#manim.mobject.three_d.three_dimensions.Line3D "manim.mobject.three_d.three_dimensions.Line3D")

        Examples

        Example: PerpLineExample [¶](#perplineexample)

        ![../_images/PerpLineExample-1.png](../_images/PerpLineExample-1.png)

        ```
        from manim import *

        class PerpLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.perpendicular_to(line1, color=BLUE)
                self.add(ax, line1, line2)

        ```

        ```

        class PerpLineExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(PI / 3, -PI / 4)
                ax = ThreeDAxes((-5, 5), (-5, 5), (-5, 5), 10, 10, 10)
                line1 = Line3D(RIGHT * 2, UP + OUT, color=RED)
                line2 = Line3D.perpendicular_to(line1, color=BLUE)
                self.add(ax, line1, line2)


        ```

    pointify(*mob\_or\_point*, *direction=None*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.pointify)[¶](#manim.mobject.three_d.three_dimensions.Line3D.pointify "Link to this definition")
    :   Gets a point representing the center of the [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

        Parameters:
        :   * **mob\_or\_point** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or point whose center should be returned.
            * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – If an edge of a [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") should be returned, the direction of the edge.

        Returns:
        :   Center of the [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or point, or edge if direction is given.

        Return type:
        :   `numpy.array`

    set\_start\_and\_end\_attrs(*start*, *end*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Line3D.set_start_and_end_attrs)[¶](#manim.mobject.three_d.three_dimensions.Line3D.set_start_and_end_attrs "Link to this definition")
    :   Sets the start and end points of the line.

        If either `start` or `end` are [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"),
        this gives their centers.

        Parameters:
        :   * **start** (*ndarray*) – Starting point or `Mobject`.
            * **end** (*ndarray*) – Ending point or `Mobject`.

        Return type:
        :   None