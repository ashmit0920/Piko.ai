# Source: https://docs.manim.community/en/stable/reference/manim.animation.creation.ShowIncreasingSubsets.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ShowIncreasingSubsets[¶](#showincreasingsubsets "Link to this heading")
=======================================================================

Qualified name: `manim.animation.creation.ShowIncreasingSubsets`

*class* ShowIncreasingSubsets(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/creation.html#ShowIncreasingSubsets)[¶](#manim.animation.creation.ShowIncreasingSubsets "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Show one submobject at a time, leaving all previous ones displayed on screen.

    Examples

    Example: ShowIncreasingSubsetsScene [¶](#showincreasingsubsetsscene)

    [
    ](./ShowIncreasingSubsetsScene-1.mp4)

    ```
    from manim import *

    class ShowIncreasingSubsetsScene(Scene):
        def construct(self):
            p = VGroup(Dot(), Square(), Triangle())
            self.add(p)
            self.play(ShowIncreasingSubsets(p))
            self.wait()

    ```

    ```

    class ShowIncreasingSubsetsScene(Scene):
        def construct(self):
            p = VGroup(Dot(), Square(), Triangle())
            self.add(p)
            self.play(ShowIncreasingSubsets(p))
            self.wait()


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`interpolate_mobject`](#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject "manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value. |
    | `update_submobject_list` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **group** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **suspend\_mobject\_updating** (*bool*)
        * **int\_func** (*Callable**[**[**np.ndarray**]**,* *np.ndarray**]*)

    \_original\_\_init\_\_(*group*, *suspend\_mobject\_updating=False*, *int\_func=<ufunc 'floor'>*, *reverse\_rate\_function=False*, *\*\*kwargs*)[¶](#manim.animation.creation.ShowIncreasingSubsets._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **group** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **suspend\_mobject\_updating** (*bool*)
            * **int\_func** (*Callable**[**[**ndarray**]**,* *ndarray**]*)

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/creation.html#ShowIncreasingSubsets.interpolate_mobject)[¶](#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the `Animation` based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None