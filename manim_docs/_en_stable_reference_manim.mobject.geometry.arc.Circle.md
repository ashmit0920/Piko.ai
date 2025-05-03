# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Circle.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Circle[¶](#circle "Link to this heading")
=========================================

Qualified name: `manim.mobject.geometry.arc.Circle`

*class* Circle(*radius=None*, *color=ManimColor('#FC6255')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Circle)[¶](#manim.mobject.geometry.arc.Circle "Link to this definition")
:   Bases: [`Arc`](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

    A circle.

    Parameters:
    :   * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color of the shape.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Arc`](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")
        * **radius** (*float* *|* *None*)

    Examples

    Example: CircleExample [¶](#circleexample)

    ![../_images/CircleExample-1.png](../_images/CircleExample-1.png)

    ```
    from manim import *

    class CircleExample(Scene):
        def construct(self):
            circle_1 = Circle(radius=1.0)
            circle_2 = Circle(radius=1.5, color=GREEN)
            circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

            circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
            self.add(circle_group)

    ```

    ```

    class CircleExample(Scene):
        def construct(self):
            circle_1 = Circle(radius=1.0)
            circle_2 = Circle(radius=1.5, color=GREEN)
            circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)

            circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
            self.add(circle_group)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`from_three_points`](#manim.mobject.geometry.arc.Circle.from_three_points "manim.mobject.geometry.arc.Circle.from_three_points") | Returns a circle passing through the specified three points. |
    | [`point_at_angle`](#manim.mobject.geometry.arc.Circle.point_at_angle "manim.mobject.geometry.arc.Circle.point_at_angle") | Returns the position of a point on the circle. |
    | [`surround`](#manim.mobject.geometry.arc.Circle.surround "manim.mobject.geometry.arc.Circle.surround") | Modifies a circle so that it surrounds a given mobject. |

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

    \_original\_\_init\_\_(*radius=None*, *color=ManimColor('#FC6255')*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Circle._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **radius** (*float* *|* *None*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **kwargs** (*Any*)

        Return type:
        :   None

    *static* from\_three\_points(*p1*, *p2*, *p3*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Circle.from_three_points)[¶](#manim.mobject.geometry.arc.Circle.from_three_points "Link to this definition")
    :   Returns a circle passing through the specified
        three points.

        Example

        Example: CircleFromPointsExample [¶](#circlefrompointsexample)

        ![../_images/CircleFromPointsExample-1.png](../_images/CircleFromPointsExample-1.png)

        ```
        from manim import *

        class CircleFromPointsExample(Scene):
            def construct(self):
                circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
                dots = VGroup(
                    Dot(LEFT),
                    Dot(LEFT + UP),
                    Dot(UP * 2),
                )
                self.add(NumberPlane(), circle, dots)

        ```

        ```

        class CircleFromPointsExample(Scene):
            def construct(self):
                circle = Circle.from_three_points(LEFT, LEFT + UP, UP * 2, color=RED)
                dots = VGroup(
                    Dot(LEFT),
                    Dot(LEFT + UP),
                    Dot(UP * 2),
                )
                self.add(NumberPlane(), circle, dots)


        ```

        Parameters:
        :   * **p1** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **p2** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **p3** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **kwargs** (*Any*)

        Return type:
        :   [Circle](#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    point\_at\_angle(*angle*)[[source]](../_modules/manim/mobject/geometry/arc.html#Circle.point_at_angle)[¶](#manim.mobject.geometry.arc.Circle.point_at_angle "Link to this definition")
    :   Returns the position of a point on the circle.

        Parameters:
        :   **angle** (*float*) – The angle of the point along the circle in radians.

        Returns:
        :   The location of the point along the circle’s circumference.

        Return type:
        :   `numpy.ndarray`

        Examples

        Example: PointAtAngleExample [¶](#pointatangleexample)

        ![../_images/PointAtAngleExample-1.png](../_images/PointAtAngleExample-1.png)

        ```
        from manim import *

        class PointAtAngleExample(Scene):
            def construct(self):
                circle = Circle(radius=2.0)
                p1 = circle.point_at_angle(PI/2)
                p2 = circle.point_at_angle(270*DEGREES)

                s1 = Square(side_length=0.25).move_to(p1)
                s2 = Square(side_length=0.25).move_to(p2)
                self.add(circle, s1, s2)

        ```

        ```

        class PointAtAngleExample(Scene):
            def construct(self):
                circle = Circle(radius=2.0)
                p1 = circle.point_at_angle(PI/2)
                p2 = circle.point_at_angle(270*DEGREES)

                s1 = Square(side_length=0.25).move_to(p1)
                s2 = Square(side_length=0.25).move_to(p2)
                self.add(circle, s1, s2)


        ```

    surround(*mobject*, *dim\_to\_match=0*, *stretch=False*, *buffer\_factor=1.2*)[[source]](../_modules/manim/mobject/geometry/arc.html#Circle.surround)[¶](#manim.mobject.geometry.arc.Circle.surround "Link to this definition")
    :   Modifies a circle so that it surrounds a given mobject.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject that the circle will be surrounding.
            * **dim\_to\_match** (*int*)
            * **buffer\_factor** (*float*) – Scales the circle with respect to the mobject. A buffer\_factor < 1 makes the circle smaller than the mobject.
            * **stretch** (*bool*) – Stretches the circle to fit more tightly around the mobject. Note: Does not work with `Line`

        Return type:
        :   Self

        Examples

        Example: CircleSurround [¶](#circlesurround)

        ![../_images/CircleSurround-1.png](../_images/CircleSurround-1.png)

        ```
        from manim import *

        class CircleSurround(Scene):
            def construct(self):
                triangle1 = Triangle()
                circle1 = Circle().surround(triangle1)
                group1 = Group(triangle1,circle1) # treat the two mobjects as one

                line2 = Line()
                circle2 = Circle().surround(line2, buffer_factor=2.0)
                group2 = Group(line2,circle2)

                # buffer_factor < 1, so the circle is smaller than the square
                square3 = Square()
                circle3 = Circle().surround(square3, buffer_factor=0.5)
                group3 = Group(square3, circle3)

                group = Group(group1, group2, group3).arrange(buff=1)
                self.add(group)

        ```

        ```

        class CircleSurround(Scene):
            def construct(self):
                triangle1 = Triangle()
                circle1 = Circle().surround(triangle1)
                group1 = Group(triangle1,circle1) # treat the two mobjects as one

                line2 = Line()
                circle2 = Circle().surround(line2, buffer_factor=2.0)
                group2 = Group(line2,circle2)

                # buffer_factor < 1, so the circle is smaller than the square
                square3 = Square()
                circle3 = Circle().surround(square3, buffer_factor=0.5)
                group3 = Group(square3, circle3)

                group = Group(group1, group2, group3).arrange(buff=1)
                self.add(group)


        ```