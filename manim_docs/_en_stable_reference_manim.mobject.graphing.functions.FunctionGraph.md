# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.FunctionGraph.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

FunctionGraph[¶](#functiongraph "Link to this heading")
=======================================================

Qualified name: `manim.mobject.graphing.functions.FunctionGraph`

*class* FunctionGraph(*function*, *x\_range=None*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/functions.html#FunctionGraph)[¶](#manim.mobject.graphing.functions.FunctionGraph "Link to this definition")
:   Bases: [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction")

    A [`ParametricFunction`](manim.mobject.graphing.functions.ParametricFunction.html#manim.mobject.graphing.functions.ParametricFunction "manim.mobject.graphing.functions.ParametricFunction") that spans the length of the scene by default.

    Examples

    Example: ExampleFunctionGraph [¶](#examplefunctiongraph)

    ![../_images/ExampleFunctionGraph-1.png](../_images/ExampleFunctionGraph-1.png)

    ```
    from manim import *

    class ExampleFunctionGraph(Scene):
        def construct(self):
            cos_func = FunctionGraph(
                lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
                color=RED,
            )

            sin_func_1 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                color=BLUE,
            )

            sin_func_2 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                x_range=[-4, 4],
                color=GREEN,
            ).move_to([0, 1, 0])

            self.add(cos_func, sin_func_1, sin_func_2)

    ```

    ```

    class ExampleFunctionGraph(Scene):
        def construct(self):
            cos_func = FunctionGraph(
                lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
                color=RED,
            )

            sin_func_1 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                color=BLUE,
            )

            sin_func_2 = FunctionGraph(
                lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
                x_range=[-4, 4],
                color=GREEN,
            ).move_to([0, 1, 0])

            self.add(cos_func, sin_func_1, sin_func_2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_function` |  |
    | `get_point_from_function` |  |

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

    \_original\_\_init\_\_(*function*, *x\_range=None*, *color=ManimColor('#FFFF00')*, *\*\*kwargs*)[¶](#manim.mobject.graphing.functions.FunctionGraph._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.