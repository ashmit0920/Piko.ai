# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Sector.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Sector[¶](#sector "Link to this heading")
=========================================

Qualified name: `manim.mobject.geometry.arc.Sector`

*class* Sector(*radius=1*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Sector)[¶](#manim.mobject.geometry.arc.Sector "Link to this definition")
:   Bases: [`AnnularSector`](manim.mobject.geometry.arc.AnnularSector.html#manim.mobject.geometry.arc.AnnularSector "manim.mobject.geometry.arc.AnnularSector")

    A sector of a circle.

    Examples

    Example: ExampleSector [¶](#examplesector)

    ![../_images/ExampleSector-1.png](../_images/ExampleSector-1.png)

    ```
    from manim import *

    class ExampleSector(Scene):
        def construct(self):
            sector = Sector(radius=2)
            sector2 = Sector(radius=2.5, angle=60*DEGREES).move_to([-3, 0, 0])
            sector.set_color(RED)
            sector2.set_color(PINK)
            self.add(sector, sector2)

    ```

    ```

    class ExampleSector(Scene):
        def construct(self):
            sector = Sector(radius=2)
            sector2 = Sector(radius=2.5, angle=60*DEGREES).move_to([-3, 0, 0])
            sector.set_color(RED)
            sector2.set_color(PINK)
            self.add(sector, sector2)


    ```

    Methods

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
    :   * **radius** (*float*)
        * **kwargs** (*Any*)

    \_original\_\_init\_\_(*radius=1*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Sector._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **radius** (*float*)
            * **kwargs** (*Any*)

        Return type:
        :   None