# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.SingleStringMathTex.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SingleStringMathTex[¶](#singlestringmathtex "Link to this heading")
===================================================================

Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`

*class* SingleStringMathTex(*tex\_string*, *stroke\_width=0*, *should\_center=True*, *height=None*, *organize\_left\_to\_right=False*, *tex\_environment='align\*'*, *tex\_template=None*, *font\_size=48*, *color=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex "Link to this definition")
:   Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

    Elementary building block for rendering text with LaTeX.

    Tests

    Check that creating a [`SingleStringMathTex`](#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex") object works:

    ```
    >>> SingleStringMathTex('Test') 
    SingleStringMathTex('Test')

    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_tex_string` |  |
    | [`init_colors`](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors") | Initializes the colors. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`font_size`](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "manim.mobject.text.tex_mobject.SingleStringMathTex.font_size") | The font size of the tex mobject. |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **tex\_string** (*str*)
        * **stroke\_width** (*float*)
        * **should\_center** (*bool*)
        * **height** (*float* *|* *None*)
        * **organize\_left\_to\_right** (*bool*)
        * **tex\_environment** (*str*)
        * **tex\_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") *|* *None*)
        * **font\_size** (*float*)
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)

    \_original\_\_init\_\_(*tex\_string*, *stroke\_width=0*, *should\_center=True*, *height=None*, *organize\_left\_to\_right=False*, *tex\_environment='align\*'*, *tex\_template=None*, *font\_size=48*, *color=None*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **tex\_string** (*str*)
            * **stroke\_width** (*float*)
            * **should\_center** (*bool*)
            * **height** (*float* *|* *None*)
            * **organize\_left\_to\_right** (*bool*)
            * **tex\_environment** (*str*)
            * **tex\_template** ([*TexTemplate*](manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "manim.utils.tex.TexTemplate") *|* *None*)
            * **font\_size** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)

    \_remove\_stray\_braces(*tex*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex._remove_stray_braces)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex._remove_stray_braces "Link to this definition")
    :   Makes [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") resilient to unmatched braces.

        This is important when the braces in the TeX code are spread over
        multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.

    *property* font\_size[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size "Link to this definition")
    :   The font size of the tex mobject.

    init\_colors(*propagate\_colors=True*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex.init_colors)[¶](#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors "Link to this definition")
    :   Initializes the colors.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.