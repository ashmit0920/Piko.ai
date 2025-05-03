# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RemoveTextLetterByLetter[¶](#removetextletterbyletter "Link to this heading")
=============================================================================

Qualified name: `manim.animation.creation.RemoveTextLetterByLetter`

*class* RemoveTextLetterByLetter(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#RemoveTextLetterByLetter)[¶](#manim.animation.creation.RemoveTextLetterByLetter "Link to this definition")
:   Bases: [`AddTextLetterByLetter`](manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")

    Remove a [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") letter by letter from the scene.

    Parameters:
    :   * **time\_per\_char** (*float*) – Frequency of appearance of the letters.
        * **tip::** (*..*) – This is currently only possible for class:~.Text and not for class:~.MathTex
        * **text** ([*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
        * **suspend\_mobject\_updating** (*bool*)
        * **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
        * **run\_time** (*float* *|* *None*)

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*text*, *suspend\_mobject\_updating=False*, *int\_func=<ufunc 'ceil'>*, *rate\_func=<function linear>*, *time\_per\_char=0.1*, *run\_time=None*, *reverse\_rate\_function=True*, *introducer=False*, *remover=True*, *\*\*kwargs*)[¶](#manim.animation.creation.RemoveTextLetterByLetter._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **text** ([*Text*](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))
            * **suspend\_mobject\_updating** (*bool*)
            * **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **time\_per\_char** (*float*)
            * **run\_time** (*float* *|* *None*)

        Return type:
        :   None