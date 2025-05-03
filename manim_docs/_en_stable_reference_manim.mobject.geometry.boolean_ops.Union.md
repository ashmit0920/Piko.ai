# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Union[¶](#union "Link to this heading")
=======================================

Qualified name: `manim.mobject.geometry.boolean\_ops.Union`

*class* Union(*\*vmobjects*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/boolean_ops.html#Union)[¶](#manim.mobject.geometry.boolean_ops.Union "Link to this definition")
:   Bases: `_BooleanOps`

    Union of two or more [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") s. This returns the common region of
    the `VMobject` s.

    Parameters:
    :   * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") s to find the union of.
        * **kwargs** (*Any*)

    Raises:
    :   **ValueError** – If less than 2 [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") s are passed.

    Example

    Example: UnionExample [¶](#unionexample)

    ![../_images/UnionExample-1.png](../_images/UnionExample-1.png)

    ```
    from manim import *

    class UnionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Union(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0.3, 0])
            self.add(sq, cr, un)

    ```

    ```

    class UnionExample(Scene):
        def construct(self):
            sq = Square(color=RED, fill_opacity=1)
            sq.move_to([-2, 0, 0])
            cr = Circle(color=BLUE, fill_opacity=1)
            cr.move_to([-1.3, 0.7, 0])
            un = Union(sq, cr, color=GREEN, fill_opacity=1)
            un.move_to([1.5, 0.3, 0])
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

    \_original\_\_init\_\_(*\*vmobjects*, *\*\*kwargs*)[¶](#manim.mobject.geometry.boolean_ops.Union._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobjects** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **kwargs** (*Any*)

        Return type:
        :   None