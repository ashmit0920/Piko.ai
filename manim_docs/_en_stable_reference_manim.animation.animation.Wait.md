# Source: https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Wait[¶](#wait "Link to this heading")
=====================================

Qualified name: `manim.animation.animation.Wait`

*class* Wait(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/animation.html#Wait)[¶](#manim.animation.animation.Wait "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    A “no operation” animation.

    Parameters:
    :   * **run\_time** (*float*) – The amount of time that should pass.
        * **stop\_condition** (*Callable**[**[**]**,* *bool**]* *|* *None*) – A function without positional arguments that evaluates to a boolean.
          The function is evaluated after every new frame has been rendered.
          Playing the animation stops after the return value is truthy, or
          after the specified `run_time` has passed.
        * **frozen\_frame** (*bool* *|* *None*) – Controls whether or not the wait animation is static, i.e., corresponds
          to a frozen frame. If `False` is passed, the render loop still
          progresses through the animation as usual and (among other things)
          continues to call updater functions. If `None` (the default value),
          the [`Scene.play()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") call tries to determine whether the Wait call
          can be static or not itself via `Scene.should_mobjects_update()`.
        * **kwargs** – Keyword arguments to be passed to the parent class, [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.animation.Wait.begin "manim.animation.animation.Wait.begin") | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.animation.Wait.clean_up_from_scene "manim.animation.animation.Wait.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | [`finish`](#manim.animation.animation.Wait.finish "manim.animation.animation.Wait.finish") | Finish the animation. |
    | [`interpolate`](#manim.animation.animation.Wait.interpolate "manim.animation.animation.Wait.interpolate") | Set the animation progress. |
    | [`update_mobjects`](#manim.animation.animation.Wait.update_mobjects "manim.animation.animation.Wait.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*run\_time=1*, *stop\_condition=None*, *frozen\_frame=None*, *rate\_func=<function linear>*, *\*\*kwargs*)[¶](#manim.animation.animation.Wait._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **run\_time** (*float*)
            * **stop\_condition** (*Callable**[**[**]**,* *bool**]* *|* *None*)
            * **frozen\_frame** (*bool* *|* *None*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)

    begin()[[source]](../_modules/manim/animation/animation.html#Wait.begin)[¶](#manim.animation.animation.Wait.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/animation.html#Wait.clean_up_from_scene)[¶](#manim.animation.animation.Wait.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    finish()[[source]](../_modules/manim/animation/animation.html#Wait.finish)[¶](#manim.animation.animation.Wait.finish "Link to this definition")
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    interpolate(*alpha*)[[source]](../_modules/manim/animation/animation.html#Wait.interpolate)[¶](#manim.animation.animation.Wait.interpolate "Link to this definition")
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    update\_mobjects(*dt*)[[source]](../_modules/manim/animation/animation.html#Wait.update_mobjects)[¶](#manim.animation.animation.Wait.update_mobjects "Link to this definition")
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None