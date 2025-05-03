# Source: https://docs.manim.community/en/stable/reference/manim.animation.composition.AnimationGroup.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

AnimationGroup[¶](#animationgroup "Link to this heading")
=========================================================

Qualified name: `manim.animation.composition.AnimationGroup`

*class* AnimationGroup(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup)[¶](#manim.animation.composition.AnimationGroup "Link to this definition")
:   Bases: [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

    Plays a group or series of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation").

    Parameters:
    :   * **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") *|* *Iterable**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]* *|* *types.GeneratorType**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*) – Sequence of [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") objects to be played.
        * **group** ([*Group*](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group") *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") *|* *OpenGLGroup* *|* *OpenGLVGroup*) – A group of multiple [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **run\_time** (*float* *|* *None*) – The duration of the animation in seconds.
        * **rate\_func** (*Callable**[**[**float**]**,* *float**]*) – The function defining the animation progress based on the relative
          runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")) .
        * **lag\_ratio** (*float*) –

          Defines the delay after which the animation is applied to submobjects. A lag\_ratio of
          `n.nn` means the next animation will play when `nnn%` of the current animation has played.
          Defaults to 0.0, meaning that all animations will be played together.

          This does not influence the total runtime of the animation. Instead the runtime
          of individual animations is adjusted so that the complete animation has the defined
          run time.

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.composition.AnimationGroup.begin "manim.animation.composition.AnimationGroup.begin") | Begin the animation. |
    | [`build_animations_with_timings`](#manim.animation.composition.AnimationGroup.build_animations_with_timings "manim.animation.composition.AnimationGroup.build_animations_with_timings") | Creates a list of triplets of the form (anim, start\_time, end\_time). |
    | [`clean_up_from_scene`](#manim.animation.composition.AnimationGroup.clean_up_from_scene "manim.animation.composition.AnimationGroup.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | [`finish`](#manim.animation.composition.AnimationGroup.finish "manim.animation.composition.AnimationGroup.finish") | Finish the animation. |
    | [`get_all_mobjects`](#manim.animation.composition.AnimationGroup.get_all_mobjects "manim.animation.composition.AnimationGroup.get_all_mobjects") | Get all mobjects involved in the animation. |
    | [`init_run_time`](#manim.animation.composition.AnimationGroup.init_run_time "manim.animation.composition.AnimationGroup.init_run_time") | Calculates the run time of the animation, if different from `run_time`. |
    | [`interpolate`](#manim.animation.composition.AnimationGroup.interpolate "manim.animation.composition.AnimationGroup.interpolate") | Set the animation progress. |
    | [`update_mobjects`](#manim.animation.composition.AnimationGroup.update_mobjects "manim.animation.composition.AnimationGroup.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*\*animations*, *group=None*, *run\_time=None*, *rate\_func=<function linear>*, *lag\_ratio=0*, *\*\*kwargs*)[¶](#manim.animation.composition.AnimationGroup._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **animations** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") *|* *Iterable**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]* *|* *types.GeneratorType**[*[*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")*]*)
            * **group** ([*Group*](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group") *|* [*VGroup*](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup") *|* *OpenGLGroup* *|* *OpenGLVGroup*)
            * **run\_time** (*float* *|* *None*)
            * **rate\_func** (*Callable**[**[**float**]**,* *float**]*)
            * **lag\_ratio** (*float*)

        Return type:
        :   None

    \_setup\_scene(*scene*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup._setup_scene)[¶](#manim.animation.composition.AnimationGroup._setup_scene "Link to this definition")
    :   Setup up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.

        This includes to [`add()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.

        Parameters:
        :   **scene** – The scene the animation should be cleaned up from.

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/composition.html#AnimationGroup.begin)[¶](#manim.animation.composition.AnimationGroup.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    build\_animations\_with\_timings()[[source]](../_modules/manim/animation/composition.html#AnimationGroup.build_animations_with_timings)[¶](#manim.animation.composition.AnimationGroup.build_animations_with_timings "Link to this definition")
    :   Creates a list of triplets of the form (anim, start\_time, end\_time).

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup.clean_up_from_scene)[¶](#manim.animation.composition.AnimationGroup.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    finish()[[source]](../_modules/manim/animation/composition.html#AnimationGroup.finish)[¶](#manim.animation.composition.AnimationGroup.finish "Link to this definition")
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](../_modules/manim/animation/composition.html#AnimationGroup.get_all_mobjects)[¶](#manim.animation.composition.AnimationGroup.get_all_mobjects "Link to this definition")
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]

    init\_run\_time(*run\_time*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup.init_run_time)[¶](#manim.animation.composition.AnimationGroup.init_run_time "Link to this definition")
    :   Calculates the run time of the animation, if different from `run_time`.

        Parameters:
        :   **run\_time** – The duration of the animation in seconds.

        Returns:
        :   The duration of the animation in seconds.

        Return type:
        :   run\_time

    interpolate(*alpha*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup.interpolate)[¶](#manim.animation.composition.AnimationGroup.interpolate "Link to this definition")
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    update\_mobjects(*dt*)[[source]](../_modules/manim/animation/composition.html#AnimationGroup.update_mobjects)[¶](#manim.animation.composition.AnimationGroup.update_mobjects "Link to this definition")
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None