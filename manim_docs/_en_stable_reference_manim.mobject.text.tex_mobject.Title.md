# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.Title.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Title[¶](#title "Link to this heading")
=======================================

Qualified name: `manim.mobject.text.tex\_mobject.Title`

*class* Title(*\*text\_parts*, *include\_underline=True*, *match\_underline\_width\_to\_text=False*, *underline\_buff=0.25*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#Title)[¶](#manim.mobject.text.tex_mobject.Title "Link to this definition")
:   Bases: [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

    A mobject representing an underlined title.

    Examples

    Example: TitleExample [¶](#titleexample)

    ![../_images/TitleExample-1.png](../_images/TitleExample-1.png)

    ```
    from manim import *

    import manim

    class TitleExample(Scene):
        def construct(self):
            banner = ManimBanner()
            title = Title(f"Manim version {manim.__version__}")
            self.add(banner, title)

    ```

    ```

    import manim

    class TitleExample(Scene):
        def construct(self):
            banner = ManimBanner()
            title = Title(f"Manim version {manim.__version__}")
            self.add(banner, title)


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

    \_original\_\_init\_\_(*\*text\_parts*, *include\_underline=True*, *match\_underline\_width\_to\_text=False*, *underline\_buff=0.25*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.Title._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.