# Source: https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceBetweenPoints.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

BraceBetweenPoints[¶](#bracebetweenpoints "Link to this heading")
=================================================================

Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`

*class* BraceBetweenPoints(*point\_1*, *point\_2*, *direction=array([0., 0., 0.])*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#BraceBetweenPoints)[¶](#manim.mobject.svg.brace.BraceBetweenPoints "Link to this definition")
:   Bases: [`Brace`](manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace")

    Similar to Brace, but instead of taking a mobject it uses 2
    points to place the brace.

    A fitting direction for the brace is
    computed, but it still can be manually overridden.
    If the points go from left to right, the brace is drawn from below.
    Swapping the points places the brace on the opposite side.

    Parameters:
    :   * **point\_1** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*) – The first point.
        * **point\_2** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*) – The second point.
        * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") *|* *None*) – The direction from which the brace faces towards the points.

    Examples

    Example: BraceBPExample [¶](#bracebpexample)

    [
    ](./BraceBPExample-1.mp4)

    ```
    from manim import *

    class BraceBPExample(Scene):
        def construct(self):
            p1 = [0,0,0]
            p2 = [1,2,0]
            brace = BraceBetweenPoints(p1,p2)
            self.play(Create(NumberPlane()))
            self.play(Create(brace))
            self.wait(2)

    ```

    ```

    class BraceBPExample(Scene):
        def construct(self):
            p1 = [0,0,0]
            p2 = [1,2,0]
            brace = BraceBetweenPoints(p1,p2)
            self.play(Create(NumberPlane()))
            self.play(Create(brace))
            self.wait(2)


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

    \_original\_\_init\_\_(*point\_1*, *point\_2*, *direction=array([0., 0., 0.])*, *\*\*kwargs*)[¶](#manim.mobject.svg.brace.BraceBetweenPoints._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **point\_1** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*)
            * **point\_2** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*)
            * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") *|* *None*)