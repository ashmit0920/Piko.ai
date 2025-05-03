# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledLine.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LabeledLine[¶](#labeledline "Link to this heading")
===================================================

Qualified name: `manim.mobject.geometry.labeled.LabeledLine`

*class* LabeledLine(*label*, *label\_position=0.5*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*args*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/labeled.html#LabeledLine)[¶](#manim.mobject.geometry.labeled.LabeledLine "Link to this definition")
:   Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

    Constructs a line containing a label box somewhere along its length.

    Parameters:
    :   * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")) – Label that will be displayed on the line.
        * **label\_position** (*float*) – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
        * **label\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        * **box\_config** (*dict**[**str**,* *Any**]* *|* *None*) – A dictionary containing the configuration for the background box.
        * **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*) –

          A dictionary containing the configuration for the frame.

          See also

          [`LabeledArrow`](manim.mobject.geometry.labeled.LabeledArrow.html#manim.mobject.geometry.labeled.LabeledArrow "manim.mobject.geometry.labeled.LabeledArrow")
        * **args** (*Any*)
        * **kwargs** (*Any*)

    Examples

    Example: LabeledLineExample [¶](#labeledlineexample)

    ![../_images/LabeledLineExample-1.png](../_images/LabeledLineExample-1.png)

    ```
    from manim import *

    class LabeledLineExample(Scene):
        def construct(self):
            line = LabeledLine(
                label          = '0.5',
                label_position = 0.8,
                label_config = {
                    "font_size" : 20
                },
                start=LEFT+DOWN,
                end=RIGHT+UP)

            line.set_length(line.get_length() * 2)
            self.add(line)

    ```

    ```

    class LabeledLineExample(Scene):
        def construct(self):
            line = LabeledLine(
                label          = '0.5',
                label_position = 0.8,
                label_config = {
                    "font_size" : 20
                },
                start=LEFT+DOWN,
                end=RIGHT+UP)

            line.set_length(line.get_length() * 2)
            self.add(line)


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

    \_original\_\_init\_\_(*label*, *label\_position=0.5*, *label\_config=None*, *box\_config=None*, *frame\_config=None*, *\*args*, *\*\*kwargs*)[¶](#manim.mobject.geometry.labeled.LabeledLine._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **label** (*str* *|* [*Tex*](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") *|* [*MathTex*](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") *|* [*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
            * **label\_position** (*float*)
            * **label\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **box\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **frame\_config** (*dict**[**str**,* *Any**]* *|* *None*)
            * **args** (*Any*)
            * **kwargs** (*Any*)

        Return type:
        :   None