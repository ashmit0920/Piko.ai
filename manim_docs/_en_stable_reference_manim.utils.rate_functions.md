# Source: https://docs.manim.community/en/stable/reference/manim.utils.rate_functions.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

rate\_functions[¶](#module-manim.utils.rate_functions "Link to this heading")
=============================================================================

A selection of rate functions, i.e., *speed curves* for animations.
Please find a standard list at <https://easings.net/>. Here is a picture
for the non-standard ones

Example: RateFuncExample [¶](#ratefuncexample)

![../_images/RateFuncExample-1.png](../_images/RateFuncExample-1.png)

```
from manim import *

class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)

```

```

class RateFuncExample(Scene):
    def construct(self):
        x = VGroup()
        for k, v in rate_functions.__dict__.items():
            if "function" in str(v):
                if (
                    not k.startswith("__")
                    and not k.startswith("sqrt")
                    and not k.startswith("bezier")
                ):
                    try:
                        rate_func = v
                        plot = (
                            ParametricFunction(
                                lambda x: [x, rate_func(x), 0],
                                t_range=[0, 1, .01],
                                use_smoothing=False,
                                color=YELLOW,
                            )
                            .stretch_to_fit_width(1.5)
                            .stretch_to_fit_height(1)
                        )
                        plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                        plot_title = (
                            Text(rate_func.__name__, weight=BOLD)
                            .scale(0.5)
                            .next_to(plot_bg, UP, buff=0.1)
                        )
                        x.add(VGroup(plot_bg, plot, plot_title))
                    except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                        pass
        x.arrange_in_grid(cols=8)
        x.height = config.frame_height
        x.width = config.frame_width
        x.move_to(ORIGIN).scale(0.95)
        self.add(x)


```

There are primarily 3 kinds of standard easing functions:

1. Ease In - The animation has a smooth start.
2. Ease Out - The animation has a smooth end.
3. Ease In Out - The animation has a smooth start as well as smooth end.

Note

The standard functions are not exported, so to use them you do something like this:
rate\_func=rate\_functions.ease\_in\_sine
On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.

Example: RateFunctions1Example [¶](#ratefunctions1example)

[
](./RateFunctions1Example-1.mp4)

```
from manim import *

class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()

```

```

class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        label1 = Tex("Ease In").next_to(line1, RIGHT)
        label2 = Tex("Ease out").next_to(line2, RIGHT)
        label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=7
        )
        self.wait()


```

Classes

|  |  |
| --- | --- |
| [`RateFunction`](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction") |  |

Functions

double\_smooth(*t*)[[source]](../_modules/manim/utils/rate_functions.html#double_smooth)[¶](#manim.utils.rate_functions.double_smooth "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_back(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_back)[¶](#manim.utils.rate_functions.ease_in_back "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_bounce(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_bounce)[¶](#manim.utils.rate_functions.ease_in_bounce "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_circ(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_circ)[¶](#manim.utils.rate_functions.ease_in_circ "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_cubic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_cubic)[¶](#manim.utils.rate_functions.ease_in_cubic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_elastic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_elastic)[¶](#manim.utils.rate_functions.ease_in_elastic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_expo(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_expo)[¶](#manim.utils.rate_functions.ease_in_expo "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_back(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_back)[¶](#manim.utils.rate_functions.ease_in_out_back "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_bounce(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_bounce)[¶](#manim.utils.rate_functions.ease_in_out_bounce "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_circ(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_circ)[¶](#manim.utils.rate_functions.ease_in_out_circ "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_cubic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_cubic)[¶](#manim.utils.rate_functions.ease_in_out_cubic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_elastic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_elastic)[¶](#manim.utils.rate_functions.ease_in_out_elastic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_expo(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_expo)[¶](#manim.utils.rate_functions.ease_in_out_expo "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quad(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_quad)[¶](#manim.utils.rate_functions.ease_in_out_quad "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quart(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_quart)[¶](#manim.utils.rate_functions.ease_in_out_quart "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_quint(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_quint)[¶](#manim.utils.rate_functions.ease_in_out_quint "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_out\_sine(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_out_sine)[¶](#manim.utils.rate_functions.ease_in_out_sine "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quad(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_quad)[¶](#manim.utils.rate_functions.ease_in_quad "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quart(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_quart)[¶](#manim.utils.rate_functions.ease_in_quart "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_quint(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_quint)[¶](#manim.utils.rate_functions.ease_in_quint "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_in\_sine(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_in_sine)[¶](#manim.utils.rate_functions.ease_in_sine "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_back(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_back)[¶](#manim.utils.rate_functions.ease_out_back "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_bounce(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_bounce)[¶](#manim.utils.rate_functions.ease_out_bounce "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_circ(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_circ)[¶](#manim.utils.rate_functions.ease_out_circ "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_cubic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_cubic)[¶](#manim.utils.rate_functions.ease_out_cubic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_elastic(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_elastic)[¶](#manim.utils.rate_functions.ease_out_elastic "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_expo(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_expo)[¶](#manim.utils.rate_functions.ease_out_expo "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quad(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_quad)[¶](#manim.utils.rate_functions.ease_out_quad "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quart(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_quart)[¶](#manim.utils.rate_functions.ease_out_quart "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_quint(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_quint)[¶](#manim.utils.rate_functions.ease_out_quint "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

ease\_out\_sine(*t*)[[source]](../_modules/manim/utils/rate_functions.html#ease_out_sine)[¶](#manim.utils.rate_functions.ease_out_sine "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

exponential\_decay(*t*, *half\_life=0.1*)[[source]](../_modules/manim/utils/rate_functions.html#exponential_decay)[¶](#manim.utils.rate_functions.exponential_decay "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **half\_life** (*float*)

    Return type:
    :   float

linear(*t*)[[source]](../_modules/manim/utils/rate_functions.html#linear)[¶](#manim.utils.rate_functions.linear "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

lingering(*t*)[[source]](../_modules/manim/utils/rate_functions.html#lingering)[¶](#manim.utils.rate_functions.lingering "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

not\_quite\_there(*func=<function smooth>*, *proportion=0.7*)[[source]](../_modules/manim/utils/rate_functions.html#not_quite_there)[¶](#manim.utils.rate_functions.not_quite_there "Link to this definition")
:   Parameters:
    :   * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction"))
        * **proportion** (*float*)

    Return type:
    :   [*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction")

running\_start(*t*, *pull\_factor=-0.5*)[[source]](../_modules/manim/utils/rate_functions.html#running_start)[¶](#manim.utils.rate_functions.running_start "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **pull\_factor** (*float*)

    Return type:
    :   float

rush\_from(*t*, *inflection=10.0*)[[source]](../_modules/manim/utils/rate_functions.html#rush_from)[¶](#manim.utils.rate_functions.rush_from "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **inflection** (*float*)

    Return type:
    :   float

rush\_into(*t*, *inflection=10.0*)[[source]](../_modules/manim/utils/rate_functions.html#rush_into)[¶](#manim.utils.rate_functions.rush_into "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **inflection** (*float*)

    Return type:
    :   float

slow\_into(*t*)[[source]](../_modules/manim/utils/rate_functions.html#slow_into)[¶](#manim.utils.rate_functions.slow_into "Link to this definition")
:   Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smooth(*t*, *inflection=10.0*)[[source]](../_modules/manim/utils/rate_functions.html#smooth)[¶](#manim.utils.rate_functions.smooth "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **inflection** (*float*)

    Return type:
    :   float

smoothererstep(*t*)[[source]](../_modules/manim/utils/rate_functions.html#smoothererstep)[¶](#manim.utils.rate_functions.smoothererstep "Link to this definition")
:   Implementation of the 3rd order SmoothStep sigmoid function.
    The 1st, 2nd and 3rd derivatives (speed, acceleration and jerk) are zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smootherstep(*t*)[[source]](../_modules/manim/utils/rate_functions.html#smootherstep)[¶](#manim.utils.rate_functions.smootherstep "Link to this definition")
:   Implementation of the 2nd order SmoothStep sigmoid function.
    The 1st and 2nd derivatives (speed and acceleration) are zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

smoothstep(*t*)[[source]](../_modules/manim/utils/rate_functions.html#smoothstep)[¶](#manim.utils.rate_functions.smoothstep "Link to this definition")
:   Implementation of the 1st order SmoothStep sigmoid function.
    The 1st derivative (speed) is zero at the endpoints.
    <https://en.wikipedia.org/wiki/Smoothstep>

    Parameters:
    :   **t** (*float*)

    Return type:
    :   float

squish\_rate\_func(*func*, *a=0.4*, *b=0.6*)[[source]](../_modules/manim/utils/rate_functions.html#squish_rate_func)[¶](#manim.utils.rate_functions.squish_rate_func "Link to this definition")
:   Parameters:
    :   * **func** ([*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction"))
        * **a** (*float*)
        * **b** (*float*)

    Return type:
    :   [*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction")

there\_and\_back(*t*, *inflection=10.0*)[[source]](../_modules/manim/utils/rate_functions.html#there_and_back)[¶](#manim.utils.rate_functions.there_and_back "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **inflection** (*float*)

    Return type:
    :   float

there\_and\_back\_with\_pause(*t*, *pause\_ratio=0.3333333333333333*)[[source]](../_modules/manim/utils/rate_functions.html#there_and_back_with_pause)[¶](#manim.utils.rate_functions.there_and_back_with_pause "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **pause\_ratio** (*float*)

    Return type:
    :   float

unit\_interval(*function*)[[source]](../_modules/manim/utils/rate_functions.html#unit_interval)[¶](#manim.utils.rate_functions.unit_interval "Link to this definition")
:   Parameters:
    :   **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction"))

    Return type:
    :   [*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction")

wiggle(*t*, *wiggles=2*)[[source]](../_modules/manim/utils/rate_functions.html#wiggle)[¶](#manim.utils.rate_functions.wiggle "Link to this definition")
:   Parameters:
    :   * **t** (*float*)
        * **wiggles** (*float*)

    Return type:
    :   float

zero(*function*)[[source]](../_modules/manim/utils/rate_functions.html#zero)[¶](#manim.utils.rate_functions.zero "Link to this definition")
:   Parameters:
    :   **function** ([*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction"))

    Return type:
    :   [*RateFunction*](manim.utils.rate_functions.RateFunction.html#manim.utils.rate_functions.RateFunction "manim.utils.rate_functions.RateFunction")