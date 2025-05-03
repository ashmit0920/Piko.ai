# Source: https://docs.manim.community/en/stable/reference/manim.mobject.geometry.arc.Annulus.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Annulus[¶](#annulus "Link to this heading")
===========================================

Qualified name: `manim.mobject.geometry.arc.Annulus`

*class* Annulus(*inner\_radius=1*, *outer\_radius=2*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *mark\_paths\_closed=False*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/geometry/arc.html#Annulus)[¶](#manim.mobject.geometry.arc.Annulus "Link to this definition")
:   Bases: [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    Region between two concentric [`Circles`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").

    Parameters:
    :   * **inner\_radius** (*float*) – The radius of the inner [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").
        * **outer\_radius** (*float*) – The radius of the outer [`Circle`](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle").
        * **kwargs** (*Any*) – Additional arguments to be passed to [`Annulus`](#manim.mobject.geometry.arc.Annulus "manim.mobject.geometry.arc.Annulus")
        * **fill\_opacity** (*float*)
        * **stroke\_width** (*float*)
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
        * **mark\_paths\_closed** (*bool*)

    Examples

    Example: AnnulusExample [¶](#annulusexample)

    ![../_images/AnnulusExample-1.png](../_images/AnnulusExample-1.png)

    ```
    from manim import *

    class AnnulusExample(Scene):
        def construct(self):
            annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)
            annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).next_to(annulus_1, DOWN)
            self.add(annulus_1, annulus_2)

    ```

    ```

    class AnnulusExample(Scene):
        def construct(self):
            annulus_1 = Annulus(inner_radius=0.5, outer_radius=1).shift(UP)
            annulus_2 = Annulus(inner_radius=0.3, outer_radius=0.6, color=RED).next_to(annulus_1, DOWN)
            self.add(annulus_1, annulus_2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.geometry.arc.Annulus.generate_points "manim.mobject.geometry.arc.Annulus.generate_points") | Initializes `points` and therefore the shape. |
    | [`init_points`](#manim.mobject.geometry.arc.Annulus.init_points "manim.mobject.geometry.arc.Annulus.init_points") | Initializes `points` and therefore the shape. |

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

    \_original\_\_init\_\_(*inner\_radius=1*, *outer\_radius=2*, *fill\_opacity=1*, *stroke\_width=0*, *color=ManimColor('#FFFFFF')*, *mark\_paths\_closed=False*, *\*\*kwargs*)[¶](#manim.mobject.geometry.arc.Annulus._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **inner\_radius** (*float*)
            * **outer\_radius** (*float*)
            * **fill\_opacity** (*float*)
            * **stroke\_width** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))
            * **mark\_paths\_closed** (*bool*)
            * **kwargs** (*Any*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/geometry/arc.html#Annulus.generate_points)[¶](#manim.mobject.geometry.arc.Annulus.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None

    init\_points()[¶](#manim.mobject.geometry.arc.Annulus.init_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None