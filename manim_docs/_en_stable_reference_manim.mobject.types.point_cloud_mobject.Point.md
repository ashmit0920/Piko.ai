# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.Point.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Point[¶](#point "Link to this heading")
=======================================

Qualified name: `manim.mobject.types.point\_cloud\_mobject.Point`

*class* Point(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#Point)[¶](#manim.mobject.types.point_cloud_mobject.Point "Link to this definition")
:   Bases: [`PMobject`](manim.mobject.types.point_cloud_mobject.PMobject.html#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")

    A mobject representing a point.

    Examples

    Example: ExamplePoint [¶](#examplepoint)

    ![../_images/ExamplePoint-1.png](../_images/ExamplePoint-1.png)

    ```
    from manim import *

    class ExamplePoint(Scene):
        def construct(self):
            colorList = [RED, GREEN, BLUE, YELLOW]
            for i in range(200):
                point = Point(location=[0.63 * np.random.randint(-4, 4), 0.37 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            for i in range(200):
                point = Point(location=[0.37 * np.random.randint(-4, 4), 0.63 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            self.add(point)

    ```

    ```

    class ExamplePoint(Scene):
        def construct(self):
            colorList = [RED, GREEN, BLUE, YELLOW]
            for i in range(200):
                point = Point(location=[0.63 * np.random.randint(-4, 4), 0.37 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            for i in range(200):
                point = Point(location=[0.37 * np.random.randint(-4, 4), 0.63 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
                self.add(point)
            self.add(point)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.types.point_cloud_mobject.Point.generate_points "manim.mobject.types.point_cloud_mobject.Point.generate_points") | Initializes `points` and therefore the shape. |
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
    :   * **location** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
        * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *\*\*kwargs*)[¶](#manim.mobject.types.point_cloud_mobject.Point._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **location** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))
            * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
            * **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#Point.generate_points)[¶](#manim.mobject.types.point_cloud_mobject.Point.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None