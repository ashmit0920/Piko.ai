# Source: https://docs.manim.community/en/stable/reference/manim.mobject.types.point_cloud_mobject.PMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

PMobject[¶](#pmobject "Link to this heading")
=============================================

Qualified name: `manim.mobject.types.point\_cloud\_mobject.PMobject`

*class* PMobject(*stroke\_width=4*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject)[¶](#manim.mobject.types.point_cloud_mobject.PMobject "Link to this definition")
:   Bases: [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    A disc made of a cloud of Dots

    Examples

    Example: PMobjectExample [¶](#pmobjectexample)

    ![../_images/PMobjectExample-1.png](../_images/PMobjectExample-1.png)

    ```
    from manim import *

    class PMobjectExample(Scene):
        def construct(self):

            pG = PGroup()  # This is just a collection of PMobject's

            # As the scale factor increases, the number of points
            # removed increases.
            for sf in range(1, 9 + 1):
                p = PointCloudDot(density=20, radius=1).thin_out(sf)
                # PointCloudDot is a type of PMobject
                # and can therefore be added to a PGroup
                pG.add(p)

            # This organizes all the shapes in a grid.
            pG.arrange_in_grid()

            self.add(pG)

    ```

    ```

    class PMobjectExample(Scene):
        def construct(self):

            pG = PGroup()  # This is just a collection of PMobject's

            # As the scale factor increases, the number of points
            # removed increases.
            for sf in range(1, 9 + 1):
                p = PointCloudDot(density=20, radius=1).thin_out(sf)
                # PointCloudDot is a type of PMobject
                # and can therefore be added to a PGroup
                pG.add(p)

            # This organizes all the shapes in a grid.
            pG.arrange_in_grid()

            self.add(pG)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`add_points`](#manim.mobject.types.point_cloud_mobject.PMobject.add_points "manim.mobject.types.point_cloud_mobject.PMobject.add_points") | Add points. |
    | `align_points_with_larger` |  |
    | `fade_to` |  |
    | `filter_out` |  |
    | `get_all_rgbas` |  |
    | `get_array_attrs` |  |
    | [`get_color`](#manim.mobject.types.point_cloud_mobject.PMobject.get_color "manim.mobject.types.point_cloud_mobject.PMobject.get_color") | Returns the color of the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
    | [`get_mobject_type_class`](#manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class "manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class") | Return the base class of this mobject type. |
    | [`get_point_mobject`](#manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject "manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject") | The simplest [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self. |
    | `get_stroke_width` |  |
    | `ingest_submobjects` |  |
    | `interpolate_color` |  |
    | `match_colors` |  |
    | `point_from_proportion` |  |
    | `pointwise_become_partial` |  |
    | [`reset_points`](#manim.mobject.types.point_cloud_mobject.PMobject.reset_points "manim.mobject.types.point_cloud_mobject.PMobject.reset_points") | Sets `points` to be an empty array. |
    | [`set_color`](#manim.mobject.types.point_cloud_mobject.PMobject.set_color "manim.mobject.types.point_cloud_mobject.PMobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
    | [`set_color_by_gradient`](#manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient "manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient") |  |
    | `set_colors_by_radial_gradient` |  |
    | `set_stroke_width` |  |
    | [`sort_points`](#manim.mobject.types.point_cloud_mobject.PMobject.sort_points "manim.mobject.types.point_cloud_mobject.PMobject.sort_points") | Function is any map from R^3 to R |
    | [`thin_out`](#manim.mobject.types.point_cloud_mobject.PMobject.thin_out "manim.mobject.types.point_cloud_mobject.PMobject.thin_out") | Removes all but every nth point for n = factor |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    Parameters:
    :   * **stroke\_width** (*int*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*stroke\_width=4*, *\*\*kwargs*)[¶](#manim.mobject.types.point_cloud_mobject.PMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **stroke\_width** (*int*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    add\_points(*points*, *rgbas=None*, *color=None*, *alpha=1*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.add_points)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.add_points "Link to this definition")
    :   Add points.

        Points must be a Nx3 numpy array.
        Rgbas must be a Nx4 numpy array if it is not None.

        Parameters:
        :   * **points** (*npt.NDArray*)
            * **rgbas** (*npt.NDArray* *|* *None*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
            * **alpha** (*float*)

        Return type:
        :   Self

    get\_color()[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_color)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.get_color "Link to this definition")
    :   Returns the color of the [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

        Examples

        ```
        >>> from manim import Square, RED
        >>> Square(color=RED).get_color() == RED
        True

        ```

        Return type:
        :   [*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

    *static* get\_mobject\_type\_class()[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_mobject_type_class)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.get_mobject_type_class "Link to this definition")
    :   Return the base class of this mobject type.

        Return type:
        :   type[[*PMobject*](#manim.mobject.types.point_cloud_mobject.PMobject "manim.mobject.types.point_cloud_mobject.PMobject")]

    get\_point\_mobject(*center=None*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.get_point_mobject)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.get_point_mobject "Link to this definition")
    :   The simplest [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self.
        Should by a point of the appropriate type

        Parameters:
        :   **center** ([*Point3DLike*](manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") *|* *None*)

        Return type:
        :   [Point](manim.mobject.types.point_cloud_mobject.Point.html#manim.mobject.types.point_cloud_mobject.Point "manim.mobject.types.point_cloud_mobject.Point")

    reset\_points()[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.reset_points)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.reset_points "Link to this definition")
    :   Sets `points` to be an empty array.

        Return type:
        :   Self

    set\_color(*color=ManimColor('#FFFF00')*, *family=True*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.set_color)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.set_color "Link to this definition")
    :   Condition is function which takes in one arguments, (x, y, z).
        Here it just recurses to submobjects, but in subclasses this
        should be further implemented based on the the inner workings
        of color

        Parameters:
        :   * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **family** (*bool*)

        Return type:
        :   Self

    set\_color\_by\_gradient(*\*colors*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.set_color_by_gradient)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.set_color_by_gradient "Link to this definition")
    :   Parameters:
        :   * **colors** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN).
            * **ManimColor.parse****(****color****)** (*self.color =*)
            * **self** (*return*)

        Return type:
        :   Self

    sort\_points(*function=<function PMobject.<lambda>>*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.sort_points)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.sort_points "Link to this definition")
    :   Function is any map from R^3 to R

        Parameters:
        :   **function** (*Callable**[**[**npt.NDArray**[*[*ManimFloat*](manim.typing.html#manim.typing.ManimFloat "manim.typing.ManimFloat")*]**]**,* *float**]*)

        Return type:
        :   Self

    thin\_out(*factor=5*)[[source]](../_modules/manim/mobject/types/point_cloud_mobject.html#PMobject.thin_out)[¶](#manim.mobject.types.point_cloud_mobject.PMobject.thin_out "Link to this definition")
    :   Removes all but every nth point for n = factor

        Parameters:
        :   **factor** (*int*)

        Return type:
        :   Self