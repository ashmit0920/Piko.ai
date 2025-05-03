# Source: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.functions.ParametricFunction.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ParametricFunction[¶](#parametricfunction "Link to this heading")
=================================================================

Qualified name: `manim.mobject.graphing.functions.ParametricFunction`

*class* ParametricFunction(*function*, *t\_range=(0*, *1)*, *scaling=<manim.mobject.graphing.scale.LinearBase object>*, *dt=1e-08*, *discontinuities=None*, *use\_smoothing=True*, *use\_vectorized=False*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/graphing/functions.html#ParametricFunction)[¶](#manim.mobject.graphing.functions.ParametricFunction "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A parametric curve.

    Parameters:
    :   * **function** (*Callable**[**[**float**]**,* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")*]*) – The function to be plotted in the form of `(lambda t: (x(t), y(t), z(t)))`
        * **t\_range** (*tuple**[**float**,* *float**]* *|* *tuple**[**float**,* *float**,* *float**]*) – Determines the length that the function spans in the form of (t\_min, t\_max, step=0.01). By default `[0, 1]`
        * **scaling** (*\_ScaleBase*) – Scaling class applied to the points of the function. Default of [`LinearBase`](manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase "manim.mobject.graphing.scale.LinearBase").
        * **use\_smoothing** (*bool*) – Whether to interpolate between the points of the function after they have been created.
          (Will have odd behaviour with a low number of points)
        * **use\_vectorized** (*bool*) – Whether to pass in the generated t value array to the function as `[t_0, t_1, ...]`.
          Only use this if your function supports it. Output should be a numpy array
          of shape `[[x_0, x_1, ...], [y_0, y_1, ...], [z_0, z_1, ...]]` but `z` can
          also be 0 if the Axes is 2D
        * **discontinuities** (*Iterable**[**float**]* *|* *None*) – Values of t at which the function experiences discontinuity.
        * **dt** (*float*) – The left and right tolerance for the discontinuities.

    Examples

    Example: PlotParametricFunction [¶](#plotparametricfunction)

    ![../_images/PlotParametricFunction-1.png](../_images/PlotParametricFunction-1.png)

    ```
    from manim import *

    class PlotParametricFunction(Scene):
        def func(self, t):
            return (np.sin(2 * t), np.sin(3 * t), 0)

        def construct(self):
            func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
            self.add(func.scale(3))

    ```

    ```

    class PlotParametricFunction(Scene):
        def func(self, t):
            return (np.sin(2 * t), np.sin(3 * t), 0)

        def construct(self):
            func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
            self.add(func.scale(3))


    ```

    Example: ThreeDParametricSpring [¶](#threedparametricspring)

    ![../_images/ThreeDParametricSpring-1.png](../_images/ThreeDParametricSpring-1.png)

    ```
    from manim import *

    class ThreeDParametricSpring(ThreeDScene):
        def construct(self):
            curve1 = ParametricFunction(
                lambda u: (
                    1.2 * np.cos(u),
                    1.2 * np.sin(u),
                    u * 0.05
                ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
            ).set_shade_in_3d(True)
            axes = ThreeDAxes()
            self.add(axes, curve1)
            self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
            self.wait()

    ```

    ```

    class ThreeDParametricSpring(ThreeDScene):
        def construct(self):
            curve1 = ParametricFunction(
                lambda u: (
                    1.2 * np.cos(u),
                    1.2 * np.sin(u),
                    u * 0.05
                ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
            ).set_shade_in_3d(True)
            axes = ThreeDAxes()
            self.add(axes, curve1)
            self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
            self.wait()


    ```

    Attention

    If your function has discontinuities, you’ll have to specify the location
    of the discontinuities manually. See the following example for guidance.

    Example: DiscontinuousExample [¶](#discontinuousexample)

    ![../_images/DiscontinuousExample-1.png](../_images/DiscontinuousExample-1.png)

    ```
    from manim import *

    class DiscontinuousExample(Scene):
        def construct(self):
            ax1 = NumberPlane((-3, 3), (-4, 4))
            ax2 = NumberPlane((-3, 3), (-4, 4))
            VGroup(ax1, ax2).arrange()
            discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
            incorrect = ax1.plot(discontinuous_function, color=RED)
            correct = ax2.plot(
                discontinuous_function,
                discontinuities=[-2, 2],  # discontinuous points
                dt=0.1,  # left and right tolerance of discontinuity
                color=GREEN,
            )
            self.add(ax1, ax2, incorrect, correct)

    ```

    ```

    class DiscontinuousExample(Scene):
        def construct(self):
            ax1 = NumberPlane((-3, 3), (-4, 4))
            ax2 = NumberPlane((-3, 3), (-4, 4))
            VGroup(ax1, ax2).arrange()
            discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
            incorrect = ax1.plot(discontinuous_function, color=RED)
            correct = ax2.plot(
                discontinuous_function,
                discontinuities=[-2, 2],  # discontinuous points
                dt=0.1,  # left and right tolerance of discontinuity
                color=GREEN,
            )
            self.add(ax1, ax2, incorrect, correct)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.graphing.functions.ParametricFunction.generate_points "manim.mobject.graphing.functions.ParametricFunction.generate_points") | Initializes `points` and therefore the shape. |
    | `get_function` |  |
    | `get_point_from_function` |  |
    | [`init_points`](#manim.mobject.graphing.functions.ParametricFunction.init_points "manim.mobject.graphing.functions.ParametricFunction.init_points") | Initializes `points` and therefore the shape. |

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

    \_original\_\_init\_\_(*function*, *t\_range=(0*, *1)*, *scaling=<manim.mobject.graphing.scale.LinearBase object>*, *dt=1e-08*, *discontinuities=None*, *use\_smoothing=True*, *use\_vectorized=False*, *\*\*kwargs*)[¶](#manim.mobject.graphing.functions.ParametricFunction._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **function** (*Callable**[**[**float**]**,* [*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")*]*)
            * **t\_range** (*tuple**[**float**,* *float**]* *|* *tuple**[**float**,* *float**,* *float**]*)
            * **scaling** (*\_ScaleBase*)
            * **dt** (*float*)
            * **discontinuities** (*Iterable**[**float**]* *|* *None*)
            * **use\_smoothing** (*bool*)
            * **use\_vectorized** (*bool*)

    generate\_points()[[source]](../_modules/manim/mobject/graphing/functions.html#ParametricFunction.generate_points)[¶](#manim.mobject.graphing.functions.ParametricFunction.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   Self

    init\_points()[¶](#manim.mobject.graphing.functions.ParametricFunction.init_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   Self