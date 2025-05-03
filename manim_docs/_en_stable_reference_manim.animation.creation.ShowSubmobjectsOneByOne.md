# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowSubmobjectsOneByOne.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ShowSubmobjectsOneByOne[¶](#showsubmobjectsonebyone "Link to this heading")
===========================================================================

Qualified name: `manim.animation.creation.ShowSubmobjectsOneByOne`

*class* ShowSubmobjectsOneByOne(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#ShowSubmobjectsOneByOne)[¶](#manim.animation.creation.ShowSubmobjectsOneByOne "Link to this definition")
:   Bases: [`ShowIncreasingSubsets`](manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets "manim.animation.creation.ShowIncreasingSubsets")

    Show one submobject at a time, removing all previously displayed ones from screen.

    Methods

    |  |  |
    | --- | --- |
    | `update_submobject_list` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **group** (*Iterable**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
        * **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)

    \_original\_\_init\_\_(*group*, *int\_func=<ufunc 'ceil'>*, *\*\*kwargs*)[¶](#manim.animation.creation.ShowSubmobjectsOneByOne._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **group** (*Iterable**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*)
            * **int\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*)

        Return type:
        :   None