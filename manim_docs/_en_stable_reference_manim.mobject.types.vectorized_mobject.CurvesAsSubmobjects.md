# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

CurvesAsSubmobjects[¶](#curvesassubmobjects "Link to this heading")
===================================================================

Qualified name: `manim.mobject.types.vectorized\_mobject.CurvesAsSubmobjects`

*class* CurvesAsSubmobjects(*vmobject*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/vectorized_mobject.html#CurvesAsSubmobjects)[¶](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "Link to this definition")
:   Bases: [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")

    Convert a curve’s elements to submobjects.

    Examples

    Example: LineGradientExample [¶](#linegradientexample)

    ![../_images/LineGradientExample-1.png](../_images/LineGradientExample-1.png)

    ```
    from manim import *

    class LineGradientExample(Scene):
        def construct(self):
            curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
            new_curve = CurvesAsSubmobjects(curve)
            new_curve.set_color_by_gradient(BLUE, RED)
            self.add(new_curve.shift(UP), curve)

    ```

    ```

    class LineGradientExample(Scene):
        def construct(self):
            curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
            new_curve = CurvesAsSubmobjects(curve)
            new_curve.set_color_by_gradient(BLUE, RED)
            self.add(new_curve.shift(UP), curve)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`point_from_proportion`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion") | Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects"). |

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

    Parameters:
    :   **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

    \_original\_\_init\_\_(*vmobject*, *\*\*kwargs*)[¶](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **vmobject** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject"))

        Return type:
        :   None

    point\_from\_proportion(*alpha*)[[source]](../_modules/manim/mobject/types/vectorized_mobject.html#CurvesAsSubmobjects.point_from_proportion)[¶](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.point_from_proportion "Link to this definition")
    :   Gets the point at a proportion along the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

        Parameters:
        :   **alpha** (*float*) – The proportion along the the path of the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

        Returns:
        :   The point on the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects").

        Return type:
        :   `numpy.ndarray`

        Raises:
        :   * **ValueError** – If `alpha` is not between 0 and 1.
            * **Exception** – If the [`CurvesAsSubmobjects`](#manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects "manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects") has no submobjects, or no submobject has points.