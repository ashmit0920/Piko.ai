# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.AnnularSector.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

AnnularSector[¶](#annularsector "Link to this heading")
=======================================================

Qualified name: `manim.mobject.geometry.arc.AnnularSector`

*class* AnnularSector(*inner\_radius=1*, *outer\_radius=2*, *angle=1.5707963267948966*, *start\_angle=0*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#AnnularSector)[¶](#manim.mobject.geometry.arc.AnnularSector "Link to this definition")
:   Bases: [`Arc`](manim.mobject.geometry.arc.Arc.html#manim.mobject.geometry.arc.Arc "manim.mobject.geometry.arc.Arc")

    A sector of an annulus.

    Parameters:
    :   * **inner\_radius** (*float*) – The inside radius of the Annular Sector.
        * **outer\_radius** (*float*) – The outside radius of the Annular Sector.
        * **angle** (*float*) – The clockwise angle of the Annular Sector.
        * **start\_angle** (*float*) – The starting clockwise angle of the Annular Sector.
        * **fill\_opacity** (*float*) – The opacity of the color filled in the Annular Sector.
        * **stroke\_width** (*float*) – The stroke width of the Annular Sector.
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The color filled into the Annular Sector.
        * **kwargs** (*Any*)

    Examples

    Example: AnnularSectorExample [¶](#annularsectorexample)

    ![../_images/AnnularSectorExample-1.png](../_images/AnnularSectorExample-1.png)

    ```
    from manim import *

    class AnnularSectorExample(Scene):
        def construct(self):
            # Changes background color to clearly visualize changes in fill_opacity.
            self.camera.background_color = WHITE

            # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
            s1 = AnnularSector(color=YELLOW).move_to(2 * UL)

            # Different inner_radius and outer_radius than the default.
            s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 * DEGREES, color=RED).move_to(2 * UR)

            # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
            s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 * DL)

            # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
            s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 * PI / 2, color=GREEN).move_to(2 * DR)

            self.add(s1, s2, s3, s4)

    ```

    ```

    class AnnularSectorExample(Scene):
        def construct(self):
            # Changes background color to clearly visualize changes in fill_opacity.
            self.camera.background_color = WHITE

            # The default parameter start_angle is 0, so the AnnularSector starts from the +x-axis.
            s1 = AnnularSector(color=YELLOW).move_to(2 * UL)

            # Different inner_radius and outer_radius than the default.
            s2 = AnnularSector(inner_radius=1.5, outer_radius=2, angle=45 * DEGREES, color=RED).move_to(2 * UR)

            # fill_opacity is typically a number > 0 and <= 1. If fill_opacity=0, the AnnularSector is transparent.
            s3 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=PI, fill_opacity=0.25, color=BLUE).move_to(2 * DL)

            # With a negative value for the angle, the AnnularSector is drawn clockwise from the start value.
            s4 = AnnularSector(inner_radius=1, outer_radius=1.5, angle=-3 * PI / 2, color=GREEN).move_to(2 * DR)

            self.add(s1, s2, s3, s4)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.geometry.arc.AnnularSector.generate_points "manim.mobject.geometry.arc.AnnularSector.generate_points") | Initializes `points` and therefore the shape. |
    | [`init_points`](#manim.mobject.geometry.arc.AnnularSector.init_points "manim.mobject.geometry.arc.AnnularSector.init_points") | Initializes `points` and therefore the shape. |

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

    \_original\_\_init\_\_(*inner\_radius=1*, *outer\_radius=2*, *angle=1.5707963267948966*, *start\_angle=0*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.AnnularSector._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **inner\_radius** (*float*)
            * **outer\_radius** (*float*)
            * **angle** (*float*)
            * **start\_angle** (*float*)
            * **fill\_opacity** (*float*)
            * **stroke\_width** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/geometry/arc.html#AnnularSector.generate_points)[¶](#manim.mobject.geometry.arc.AnnularSector.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None

    init\_points()[¶](#manim.mobject.geometry.arc.AnnularSector.init_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None