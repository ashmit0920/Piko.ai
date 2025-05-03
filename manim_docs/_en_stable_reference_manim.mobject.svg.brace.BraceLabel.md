# Source: https://docs.manim.community/en/stable/reference/manim.mobject.svg.brace.BraceLabel.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

BraceLabel[¶](#bracelabel "Link to this heading")
=================================================

Qualified name: `manim.mobject.svg.brace.BraceLabel`

*class* BraceLabel(*obj*, *text*, *brace\_direction=array([ 0.*, *-1.*, *0.])*, *label\_constructor=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *font\_size=48*, *buff=0.2*, *brace\_config=None*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/brace.html#BraceLabel)[¶](#manim.mobject.svg.brace.BraceLabel "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    Create a brace with a label attached.

    Parameters:
    :   * **obj** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject adjacent to which the brace is placed.
        * **text** (*str*) – The label text.
        * **brace\_direction** (*np.ndarray*) – The direction of the brace. By default `DOWN`.
        * **label\_constructor** (*type*) – A class or function used to construct a mobject representing
          the label. By default [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex").
        * **font\_size** (*float*) – The font size of the label, passed to the `label_constructor`.
        * **buff** (*float*) – The buffer between the mobject and the brace.
        * **brace\_config** (*dict* *|* *None*) – Arguments to be passed to [`Brace`](manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace "manim.mobject.svg.brace.Brace").
        * **kwargs** – Additional arguments to be passed to [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject").

    Methods

    |  |  |
    | --- | --- |
    | `change_brace_label` |  |
    | `change_label` |  |
    | `creation_anim` |  |
    | `shift_brace` |  |

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

    \_original\_\_init\_\_(*obj*, *text*, *brace\_direction=array([ 0.*, *-1.*, *0.])*, *label\_constructor=<class 'manim.mobject.text.tex\_mobject.MathTex'>*, *font\_size=48*, *buff=0.2*, *brace\_config=None*, *\*\*kwargs*)[¶](#manim.mobject.svg.brace.BraceLabel._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **obj** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **text** (*str*)
            * **brace\_direction** (*ndarray*)
            * **label\_constructor** (*type*)
            * **font\_size** (*float*)
            * **buff** (*float*)
            * **brace\_config** (*dict* *|* *None*)