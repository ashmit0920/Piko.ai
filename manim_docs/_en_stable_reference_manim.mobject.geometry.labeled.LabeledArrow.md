# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.labeled.LabeledArrow.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

LabeledArrow[¶](#labeledarrow "Link to this heading")
=====================================================

Qualified name: `manim.mobject.geometry.labeled.LabeledArrow`

*class* LabeledArrow(*\*args*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/labeled.html#LabeledArrow)[¶](#manim.mobject.geometry.labeled.LabeledArrow "Link to this definition")
:   Bases: [`LabeledLine`](manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine"), [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")

    Constructs an arrow containing a label box somewhere along its length.
    This class inherits its label properties from LabeledLine, so the main parameters controlling it are the same.

    Parameters:
    :   * **label** – Label that will be displayed on the Arrow.
        * **label\_position** – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
        * **label\_config** – A dictionary containing the configuration for the label.
          This is only applied if `label` is of type `str`.
        * **box\_config** – A dictionary containing the configuration for the background box.
        * **frame\_config** –

          A dictionary containing the configuration for the frame.

          See also

          [`LabeledLine`](manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine "manim.mobject.geometry.labeled.LabeledLine")
        * **args** (*Any*)
        * **kwargs** (*Any*)

    Examples

    Example: LabeledArrowExample [¶](#labeledarrowexample)

    ![../_images/LabeledArrowExample-1.png](../_images/LabeledArrowExample-1.png)

    ```
    from manim import *

    class LabeledArrowExample(Scene):
        def construct(self):
            l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

            self.add(l_arrow)

    ```

    ```

    class LabeledArrowExample(Scene):
        def construct(self):
            l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)

            self.add(l_arrow)


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

    \_original\_\_init\_\_(*\*args*, *\*\*kwargs*)[¶](#manim.mobject.geometry.labeled.LabeledArrow._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **args** (*Any*)
            * **kwargs** (*Any*)

        Return type:
        :   None