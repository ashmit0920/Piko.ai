# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PointCloudDot.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

PointCloudDot[¶](#pointclouddot "Link to this heading")
=======================================================

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PointCloudDot`

*class* PointCloudDot(*center=array([0., 0., 0.])*, *radius=2.0*, *stroke\_width=2*, *density=10*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PointCloudDot)[¶](#manim.mobject.types.point_cloud_mobject.PointCloudDot "Link to this definition")
:   Bases: [`Mobject1D`](manim.mobject.types.point_cloud_mobject.Mobject1D.html#manim.mobject.types.point_cloud_mobject.Mobject1D "manim.mobject.types.point_cloud_mobject.Mobject1D")

    A disc made of a cloud of dots.

    Examples

    Example: PointCloudDotExample [¶](#pointclouddotexample)

    ![../_images/PointCloudDotExample-1.png](../_images/PointCloudDotExample-1.png)

    ```
    from manim import *

    class PointCloudDotExample(Scene):
        def construct(self):
            cloud_1 = PointCloudDot(color=RED)
            cloud_2 = PointCloudDot(stroke_width=4, radius=1)
            cloud_3 = PointCloudDot(density=15)

            group = Group(cloud_1, cloud_2, cloud_3).arrange()
            self.add(group)

    ```

    ```

    class PointCloudDotExample(Scene):
        def construct(self):
            cloud_1 = PointCloudDot(color=RED)
            cloud_2 = PointCloudDot(stroke_width=4, radius=1)
            cloud_3 = PointCloudDot(density=15)

            group = Group(cloud_1, cloud_2, cloud_3).arrange()
            self.add(group)


    ```

    Example: PointCloudDotExample2 [¶](#pointclouddotexample2)

    [
    ](./PointCloudDotExample2-1.mp4)

    ```
    from manim import *

    class PointCloudDotExample2(Scene):
        def construct(self):
            plane = ComplexPlane()
            cloud = PointCloudDot(color=RED)
            self.add(
                plane, cloud
            )
            self.wait()
            self.play(
                cloud.animate.apply_complex_function(lambda z: np.exp(z))
            )

    ```

    ```

    class PointCloudDotExample2(Scene):
        def construct(self):
            plane = ComplexPlane()
            cloud = PointCloudDot(color=RED)
            self.add(
                plane, cloud
            )
            self.wait()
            self.play(
                cloud.animate.apply_complex_function(lambda z: np.exp(z))
            )


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points "manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points") | Initializes `points` and therefore the shape. |
    | `init_points` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **center** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
        * **radius** (*float*)
        * **stroke\_width** (*int*)
        * **density** (*int*)
        * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*center=array([0., 0., 0.])*, *radius=2.0*, *stroke\_width=2*, *density=10*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[¶](#manim.mobject.types.point_cloud_mobject.PointCloudDot._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **center** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
            * **radius** (*float*)
            * **stroke\_width** (*int*)
            * **density** (*int*)
            * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
            * **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PointCloudDot.generate_points)[¶](#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None