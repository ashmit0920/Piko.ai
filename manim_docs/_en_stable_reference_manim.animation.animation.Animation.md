# Source: https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Animation[¶](#animation "Link to this heading")
===============================================

Qualified name: `manim.animation.animation.Animation`

*class* Animation(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/animation.html#Animation)[¶](#manim.animation.animation.Animation "Link to this definition")
:   Bases: `object`

    An animation.

    Animations have a fixed time span.

    Parameters:
    :   * **mobject** – The mobject to be animated. This is not required for all types of animations.
        * **lag\_ratio** –

          Defines the delay after which the animation is applied to submobjects. This lag
          is relative to the duration of the animation.

          This does not influence the total
          runtime of the animation. Instead the runtime of individual animations is
          adjusted so that the complete animation has the defined run time.
        * **run\_time** – The duration of the animation in seconds.
        * **rate\_func** –

          The function defining the animation progress based on the relative runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")) .

          For example `rate_func(0.5)` is the proportion of the animation that is done
          after half of the animations run time.

    Return type:
    :   Self

    reverse\_rate\_function
    :   Reverses the rate function of the animation. Setting `reverse_rate_function`
        does not have any effect on `remover` or `introducer`. These need to be
        set explicitly if an introducer-animation should be turned into a remover one
        and vice versa.

    name
    :   The name of the animation. This gets displayed while rendering the animation.
        Defaults to <class-name>(<Mobject-name>).

    remover
    :   Whether the given mobject should be removed from the scene after this animation.

    suspend\_mobject\_updating
    :   Whether updaters of the mobject should be suspended during the animation.

    Note

    In the current implementation of this class, the specified rate function is applied
    within [`Animation.interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") call as part of the call to
    `Animation.interpolate_submobject()`. For subclasses of [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation")
    that are implemented by overriding [`interpolate_mobject()`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject"), the rate function
    has to be applied manually (e.g., by passing `self.rate_func(alpha)` instead
    of just `alpha`).

    Examples

    Example: LagRatios [¶](#lagratios)

    [
    ](./LagRatios-1.mp4)

    ```
    from manim import *

    class LagRatios(Scene):
        def construct(self):
            ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

            # Create dot groups
            group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
            groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
            self.add(groups)

            # Label groups
            self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
            for group, ratio in zip(groups, ratios):
                self.add(Text(str(ratio), font_size=36).next_to(group, UP))

            #Animate groups with different lag_ratios
            self.play(AnimationGroup(*[
                group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
                for group, ratio in zip(groups, ratios)
            ]))

            # lag_ratio also works recursively on nested submobjects:
            self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))

    ```

    ```

    class LagRatios(Scene):
        def construct(self):
            ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

            # Create dot groups
            group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
            groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
            self.add(groups)

            # Label groups
            self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
            for group, ratio in zip(groups, ratios):
                self.add(Text(str(ratio), font_size=36).next_to(group, UP))

            #Animate groups with different lag_ratios
            self.play(AnimationGroup(*[
                group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
                for group, ratio in zip(groups, ratios)
            ]))

            # lag_ratio also works recursively on nested submobjects:
            self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`begin`](#manim.animation.animation.Animation.begin "manim.animation.animation.Animation.begin") | Begin the animation. |
    | [`clean_up_from_scene`](#manim.animation.animation.Animation.clean_up_from_scene "manim.animation.animation.Animation.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | [`copy`](#manim.animation.animation.Animation.copy "manim.animation.animation.Animation.copy") | Create a copy of the animation. |
    | `create_starting_mobject` |  |
    | [`finish`](#manim.animation.animation.Animation.finish "manim.animation.animation.Animation.finish") | Finish the animation. |
    | `get_all_families_zipped` |  |
    | [`get_all_mobjects`](#manim.animation.animation.Animation.get_all_mobjects "manim.animation.animation.Animation.get_all_mobjects") | Get all mobjects involved in the animation. |
    | [`get_all_mobjects_to_update`](#manim.animation.animation.Animation.get_all_mobjects_to_update "manim.animation.animation.Animation.get_all_mobjects_to_update") | Get all mobjects to be updated during the animation. |
    | [`get_rate_func`](#manim.animation.animation.Animation.get_rate_func "manim.animation.animation.Animation.get_rate_func") | Get the rate function of the animation. |
    | [`get_run_time`](#manim.animation.animation.Animation.get_run_time "manim.animation.animation.Animation.get_run_time") | Get the run time of the animation. |
    | [`get_sub_alpha`](#manim.animation.animation.Animation.get_sub_alpha "manim.animation.animation.Animation.get_sub_alpha") | Get the animation progress of any submobjects subanimation. |
    | [`interpolate`](#manim.animation.animation.Animation.interpolate "manim.animation.animation.Animation.interpolate") | Set the animation progress. |
    | [`interpolate_mobject`](#manim.animation.animation.Animation.interpolate_mobject "manim.animation.animation.Animation.interpolate_mobject") | Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation") based on alpha value. |
    | `interpolate_submobject` |  |
    | [`is_introducer`](#manim.animation.animation.Animation.is_introducer "manim.animation.animation.Animation.is_introducer") | Test if the animation is an introducer. |
    | [`is_remover`](#manim.animation.animation.Animation.is_remover "manim.animation.animation.Animation.is_remover") | Test if the animation is a remover. |
    | [`set_default`](#manim.animation.animation.Animation.set_default "manim.animation.animation.Animation.set_default") | Sets the default values of keyword arguments. |
    | [`set_name`](#manim.animation.animation.Animation.set_name "manim.animation.animation.Animation.set_name") | Set the name of the animation. |
    | [`set_rate_func`](#manim.animation.animation.Animation.set_rate_func "manim.animation.animation.Animation.set_rate_func") | Set the rate function of the animation. |
    | [`set_run_time`](#manim.animation.animation.Animation.set_run_time "manim.animation.animation.Animation.set_run_time") | Set the run time of the animation. |
    | [`update_mobjects`](#manim.animation.animation.Animation.update_mobjects "manim.animation.animation.Animation.update_mobjects") | Updates things like starting\_mobject, and (for Transforms) target\_mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_setup\_scene(*scene*)[[source]](../_modules/manim/animation/animation.html#Animation._setup_scene)[¶](#manim.animation.animation.Animation._setup_scene "Link to this definition")
    :   Setup up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") before starting the animation.

        This includes to [`add()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.add "manim.scene.scene.Scene.add") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is an introducer.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    begin()[[source]](../_modules/manim/animation/animation.html#Animation.begin)[¶](#manim.animation.animation.Animation.begin "Link to this definition")
    :   Begin the animation.

        This method is called right as an animation is being played. As much
        initialization as possible, especially any mobject copying, should live in this
        method.

        Return type:
        :   None

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/animation.html#Animation.clean_up_from_scene)[¶](#manim.animation.animation.Animation.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None

    copy()[[source]](../_modules/manim/animation/animation.html#Animation.copy)[¶](#manim.animation.animation.Animation.copy "Link to this definition")
    :   Create a copy of the animation.

        Returns:
        :   A copy of `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")

    finish()[[source]](../_modules/manim/animation/animation.html#Animation.finish)[¶](#manim.animation.animation.Animation.finish "Link to this definition")
    :   Finish the animation.

        This method gets called when the animation is over.

        Return type:
        :   None

    get\_all\_mobjects()[[source]](../_modules/manim/animation/animation.html#Animation.get_all_mobjects)[¶](#manim.animation.animation.Animation.get_all_mobjects "Link to this definition")
    :   Get all mobjects involved in the animation.

        Ordering must match the ordering of arguments to interpolate\_submobject

        Returns:
        :   The sequence of mobjects.

        Return type:
        :   Sequence[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]

    get\_all\_mobjects\_to\_update()[[source]](../_modules/manim/animation/animation.html#Animation.get_all_mobjects_to_update)[¶](#manim.animation.animation.Animation.get_all_mobjects_to_update "Link to this definition")
    :   Get all mobjects to be updated during the animation.

        Returns:
        :   The list of mobjects to be updated during the animation.

        Return type:
        :   List[[Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")]

    get\_rate\_func()[[source]](../_modules/manim/animation/animation.html#Animation.get_rate_func)[¶](#manim.animation.animation.Animation.get_rate_func "Link to this definition")
    :   Get the rate function of the animation.

        Returns:
        :   The rate function of the animation.

        Return type:
        :   Callable[[float], float]

    get\_run\_time()[[source]](../_modules/manim/animation/animation.html#Animation.get_run_time)[¶](#manim.animation.animation.Animation.get_run_time "Link to this definition")
    :   Get the run time of the animation.

        Returns:
        :   The time the animation takes in seconds.

        Return type:
        :   float

    get\_sub\_alpha(*alpha*, *index*, *num\_submobjects*)[[source]](../_modules/manim/animation/animation.html#Animation.get_sub_alpha)[¶](#manim.animation.animation.Animation.get_sub_alpha "Link to this definition")
    :   Get the animation progress of any submobjects subanimation.

        Parameters:
        :   * **alpha** (*float*) – The overall animation progress
            * **index** (*int*) – The index of the subanimation.
            * **num\_submobjects** (*int*) – The total count of subanimations.

        Returns:
        :   The progress of the subanimation.

        Return type:
        :   float

    interpolate(*alpha*)[[source]](../_modules/manim/animation/animation.html#Animation.interpolate)[¶](#manim.animation.animation.Animation.interpolate "Link to this definition")
    :   Set the animation progress.

        This method gets called for every frame during an animation.

        Parameters:
        :   **alpha** (*float*) – The relative time to set the animation to, 0 meaning the start, 1 meaning
            the end.

        Return type:
        :   None

    interpolate\_mobject(*alpha*)[[source]](../_modules/manim/animation/animation.html#Animation.interpolate_mobject)[¶](#manim.animation.animation.Animation.interpolate_mobject "Link to this definition")
    :   Interpolates the mobject of the [`Animation`](#manim.animation.animation.Animation "manim.animation.animation.Animation") based on alpha value.

        Parameters:
        :   **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
            is completed. For example, alpha-values of 0, 0.5, and 1 correspond
            to the animation being completed 0%, 50%, and 100%, respectively.

        Return type:
        :   None

    is\_introducer()[[source]](../_modules/manim/animation/animation.html#Animation.is_introducer)[¶](#manim.animation.animation.Animation.is_introducer "Link to this definition")
    :   Test if the animation is an introducer.

        Returns:
        :   `True` if the animation is an introducer, `False` otherwise.

        Return type:
        :   bool

    is\_remover()[[source]](../_modules/manim/animation/animation.html#Animation.is_remover)[¶](#manim.animation.animation.Animation.is_remover "Link to this definition")
    :   Test if the animation is a remover.

        Returns:
        :   `True` if the animation is a remover, `False` otherwise.

        Return type:
        :   bool

    *classmethod* set\_default(*\*\*kwargs*)[[source]](../_modules/manim/animation/animation.html#Animation.set_default)[¶](#manim.animation.animation.Animation.set_default "Link to this definition")
    :   Sets the default values of keyword arguments.

        If this method is called without any additional keyword
        arguments, the original default values of the initialization
        method of this class are restored.

        Parameters:
        :   **kwargs** – Passing any keyword argument will update the default
            values of the keyword arguments of the initialization
            function of this class.

        Return type:
        :   None

        Examples

        Example: ChangeDefaultAnimation [¶](#changedefaultanimation)

        [
        ](./ChangeDefaultAnimation-1.mp4)

        ```
        from manim import *

        class ChangeDefaultAnimation(Scene):
            def construct(self):
                Rotate.set_default(run_time=2, rate_func=rate_functions.linear)
                Indicate.set_default(color=None)

                S = Square(color=BLUE, fill_color=BLUE, fill_opacity=0.25)
                self.add(S)
                self.play(Rotate(S, PI))
                self.play(Indicate(S))

                Rotate.set_default()
                Indicate.set_default()

        ```

        ```

        class ChangeDefaultAnimation(Scene):
            def construct(self):
                Rotate.set_default(run_time=2, rate_func=rate_functions.linear)
                Indicate.set_default(color=None)

                S = Square(color=BLUE, fill_color=BLUE, fill_opacity=0.25)
                self.add(S)
                self.play(Rotate(S, PI))
                self.play(Indicate(S))

                Rotate.set_default()
                Indicate.set_default()


        ```

    set\_name(*name*)[[source]](../_modules/manim/animation/animation.html#Animation.set_name)[¶](#manim.animation.animation.Animation.set_name "Link to this definition")
    :   Set the name of the animation.

        Parameters:
        :   **name** (*str*) – The new name of the animation.

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")

    set\_rate\_func(*rate\_func*)[[source]](../_modules/manim/animation/animation.html#Animation.set_rate_func)[¶](#manim.animation.animation.Animation.set_rate_func "Link to this definition")
    :   Set the rate function of the animation.

        Parameters:
        :   **rate\_func** (*Callable**[**[**float**]**,* *float**]*) – The new function defining the animation progress based on the
            relative runtime (see [`rate_functions`](manim.utils.rate_functions.html#module-manim.utils.rate_functions "manim.utils.rate_functions")).

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")

    set\_run\_time(*run\_time*)[[source]](../_modules/manim/animation/animation.html#Animation.set_run_time)[¶](#manim.animation.animation.Animation.set_run_time "Link to this definition")
    :   Set the run time of the animation.

        Parameters:
        :   * **run\_time** (*float*) – The new time the animation should take in seconds.
            * **note::** (*..*) – The run\_time of an animation should not be changed while it is already
              running.

        Returns:
        :   `self`

        Return type:
        :   [Animation](#manim.animation.animation.Animation "manim.animation.animation.Animation")

    update\_mobjects(*dt*)[[source]](../_modules/manim/animation/animation.html#Animation.update_mobjects)[¶](#manim.animation.animation.Animation.update_mobjects "Link to this definition")
    :   Updates things like starting\_mobject, and (for
        Transforms) target\_mobject. Note, since typically
        (always?) self.mobject will have its updating
        suspended during the animation, this will do
        nothing to self.mobject.

        Parameters:
        :   **dt** (*float*)

        Return type:
        :   None