# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Exclusion.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Exclusion[¶](#exclusion "Link to this heading")
===============================================

Qualified name: `manim.mobject.geometry.boolean\_ops.Exclusion`

*class* Exclusion(*subject*, *clip*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/boolean_ops.html#Exclusion)[¶](#manim.mobject.geometry.boolean_ops.Exclusion "Link to this definition")
:   Bases: `_BooleanOps`

    Find the XOR between two [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").
    This creates a new [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") consisting of the region
    covered by exactly one of them.

    Parameters:
    :   * **subject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 1st [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").
        * **clip** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The 2nd [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")
        * **kwargs** (*Any*)

    Example

    Example: IntersectionExample [¶](#intersectionexample)

    ![../_images/IntersectionExample-1.png](../_images/IntersectionExample-1.png)

    ```
    from manim import *

    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0.4, 0])
            self.add(sq, cr, un)

    ```

    ```

    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Exclusion(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0.4, 0])
            self.add(sq, cr, un)


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

    \_original\_\_init\_\_(*subject*, *clip*, *\*\*kwargs*)[¶](#manim.mobject.geometry.boolean_ops.Exclusion._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **subject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **clip** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **kwargs** (*Any*)

        Return type:
        :   None