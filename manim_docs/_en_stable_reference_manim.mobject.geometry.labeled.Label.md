# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.Label.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Label[¶](#label "Link to this heading")
=======================================

Qualified name: `manim.mobject.geometry.labeled.Label`

*class* Label(*label*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/labeled.html#Label)[¶](#manim.mobject.geometry.labeled.Label "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    A Label consisting of text surrounded by a frame.

    Parameters:
    :   * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed.
        * **label\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        * **box\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the background box.
        * **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the frame.
        * **kwargs** (*Any*)

    Examples

    Example: LabelExample [¶](#labelexample)

    ![../_images/LabelExample-1.png](../_images/LabelExample-1.png)

    ```
    from manim import *

    class LabelExample(Scene):
        def construct(self):
            label = Label(
                label=Text('Label Text', font='sans-serif'),
                box_config = {
                    "color" : BLUE,
                    "fill_opacity" : 0.75
                }
            )
            label.scale(3)
            self.add(label)

    ```

    ```

    class LabelExample(Scene):
        def construct(self):
            label = Label(
                label=Text('Label Text', font='sans-serif'),
                box_config = {
                    "color" : BLUE,
                    "fill_opacity" : 0.75
                }
            )
            label.scale(3)
            self.add(label)


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

    \_original\_\_init\_\_(*label*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*\*kwargs*)[¶](#manim.mobject.geometry.labeled.Label._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
            * **label\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **box\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **kwargs** (*Any*)

        Return type:
        :   None