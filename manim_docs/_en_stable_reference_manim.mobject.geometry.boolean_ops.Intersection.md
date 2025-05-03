# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Intersection.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Intersection[¶](#intersection "Link to this heading")
=====================================================

Qualified name: `manim.mobject.geometry.boolean\_ops.Intersection`

*class* Intersection(*\*vmobjects*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/boolean_ops.html#Intersection)[¶](#manim.mobject.geometry.boolean_ops.Intersection "Link to this definition")
:   Bases: `_BooleanOps`

    Find the intersection of two [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") s.
    This keeps the parts covered by both [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") s.

    Parameters:
    :   * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") to find the intersection.
        * **kwargs** (*Any*)

    Raises:
    :   **ValueError** – If less the 2 [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") are passed.

    Example

    Example: IntersectionExample [¶](#intersectionexample)

    ![../_images/IntersectionExample-2.png](../_images/IntersectionExample-2.png)

    ```
    from manim import *

    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0, 0])
            self.add(sq, cr, un)

    ```

    ```

    class IntersectionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0, 0])
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

    \_original\_\_init\_\_(*\*vmobjects*, *\*\*kwargs*)[¶](#manim.mobject.geometry.boolean_ops.Intersection._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **kwargs** (*Any*)

        Return type:
        :   None