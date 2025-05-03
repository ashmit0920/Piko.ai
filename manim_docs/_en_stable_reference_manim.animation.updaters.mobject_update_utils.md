# Source: https://docs.manim.community/en/stable/reference/manim.animation.updaters.mobject_update_utils.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

mobject\_update\_utils[¶](#module-manim.animation.updaters.mobject_update_utils "Link to this heading")
=======================================================================================================

Utility functions for continuous animation of mobjects.

Functions

always(*method*, *\*args*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#always)[¶](#manim.animation.updaters.mobject_update_utils.always "Link to this definition")
:   Parameters:
    :   **method** (*Callable*)

    Return type:
    :   [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

always\_redraw(*func*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#always_redraw)[¶](#manim.animation.updaters.mobject_update_utils.always_redraw "Link to this definition")
:   Redraw the mobject constructed by a function every frame.

    This function returns a mobject with an attached updater that
    continuously regenerates the mobject according to the
    specified function.

    Parameters:
    :   **func** (*Callable**[**[**]**,* [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]*) – A function without (required) input arguments that returns
        a mobject.

    Return type:
    :   [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Examples

    Example: TangentAnimation [¶](#tangentanimation)

    [
    ](./TangentAnimation-1.mp4)

    ```
    from manim import *

    class TangentAnimation(Scene):
        def construct(self):
            ax = Axes()
            sine = ax.plot(np.sin, color=RED)
            alpha = ValueTracker(0)
            point = always_redraw(
                lambda: Dot(
                    sine.point_from_proportion(alpha.get_value()),
                    color=BLUE
                )
            )
            tangent = always_redraw(
                lambda: TangentLine(
                    sine,
                    alpha=alpha.get_value(),
                    color=YELLOW,
                    length=4
                )
            )
            self.add(ax, sine, point, tangent)
            self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)

    ```

    ```

    class TangentAnimation(Scene):
        def construct(self):
            ax = Axes()
            sine = ax.plot(np.sin, color=RED)
            alpha = ValueTracker(0)
            point = always_redraw(
                lambda: Dot(
                    sine.point_from_proportion(alpha.get_value()),
                    color=BLUE
                )
            )
            tangent = always_redraw(
                lambda: TangentLine(
                    sine,
                    alpha=alpha.get_value(),
                    color=YELLOW,
                    length=4
                )
            )
            self.add(ax, sine, point, tangent)
            self.play(alpha.animate.set_value(1), rate_func=linear, run_time=2)


    ```

always\_rotate(*mobject*, *rate=0.3490658503988659*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#always_rotate)[¶](#manim.animation.updaters.mobject_update_utils.always_rotate "Link to this definition")
:   A mobject which is continuously rotated at a certain rate.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be rotated.
        * **rate** (*float*) – The angle which the mobject is rotated by
          over one second.
        * **kwags** – Further arguments to be passed to [`Mobject.rotate()`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate "manim.mobject.mobject.Mobject.rotate").

    Return type:
    :   [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Examples

    Example: SpinningTriangle [¶](#spinningtriangle)

    [
    ](./SpinningTriangle-1.mp4)

    ```
    from manim import *

    class SpinningTriangle(Scene):
        def construct(self):
            tri = Triangle().set_fill(opacity=1).set_z_index(2)
            sq = Square().to_edge(LEFT)

            # will keep spinning while there is an animation going on
            always_rotate(tri, rate=2*PI, about_point=ORIGIN)

            self.add(tri, sq)
            self.play(sq.animate.to_edge(RIGHT), rate_func=linear, run_time=1)

    ```

    ```

    class SpinningTriangle(Scene):
        def construct(self):
            tri = Triangle().set_fill(opacity=1).set_z_index(2)
            sq = Square().to_edge(LEFT)

            # will keep spinning while there is an animation going on
            always_rotate(tri, rate=2*PI, about_point=ORIGIN)

            self.add(tri, sq)
            self.play(sq.animate.to_edge(RIGHT), rate_func=linear, run_time=1)


    ```

always\_shift(*mobject*, *direction=array([1., 0., 0.])*, *rate=0.1*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#always_shift)[¶](#manim.animation.updaters.mobject_update_utils.always_shift "Link to this definition")
:   A mobject which is continuously shifted along some direction
    at a certain rate.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to shift.
        * **direction** (*ndarray**[**float64**]*) – The direction to shift. The vector is normalized, the specified magnitude
          is not relevant.
        * **rate** (*float*) – Length in Manim units which the mobject travels in one
          second along the specified direction.

    Return type:
    :   [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    Examples

    Example: ShiftingSquare [¶](#shiftingsquare)

    [
    ](./ShiftingSquare-1.mp4)

    ```
    from manim import *

    class ShiftingSquare(Scene):
        def construct(self):
            sq = Square().set_fill(opacity=1)
            tri = Triangle()
            VGroup(sq, tri).arrange(LEFT)

            # construct a square which is continuously
            # shifted to the right
            always_shift(sq, RIGHT, rate=5)

            self.add(sq)
            self.play(tri.animate.set_fill(opacity=1))

    ```

    ```

    class ShiftingSquare(Scene):
        def construct(self):
            sq = Square().set_fill(opacity=1)
            tri = Triangle()
            VGroup(sq, tri).arrange(LEFT)

            # construct a square which is continuously
            # shifted to the right
            always_shift(sq, RIGHT, rate=5)

            self.add(sq)
            self.play(tri.animate.set_fill(opacity=1))


    ```

assert\_is\_mobject\_method(*method*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#assert_is_mobject_method)[¶](#manim.animation.updaters.mobject_update_utils.assert_is_mobject_method "Link to this definition")
:   Parameters:
    :   **method** (*Callable*)

    Return type:
    :   None

cycle\_animation(*animation*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#cycle_animation)[¶](#manim.animation.updaters.mobject_update_utils.cycle_animation "Link to this definition")
:   Parameters:
    :   **animation** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))

    Return type:
    :   [Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

f\_always(*method*, *\*arg\_generators*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#f_always)[¶](#manim.animation.updaters.mobject_update_utils.f_always "Link to this definition")
:   More functional version of always, where instead
    of taking in args, it takes in functions which output
    the relevant arguments.

    Parameters:
    :   **method** (*Callable**[**[*[*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")*]**,* *None**]*)

    Return type:
    :   [*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

turn\_animation\_into\_updater(*animation*, *cycle=False*, *delay=0*, *\*\*kwargs*)[[source]](../_modules/manim/animation/updaters/mobject_update_utils.html#turn_animation_into_updater)[¶](#manim.animation.updaters.mobject_update_utils.turn_animation_into_updater "Link to this definition")
:   Add an updater to the animation’s mobject which applies
    the interpolation and update functions of the animation

    If cycle is True, this repeats over and over. Otherwise,
    the updater will be popped upon completion

    The `delay` parameter is the delay (in seconds) before the animation starts..

    Examples

    Example: WelcomeToManim [¶](#welcometomanim)

    [
    ](./WelcomeToManim-1.mp4)

    ```
    from manim import *

    class WelcomeToManim(Scene):
        def construct(self):
            words = Text("Welcome to")
            banner = ManimBanner().scale(0.5)
            VGroup(words, banner).arrange(DOWN)

            turn_animation_into_updater(Write(words, run_time=0.9))
            self.add(words)
            self.wait(0.5)
            self.play(banner.expand(), run_time=0.5)

    ```

    ```

    class WelcomeToManim(Scene):
        def construct(self):
            words = Text("Welcome to")
            banner = ManimBanner().scale(0.5)
            VGroup(words, banner).arrange(DOWN)

            turn_animation_into_updater(Write(words, run_time=0.9))
            self.add(words)
            self.wait(0.5)
            self.play(banner.expand(), run_time=0.5)


    ```

    Parameters:
    :   * **animation** ([*Animation*](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
        * **cycle** (*bool*)
        * **delay** (*float*)

    Return type:
    :   [Mobject](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")