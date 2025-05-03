# Source: https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.Brace.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Brace[¶](#brace "Link to this heading")
=======================================

Qualified name: `manim.mobject.svg.brace.Brace`

*class* Brace(*mobject*, *direction=array([0., -1., 0.])*, *buff=0.2*, *sharpness=2*, *stroke\_width=0*, *fill\_opacity=1.0*, *background\_stroke\_width=0*, *background\_stroke\_color=ManimColor('#000000')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#Brace)[¶](#manim.mobject.svg.brace.Brace "Link to this definition")
:   Bases: [`VMobjectFromSVGPath`](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath")

    Takes a mobject and draws a brace adjacent to it.

    Passing a direction vector determines the direction from which the
    brace is drawn. By default it is drawn from below.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject adjacent to which the brace is placed.
        * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") *|* *None*) – The direction from which the brace faces the mobject.
        * **buff** (*float*)
        * **sharpness** (*float*)
        * **stroke\_width** (*float*)
        * **fill\_opacity** (*float*)
        * **background\_stroke\_width** (*float*)
        * **background\_stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

    See also

    [`BraceBetweenPoints`](manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints "manim.mobject.svg.brace.BraceBetweenPoints")

    Examples

    Example: BraceExample [¶](#braceexample)

    ![../_images/BraceExample-1.png](../_images/BraceExample-1.png)

    ```
    from manim import *

    class BraceExample(Scene):
        def construct(self):
            s = Square()
            self.add(s)
            for i in np.linspace(0.1,1.0,4):
                br = Brace(s, sharpness=i)
                t = Text(f"sharpness= {i}").next_to(br, RIGHT)
                self.add(t)
                self.add(br)
            VGroup(*self.mobjects).arrange(DOWN, buff=0.2)

    ```

    ```

    class BraceExample(Scene):
        def construct(self):
            s = Square()
            self.add(s)
            for i in np.linspace(0.1,1.0,4):
                br = Brace(s, sharpness=i)
                t = Text(f"sharpness= {i}").next_to(br, RIGHT)
                self.add(t)
                self.add(br)
            VGroup(*self.mobjects).arrange(DOWN, buff=0.2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_direction`](#manim.mobject.svg.brace.Brace.get_direction "manim.mobject.svg.brace.Brace.get_direction") | Returns the direction from the center to the brace tip. |
    | [`get_tex`](#manim.mobject.svg.brace.Brace.get_tex "manim.mobject.svg.brace.Brace.get_tex") | Places the tex at the brace tip. |
    | [`get_text`](#manim.mobject.svg.brace.Brace.get_text "manim.mobject.svg.brace.Brace.get_text") | Places the text at the brace tip. |
    | [`get_tip`](#manim.mobject.svg.brace.Brace.get_tip "manim.mobject.svg.brace.Brace.get_tip") | Returns the point at the brace tip. |
    | [`put_at_tip`](#manim.mobject.svg.brace.Brace.put_at_tip "manim.mobject.svg.brace.Brace.put_at_tip") | Puts the given mobject at the brace tip. |

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

    \_original\_\_init\_\_(*mobject*, *direction=array([0., -1., 0.])*, *buff=0.2*, *sharpness=2*, *stroke\_width=0*, *fill\_opacity=1.0*, *background\_stroke\_width=0*, *background\_stroke\_color=ManimColor('#000000')*, *\*\*kwargs*)[¶](#manim.mobject.svg.brace.Brace._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **direction** ([*Vector3D*](manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D") *|* *None*)
            * **buff** (*float*)
            * **sharpness** (*float*)
            * **stroke\_width** (*float*)
            * **fill\_opacity** (*float*)
            * **background\_stroke\_width** (*float*)
            * **background\_stroke\_color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

    get\_direction()[[source]](../_modules/manim/mobject/svg/brace.html#Brace.get_direction)[¶](#manim.mobject.svg.brace.Brace.get_direction "Link to this definition")
    :   Returns the direction from the center to the brace tip.

    get\_tex(*\*tex*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#Brace.get_tex)[¶](#manim.mobject.svg.brace.Brace.get_tex "Link to this definition")
    :   Places the tex at the brace tip.

        Parameters:
        :   * **tex** – The tex to be placed at the brace tip.
            * **kwargs** – Any further keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip "manim.mobject.svg.brace.Brace.put_at_tip") which
              is used to position the tex at the brace tip.

        Return type:
        :   [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    get\_text(*\*text*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#Brace.get_text)[¶](#manim.mobject.svg.brace.Brace.get_text "Link to this definition")
    :   Places the text at the brace tip.

        Parameters:
        :   * **text** – The text to be placed at the brace tip.
            * **kwargs** – Any additional keyword arguments are passed to [`put_at_tip()`](#manim.mobject.svg.brace.Brace.put_at_tip "manim.mobject.svg.brace.Brace.put_at_tip") which
              is used to position the text at the brace tip.

        Return type:
        :   [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

    get\_tip()[[source]](../_modules/manim/mobject/svg/brace.html#Brace.get_tip)[¶](#manim.mobject.svg.brace.Brace.get_tip "Link to this definition")
    :   Returns the point at the brace tip.

    put\_at\_tip(*mob*, *use\_next\_to=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#Brace.put_at_tip)[¶](#manim.mobject.svg.brace.Brace.put_at_tip "Link to this definition")
    :   Puts the given mobject at the brace tip.

        Parameters:
        :   * **mob** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be placed at the tip.
            * **use\_next\_to** (*bool*) – If true, then `next_to()` is used to place the mobject at the
              tip.
            * **kwargs** – Any additional keyword arguments are passed to `next_to()` which
              is used to put the mobject next to the brace tip.