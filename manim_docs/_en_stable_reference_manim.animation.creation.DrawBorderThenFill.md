# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.DrawBorderThenFill.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DrawBorderThenFill[¶](#drawborderthenfill "Link to this heading")
=================================================================

Qualified name: `manim.animation.creation.DrawBorderThenFill`

*class* DrawBorderThenFill(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill)[¶](#manim.animation.creation.DrawBorderThenFill "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Draw the border first and then show the fill.

    Examples

    Example: ShowDrawBorderThenFill [¶](#showdrawborderthenfill)

    [
    ](./ShowDrawBorderThenFill-1.mp4)

    ```
    from manim import *

    class ShowDrawBorderThenFill(Scene):
        def construct(self):
            self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))

    ```

    ```

    class ShowDrawBorderThenFill(Scene):
        def construct(self):
            self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.creation.DrawBorderThenFill.begin "manim.animation.creation.DrawBorderThenFill.begin") | Begin the animation. |
    | [`get_all_mobjects`](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "manim.animation.creation.DrawBorderThenFill.get_all_mobjects") | Get all mobjects involved in the animation. |
    | `get_outline` |  |
    | `get_stroke_color` |  |
    | `interpolate_submobject` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
        * **run\_time** (*float*)
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        * **stroke\_width** (*float*)
        * **stroke\_color** (*str*)
        * **draw\_border\_animation\_config** (*dict*)
        * **fill\_animation\_config** (*dict*)
        * **introducer** (*bool*)

    \_original\_\_init\_\_(*vmobject*, *run\_time=2*, *rate\_func=<function double\_smooth>*, *stroke\_width=2*, *stroke\_color=None*, *draw\_border\_animation\_config={}*, *fill\_animation\_config={}*, *introducer=True*, *\*\*kwargs*)[¶](#manim.animation.creation.DrawBorderThenFill._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") *|* *OpenGLVMobject*)
            * **run\_time** (*float*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **stroke\_width** (*float*)
            * **stroke\_color** (*str*)
            * **draw\_border\_animation\_config** (*dict*)
            * **fill\_animation\_config** (*dict*)
            * **introducer** (*bool*)

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill.begin)[¶](#manim.animation.creation.DrawBorderThenFill.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](../_modules/manim/animation/creation.html#DrawBorderThenFill.get_all_mobjects)[¶](#manim.animation.creation.DrawBorderThenFill.get_all_mobjects "Link to this definition")
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]