# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

MathTex[¶](#mathtex "Link to this heading")
===========================================

Qualified name: `manim.mobject.text.tex\_mobject.MathTex`

*class* MathTex(*\*tex\_strings*, *arg\_separator=' '*, *substrings\_to\_isolate=None*, *tex\_to\_color\_map=None*, *tex\_environment='align\*'*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex)[¶](#manim.mobject.text.tex_mobject.MathTex "Link to this definition")
:   Bases: [`SingleStringMathTex`](manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex "manim.mobject.text.tex_mobject.SingleStringMathTex")

    A string compiled with LaTeX in math mode.

    Examples

    Example: Formula [¶](#formula)

    ![../_images/Formula-1.png](../_images/Formula-1.png)

    ```
    from manim import *

    class Formula(Scene):
        def construct(self):
            t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
            self.add(t)

    ```

    ```

    class Formula(Scene):
        def construct(self):
            t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
            self.add(t)


    ```

    Tests

    Check that creating a [`MathTex`](#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") works:

    ```
    >>> MathTex('a^2 + b^2 = c^2') 
    MathTex('a^2 + b^2 = c^2')

    ```

    Check that double brace group splitting works correctly:

    ```
    >>> t1 = MathTex('{{ a }} + {{ b }} = {{ c }}') 
    >>> len(t1.submobjects) 
    5
    >>> t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}") 
    >>> len(t2.submobjects) 
    1

    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_part_by_tex` |  |
    | `get_parts_by_tex` |  |
    | `index_of_part` |  |
    | `index_of_part_by_tex` |  |
    | `set_color_by_tex` |  |
    | `set_color_by_tex_to_color_map` |  |
    | [`set_opacity_by_tex`](#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex") | Sets the opacity of the tex specified. |
    | `sort_alphabetically` |  |

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

    Parameters:
    :   * **arg\_separator** (*str*)
        * **substrings\_to\_isolate** (*Iterable**[**str**]* *|* *None*)
        * **tex\_to\_color\_map** (*dict**[**str**,* [*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")*]*)
        * **tex\_environment** (*str*)

    \_break\_up\_by\_substrings()[[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex._break_up_by_substrings)[¶](#manim.mobject.text.tex_mobject.MathTex._break_up_by_substrings "Link to this definition")
    :   Reorganize existing submobjects one layer
        deeper based on the structure of tex\_strings (as a list
        of tex\_strings)

    \_original\_\_init\_\_(*\*tex\_strings*, *arg\_separator=' '*, *substrings\_to\_isolate=None*, *tex\_to\_color\_map=None*, *tex\_environment='align\*'*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.MathTex._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **arg\_separator** (*str*)
            * **substrings\_to\_isolate** (*Iterable**[**str**]* *|* *None*)
            * **tex\_to\_color\_map** (*dict**[**str**,* [*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")*]*)
            * **tex\_environment** (*str*)

    set\_opacity\_by\_tex(*tex*, *opacity=0.5*, *remaining\_opacity=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#MathTex.set_opacity_by_tex)[¶](#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex "Link to this definition")
    :   Sets the opacity of the tex specified. If ‘remaining\_opacity’ is specified,
        then the remaining tex will be set to that opacity.

        Parameters:
        :   * **tex** (*str*) – The tex to set the opacity of.
            * **opacity** (*float*) – Default 0.5. The opacity to set the tex to
            * **remaining\_opacity** (*float*) – Default None. The opacity to set the remaining tex to.
              If None, then the remaining tex will not be changed