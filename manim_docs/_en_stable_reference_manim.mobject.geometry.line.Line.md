# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Line.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Line[¶](#line "Link to this heading")
=====================================

Qualified name: `manim.mobject.geometry.line.Line`

*class* Line(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *buff=0*, *path\_arc=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/line.html#Line)[¶](#manim.mobject.geometry.line.Line "Link to this definition")
:   Bases: [`TipableVMobject`](manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject "manim.mobject.geometry.arc.TipableVMobject")

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.geometry.line.Line.generate_points "manim.mobject.geometry.line.Line.generate_points") | Initializes `points` and therefore the shape. |
    | `get_angle` |  |
    | [`get_projection`](#manim.mobject.geometry.line.Line.get_projection "manim.mobject.geometry.line.Line.get_projection") | Returns the projection of a point onto a line. |
    | `get_slope` |  |
    | `get_unit_vector` |  |
    | `get_vector` |  |
    | [`init_points`](#manim.mobject.geometry.line.Line.init_points "manim.mobject.geometry.line.Line.init_points") | Initializes `points` and therefore the shape. |
    | [`put_start_and_end_on`](#manim.mobject.geometry.line.Line.put_start_and_end_on "manim.mobject.geometry.line.Line.put_start_and_end_on") | Sets starts and end coordinates of a line. |
    | `set_angle` |  |
    | `set_length` |  |
    | `set_path_arc` |  |
    | [`set_points_by_ends`](#manim.mobject.geometry.line.Line.set_points_by_ends "manim.mobject.geometry.line.Line.set_points_by_ends") | Sets the points of the line based on its start and end points. |

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

    Parameters:
    :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **buff** (*float*)
        * **path\_arc** (*float* *|* *None*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*start=array([-1., 0., 0.])*, *end=array([1., 0., 0.])*, *buff=0*, *path\_arc=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.Line._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **buff** (*float*)
            * **path\_arc** (*float* *|* *None*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    \_pointify(*mob\_or\_point*, *direction=None*)[[source]](../_modules/manim/mobject/geometry/line.html#Line._pointify)[¶](#manim.mobject.geometry.line.Line._pointify "Link to this definition")
    :   Transforms a mobject into its corresponding point. Does nothing if a point is passed.

        `direction` determines the location of the point along its bounding box in that direction.

        Parameters:
        :   * **mob\_or\_point** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") *|* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The mobject or point.
            * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") *|* *None*) – The direction.

        Return type:
        :   [Point3D](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    generate\_points()[[source]](../_modules/manim/mobject/geometry/line.html#Line.generate_points)[¶](#manim.mobject.geometry.line.Line.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None

    get\_projection(*point*)[[source]](../_modules/manim/mobject/geometry/line.html#Line.get_projection)[¶](#manim.mobject.geometry.line.Line.get_projection "Link to this definition")
    :   Returns the projection of a point onto a line.

        Parameters:
        :   **point** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The point to which the line is projected.

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    init\_points()[¶](#manim.mobject.geometry.line.Line.init_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None

    put\_start\_and\_end\_on(*start*, *end*)[[source]](../_modules/manim/mobject/geometry/line.html#Line.put_start_and_end_on)[¶](#manim.mobject.geometry.line.Line.put_start_and_end_on "Link to this definition")
    :   Sets starts and end coordinates of a line.

        Examples

        Example: LineExample [¶](#lineexample)

        [
        ](./LineExample-1.mp4)

        ```
        from manim import *

        class LineExample(Scene):
            def construct(self):
                d = VGroup()
                for i in range(0,10):
                    d.add(Dot())
                d.arrange_in_grid(buff=1)
                self.add(d)
                l= Line(d[0], d[1])
                self.add(l)
                self.wait()
                l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
                self.wait()
                l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
                self.wait()

        ```

        ```

        class LineExample(Scene):
            def construct(self):
                d = VGroup()
                for i in range(0,10):
                    d.add(Dot())
                d.arrange_in_grid(buff=1)
                self.add(d)
                l= Line(d[0], d[1])
                self.add(l)
                self.wait()
                l.put_start_and_end_on(d[1].get_center(), d[2].get_center())
                self.wait()
                l.put_start_and_end_on(d[4].get_center(), d[7].get_center())
                self.wait()


        ```

        Parameters:
        :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

        Return type:
        :   Self

    set\_points\_by\_ends(*start*, *end*, *buff=0*, *path\_arc=0*)[[source]](../_modules/manim/mobject/geometry/line.html#Line.set_points_by_ends)[¶](#manim.mobject.geometry.line.Line.set_points_by_ends "Link to this definition")
    :   Sets the points of the line based on its start and end points.
        Unlike [`put_start_and_end_on()`](#manim.mobject.geometry.line.Line.put_start_and_end_on "manim.mobject.geometry.line.Line.put_start_and_end_on"), this method respects self.buff and
        Mobject bounding boxes.

        Parameters:
        :   * **start** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The start point or Mobject of the line.
            * **end** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The end point or Mobject of the line.
            * **buff** (*float*) – The empty space between the start and end of the line, by default 0.
            * **path\_arc** (*float*) – The angle of a circle spanned by this arc, by default 0 which is a straight line.

        Return type:
        :   None