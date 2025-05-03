# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Tex.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Tex[¶](#tex "Link to this heading")
===================================

Qualified name: `manim.mobject.text.tex\_mobject.Tex`

*class* Tex(*\*tex\_strings*, *arg\_separator=''*, *tex\_environment='center'*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#Tex)[¶](#manim.mobject.text.tex_mobject.Tex "Link to this definition")
:   Bases: [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex")

    A string compiled with LaTeX in normal mode.

    The color can be set using
    the `color` argument. Any parts of the `tex_string` that are colored by the
    TeX commands `\color` or `\textcolor` will retain their original color.

    Tests

    Check whether writing a LaTeX string works:

    ```
    >>> Tex('The horse does not eat cucumber salad.') 
    Tex('The horse does not eat cucumber salad.')

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
    | `font_size` | The font size of the tex mobject. |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*\*tex\_strings*, *arg\_separator=''*, *tex\_environment='center'*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.Tex._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.