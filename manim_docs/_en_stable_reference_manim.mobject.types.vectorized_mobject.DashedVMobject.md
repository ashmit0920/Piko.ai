# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.DashedVMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DashedVMobject[¶](#dashedvmobject "Link to this heading")
=========================================================

Qualified name: `manim.mobject.types.vectorized\_mobject.DashedVMobject`

*class* DashedVMobject(*vmobject*, *num\_dashes=15*, *dashed\_ratio=0.5*, *dash\_offset=0*, *color=ManimColor('#FFFFFF')*, *equal\_lengths=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/vectorized_mobject.html#DashedVMobject)[¶](#manim.mobject.types.vectorized_mobject.DashedVMobject "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") composed of dashes instead of lines.

    Parameters:
    :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The object that will get dashed
        * **num\_dashes** (*int*) – Number of dashes to add.
        * **dashed\_ratio** (*float*) – Ratio of dash to empty space.
        * **dash\_offset** (*float*) – Shifts the starting point of dashes along the
          path. Value 1 shifts by one full dash length.
        * **equal\_lengths** (*bool*) – If `True`, dashes will be (approximately) equally long.
          If `False`, dashes will be split evenly in the curve’s
          input t variable (legacy behavior).
        * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

    Examples

    Example: DashedVMobjectExample [¶](#dashedvmobjectexample)

    ![../_images/DashedVMobjectExample-1.png](../_images/DashedVMobjectExample-1.png)

    ```
    from manim import *

    class DashedVMobjectExample(Scene):
        def construct(self):
            r = 0.5

            top_row = VGroup()  # Increasing num_dashes
            for dashes in range(1, 12):
                circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
                top_row.add(circ)

            middle_row = VGroup()  # Increasing dashed_ratio
            for ratio in np.arange(1 / 11, 1, 1 / 11):
                circ = DashedVMobject(
                    Circle(radius=r, color=WHITE), dashed_ratio=ratio
                )
                middle_row.add(circ)

            func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
            func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
            func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
            bottom_row = VGroup(func_even,func_stretched)

            top_row.arrange(buff=0.3)
            middle_row.arrange()
            bottom_row.arrange(buff=1)
            everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
            self.add(everything)

    ```

    ```

    class DashedVMobjectExample(Scene):
        def construct(self):
            r = 0.5

            top_row = VGroup()  # Increasing num_dashes
            for dashes in range(1, 12):
                circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
                top_row.add(circ)

            middle_row = VGroup()  # Increasing dashed_ratio
            for ratio in np.arange(1 / 11, 1, 1 / 11):
                circ = DashedVMobject(
                    Circle(radius=r, color=WHITE), dashed_ratio=ratio
                )
                middle_row.add(circ)

            func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
            func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
            func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
            bottom_row = VGroup(func_even,func_stretched)

            top_row.arrange(buff=0.3)
            middle_row.arrange()
            bottom_row.arrange(buff=1)
            everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
            self.add(everything)


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

    \_original\_\_init\_\_(*vmobject*, *num\_dashes=15*, *dashed\_ratio=0.5*, *dash\_offset=0*, *color=ManimColor('#FFFFFF')*, *equal\_lengths=True*, *\*\*kwargs*)[¶](#manim.mobject.types.vectorized_mobject.DashedVMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))
            * **num\_dashes** (*int*)
            * **dashed\_ratio** (*float*)
            * **dash\_offset** (*float*)
            * **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))
            * **equal\_lengths** (*bool*)

        Return type:
        :   None