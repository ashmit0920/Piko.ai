# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PGroup.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

PGroup[¶](#pgroup "Link to this heading")
=========================================

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PGroup`

*class* PGroup(*\*pmobs*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PGroup)[¶](#manim.mobject.types.point_cloud_mobject.PGroup "Link to this definition")
:   Bases: [`PMobject`](manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")

    A group for several point mobjects.

    Examples

    Example: PgroupExample [¶](#pgroupexample)

    ![../_images/PgroupExample-1.png](../_images/PgroupExample-1.png)

    ```
    from manim import *

    class PgroupExample(Scene):
        def construct(self):

            p1 = PointCloudDot(radius=1, density=20, color=BLUE)
            p1.move_to(4.5 * LEFT)
            p2 = PointCloudDot()
            p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
            p3.move_to(4.5 * RIGHT)
            pList = PGroup(p1, p2, p3)

            self.add(pList)

    ```

    ```

    class PgroupExample(Scene):
        def construct(self):

            p1 = PointCloudDot(radius=1, density=20, color=BLUE)
            p1.move_to(4.5 * LEFT)
            p2 = PointCloudDot()
            p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
            p3.move_to(4.5 * RIGHT)
            pList = PGroup(p1, p2, p3)

            self.add(pList)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `fade_to` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **pmobs** (*Any*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*\*pmobs*, *\*\*kwargs*)[¶](#manim.mobject.types.point_cloud_mobject.PGroup._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **pmobs** (*Any*)
            * **kwargs** (*Any*)

        Return type:
        :   None