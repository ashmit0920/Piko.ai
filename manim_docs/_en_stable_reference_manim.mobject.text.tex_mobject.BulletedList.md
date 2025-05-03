# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.BulletedList.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

BulletedList[¶](#bulletedlist "Link to this heading")
=====================================================

Qualified name: `manim.mobject.text.tex\_mobject.BulletedList`

*class* BulletedList(*\*items*, *buff=0.5*, *dot\_scale\_factor=2*, *tex\_environment=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/tex_mobject.html#BulletedList)[¶](#manim.mobject.text.tex_mobject.BulletedList "Link to this definition")
:   Bases: [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex")

    A bulleted list.

    Examples

    Example: BulletedListExample [¶](#bulletedlistexample)

    ![../_images/BulletedListExample-1.png](../_images/BulletedListExample-1.png)

    ```
    from manim import *

    class BulletedListExample(Scene):
        def construct(self):
            blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
            blist.set_color_by_tex("Item 1", RED)
            blist.set_color_by_tex("Item 2", GREEN)
            blist.set_color_by_tex("Item 3", BLUE)
            self.add(blist)

    ```

    ```

    class BulletedListExample(Scene):
        def construct(self):
            blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
            blist.set_color_by_tex("Item 1", RED)
            blist.set_color_by_tex("Item 2", GREEN)
            blist.set_color_by_tex("Item 3", BLUE)
            self.add(blist)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `fade_all_but` |  |

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

    \_original\_\_init\_\_(*\*items*, *buff=0.5*, *dot\_scale\_factor=2*, *tex\_environment=None*, *\*\*kwargs*)[¶](#manim.mobject.text.tex_mobject.BulletedList._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.