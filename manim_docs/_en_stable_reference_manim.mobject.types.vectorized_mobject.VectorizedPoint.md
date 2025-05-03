# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VectorizedPoint.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

VectorizedPoint[¶](#vectorizedpoint "Link to this heading")
===========================================================

Qualified name: `manim.mobject.types.vectorized\_mobject.VectorizedPoint`

*class* VectorizedPoint(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *fill\_opacity=0*, *stroke\_width=0*, *artificial\_width=0.01*, *artificial\_height=0.01*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/vectorized_mobject.html#VectorizedPoint)[¶](#manim.mobject.types.vectorized_mobject.VectorizedPoint "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    Methods

    |  |  |
    | --- | --- |
    | `get_location` |  |
    | `set_location` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`height`](#manim.mobject.types.vectorized_mobject.VectorizedPoint.height "manim.mobject.types.vectorized_mobject.VectorizedPoint.height") | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | [`width`](#manim.mobject.types.vectorized_mobject.VectorizedPoint.width "manim.mobject.types.vectorized_mobject.VectorizedPoint.width") | The width of the mobject. |

    Parameters:
    :   * **location** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
        * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
        * **fill\_opacity** (*float*)
        * **stroke\_width** (*float*)
        * **artificial\_width** (*float*)
        * **artificial\_height** (*float*)

    \_original\_\_init\_\_(*location=array([0., 0., 0.])*, *color=ManimColor('#000000')*, *fill\_opacity=0*, *stroke\_width=0*, *artificial\_width=0.01*, *artificial\_height=0.01*, *\*\*kwargs*)[¶](#manim.mobject.types.vectorized_mobject.VectorizedPoint._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **location** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))
            * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
            * **fill\_opacity** (*float*)
            * **stroke\_width** (*float*)
            * **artificial\_width** (*float*)
            * **artificial\_height** (*float*)

        Return type:
        :   None

    basecls[¶](#manim.mobject.types.vectorized_mobject.VectorizedPoint.basecls "Link to this definition")
    :   alias of [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    *property* height*: float*[¶](#manim.mobject.types.vectorized_mobject.VectorizedPoint.height "Link to this definition")
    :   The height of the mobject.

        Return type:
        :   `float`

        Examples

        Example: HeightExample [¶](#heightexample)

        [
        ](./HeightExample-2.mp4)

        ```
        from manim import *

        class HeightExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.height))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(height=5))
                self.wait()

        ```

        ```

        class HeightExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.height))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(height=5))
                self.wait()


        ```

        See also

        `length_over_dim()`

    *property* width*: float*[¶](#manim.mobject.types.vectorized_mobject.VectorizedPoint.width "Link to this definition")
    :   The width of the mobject.

        Return type:
        :   `float`

        Examples

        Example: WidthExample [¶](#widthexample)

        [
        ](./WidthExample-2.mp4)

        ```
        from manim import *

        class WidthExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.width))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(width=7))
                self.wait()

        ```

        ```

        class WidthExample(Scene):
            def construct(self):
                decimal = DecimalNumber().to_edge(UP)
                rect = Rectangle(color=BLUE)
                rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

                decimal.add_updater(lambda d: d.set_value(rect.width))

                self.add(rect_copy, rect, decimal)
                self.play(rect.animate.set(width=7))
                self.wait()


        ```

        See also

        `length_over_dim()`