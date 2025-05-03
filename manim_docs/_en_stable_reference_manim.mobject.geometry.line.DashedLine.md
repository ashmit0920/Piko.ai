# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.line.DashedLine.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DashedLine[¶](#dashedline "Link to this heading")
=================================================

Qualified name: `manim.mobject.geometry.line.DashedLine`

*class* DashedLine(*\*args*, *dash\_length=0.05*, *dashed\_ratio=0.5*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine)[¶](#manim.mobject.geometry.line.DashedLine "Link to this definition")
:   Bases: [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

    A dashed [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line").

    Parameters:
    :   * **args** (*Any*) – Arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")
        * **dash\_length** (*float*) – The length of each individual dash of the line.
        * **dashed\_ratio** (*float*) – The ratio of dash space to empty space. Range of 0-1.
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Line`](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

    See also

    [`DashedVMobject`](manim.mobject.types.vectorized_mobject.DashedVMobject.html#manim.mobject.types.vectorized_mobject.DashedVMobject "manim.mobject.types.vectorized_mobject.DashedVMobject")

    Examples

    Example: DashedLineExample [¶](#dashedlineexample)

    ![../_images/DashedLineExample-1.png](../_images/DashedLineExample-1.png)

    ```
    from manim import *

    class DashedLineExample(Scene):
        def construct(self):
            # dash_length increased
            dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
            # normal
            dashed_2 = DashedLine(config.left_side, config.right_side)
            # dashed_ratio decreased
            dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
            self.add(dashed_1, dashed_2, dashed_3)

    ```

    ```

    class DashedLineExample(Scene):
        def construct(self):
            # dash_length increased
            dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
            # normal
            dashed_2 = DashedLine(config.left_side, config.right_side)
            # dashed_ratio decreased
            dashed_3 = DashedLine(config.left_side, config.right_side, dashed_ratio=0.1).shift(DOWN*2)
            self.add(dashed_1, dashed_2, dashed_3)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_end`](#manim.mobject.geometry.line.DashedLine.get_end "manim.mobject.geometry.line.DashedLine.get_end") | Returns the end point of the line. |
    | [`get_first_handle`](#manim.mobject.geometry.line.DashedLine.get_first_handle "manim.mobject.geometry.line.DashedLine.get_first_handle") | Returns the point of the first handle. |
    | [`get_last_handle`](#manim.mobject.geometry.line.DashedLine.get_last_handle "manim.mobject.geometry.line.DashedLine.get_last_handle") | Returns the point of the last handle. |
    | [`get_start`](#manim.mobject.geometry.line.DashedLine.get_start "manim.mobject.geometry.line.DashedLine.get_start") | Returns the start point of the line. |

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

    \_calculate\_num\_dashes()[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine._calculate_num_dashes)[¶](#manim.mobject.geometry.line.DashedLine._calculate_num_dashes "Link to this definition")
    :   Returns the number of dashes in the dashed line.

        Examples

        ```
        >>> DashedLine()._calculate_num_dashes()
        20

        ```

        Return type:
        :   int

    \_original\_\_init\_\_(*\*args*, *dash\_length=0.05*, *dashed\_ratio=0.5*, *\*\*kwargs*)[¶](#manim.mobject.geometry.line.DashedLine._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **args** (*Any*)
            * **dash\_length** (*float*)
            * **dashed\_ratio** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    get\_end()[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine.get_end)[¶](#manim.mobject.geometry.line.DashedLine.get_end "Link to this definition")
    :   Returns the end point of the line.

        Examples

        ```
        >>> DashedLine().get_end()
        array([1., 0., 0.])

        ```

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    get\_first\_handle()[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine.get_first_handle)[¶](#manim.mobject.geometry.line.DashedLine.get_first_handle "Link to this definition")
    :   Returns the point of the first handle.

        Examples

        ```
        >>> DashedLine().get_first_handle()
        array([-0.98333333,  0.        ,  0.        ])

        ```

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    get\_last\_handle()[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine.get_last_handle)[¶](#manim.mobject.geometry.line.DashedLine.get_last_handle "Link to this definition")
    :   Returns the point of the last handle.

        Examples

        ```
        >>> DashedLine().get_last_handle()
        array([0.98333333, 0.        , 0.        ])

        ```

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

    get\_start()[[source]](../_modules/manim/mobject/geometry/line.html#DashedLine.get_start)[¶](#manim.mobject.geometry.line.DashedLine.get_start "Link to this definition")
    :   Returns the start point of the line.

        Examples

        ```
        >>> DashedLine().get_start()
        array([-1.,  0.,  0.])

        ```

        Return type:
        :   [*Point3D*](manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")