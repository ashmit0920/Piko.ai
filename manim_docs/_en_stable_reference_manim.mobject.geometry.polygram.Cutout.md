# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Cutout.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Cutout[¶](#cutout "Link to this heading")
=========================================

Qualified name: `manim.mobject.geometry.polygram.Cutout`

*class* Cutout(*main\_shape*, *\*mobjects*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/polygram.html#Cutout)[¶](#manim.mobject.geometry.polygram.Cutout "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A shape with smaller cutouts.

    Parameters:
    :   * **main\_shape** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The primary shape from which cutouts are made.
        * **mobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The smaller shapes which are to be cut out of the `main_shape`.
        * **kwargs** (*Any*) – Further keyword arguments that are passed to the constructor of
          [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Warning

    Technically, this class behaves similar to a symmetric difference: if
    parts of the `mobjects` are not located within the `main_shape`,
    these parts will be added to the resulting [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Examples

    Example: CutoutExample [¶](#cutoutexample)

    [
    ](./CutoutExample-1.mp4)

    ```
    from manim import *

    class CutoutExample(Scene):
        def construct(self):
            s1 = Square().scale(2.5)
            s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
            s3 = Square().shift(UP + RIGHT).scale(0.5)
            s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
            s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
            c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
            self.play(Write(c), run_time=4)
            self.wait()

    ```

    ```

    class CutoutExample(Scene):
        def construct(self):
            s1 = Square().scale(2.5)
            s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
            s3 = Square().shift(UP + RIGHT).scale(0.5)
            s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
            s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
            c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
            self.play(Write(c), run_time=4)
            self.wait()


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

    \_original\_\_init\_\_(*main\_shape*, *\*mobjects*, *\*\*kwargs*)[¶](#manim.mobject.geometry.polygram.Cutout._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **main\_shape** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **mobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **kwargs** (*Any*)

        Return type:
        :   None