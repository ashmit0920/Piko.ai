# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.Vector.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Vector[¶](#vector "Link to this heading")
=========================================

Qualified name: `manim.mobject.geometry.line.Vector`

*class* Vector(*direction=array([1., 0., 0.])*, *buff=0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/line.html#Vector)[¶](#manim.mobject.geometry.line.Vector "Link to this definition")
:   Bases: [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    A vector specialized for use in graphs.

    Caution

    Do not confuse with the [`Vector2D`](manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D"),
    [`Vector3D`](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") or [`VectorND`](manim.typing.html#manim.typing.VectorND "manim.typing.VectorND") type aliases,
    which are not Mobjects!

    Parameters:
    :   * **direction** ([*Point2DLike*](manim.typing.html#manim.typing.Point2DLike "manim.typing.Point2DLike") *|* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The direction of the arrow.
        * **buff** (*float*) – The distance of the vector from its endpoints.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    Examples

    Example: VectorExample [¶](#vectorexample)

    ![../_images/VectorExample-1.png](../_images/VectorExample-1.png)

    ```
    from manim import *

    class VectorExample(Scene):
        def construct(self):
            plane = NumberPlane()
            vector_1 = Vector([1,2])
            vector_2 = Vector([-5,-2])
            self.add(plane, vector_1, vector_2)

    ```

    ```

    class VectorExample(Scene):
        def construct(self):
            plane = NumberPlane()
            vector_1 = Vector([1,2])
            vector_2 = Vector([-5,-2])
            self.add(plane, vector_1, vector_2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`coordinate_label`](#manim.mobject.geometry.line.Vector.coordinate_label "manim.mobject.geometry.line.Vector.coordinate_label") | Creates a label based on the coordinates of the vector. |

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

    \_original\_\_init\_\_(*direction=array([1., 0., 0.])*, *buff=0*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.Vector._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **direction** ([*Point2DLike*](manim.typing.html#manim.typing.Point2DLike "manim.typing.Point2DLike") *|* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **buff** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    coordinate\_label(*integer\_labels=True*, *n\_dim=2*, *color=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/line.html#Vector.coordinate_label)[¶](#manim.mobject.geometry.line.Vector.coordinate_label "Link to this definition")
    :   Creates a label based on the coordinates of the vector.

        Parameters:
        :   * **integer\_labels** (*bool*) – Whether or not to round the coordinates to integers.
            * **n\_dim** (*int*) – The number of dimensions of the vector.
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*) – Sets the color of label, optional.
            * **kwargs** (*Any*) – Additional arguments to be passed to [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix").

        Returns:
        :   The label.

        Return type:
        :   [`Matrix`](manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix "manim.mobject.matrix.Matrix")

        Examples

        Example: VectorCoordinateLabel [¶](#vectorcoordinatelabel)

        ![../_images/VectorCoordinateLabel-1.png](../_images/VectorCoordinateLabel-1.png)

        ```
        from manim import *

        class VectorCoordinateLabel(Scene):
            def construct(self):
                plane = NumberPlane()

                vec_1 = Vector([1, 2])
                vec_2 = Vector([-3, -2])
                label_1 = vec_1.coordinate_label()
                label_2 = vec_2.coordinate_label(color=YELLOW)

                self.add(plane, vec_1, vec_2, label_1, label_2)

        ```

        ```

        class VectorCoordinateLabel(Scene):
            def construct(self):
                plane = NumberPlane()

                vec_1 = Vector([1, 2])
                vec_2 = Vector([-3, -2])
                label_1 = vec_1.coordinate_label()
                label_2 = vec_2.coordinate_label(color=YELLOW)

                self.add(plane, vec_1, vec_2, label_1, label_2)


        ```