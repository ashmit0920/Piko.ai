# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.three_dimensions.Prism.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Prism[¶](#prism "Link to this heading")
=======================================

Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`

*class* Prism(*dimensions=[3, 2, 1]*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Prism)[¶](#manim.mobject.three_d.three_dimensions.Prism "Link to this definition")
:   Bases: [`Cube`](manim.mobject.three_d.three_dimensions.Cube.html#manim.mobject.three_d.three_dimensions.Cube "manim.mobject.three_d.three_dimensions.Cube")

    A right rectangular prism (or rectangular cuboid).
    Defined by the length of each side in `[x, y, z]` format.

    Parameters:
    :   **dimensions** (*tuple**[**float**,* *float**,* *float**]* *|* *np.ndarray*) – Dimensions of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism") in `[x, y, z]` format.

    Examples

    Example: ExamplePrism [¶](#exampleprism)

    ![../_images/ExamplePrism-1.png](../_images/ExamplePrism-1.png)

    ```
    from manim import *

    class ExamplePrism(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
            prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
            prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
            self.add(prismSmall, prismLarge)

    ```

    ```

    class ExamplePrism(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
            prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
            prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
            self.add(prismSmall, prismLarge)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.three_d.three_dimensions.Prism.generate_points "manim.mobject.three_d.three_dimensions.Prism.generate_points") | Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism"). |

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

    \_original\_\_init\_\_(*dimensions=[3, 2, 1]*, *\*\*kwargs*)[¶](#manim.mobject.three_d.three_dimensions.Prism._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **dimensions** (*tuple**[**float**,* *float**,* *float**]* *|* *ndarray*)

        Return type:
        :   None

    generate\_points()[[source]](../_modules/manim/mobject/three_d/three_dimensions.html#Prism.generate_points)[¶](#manim.mobject.three_d.three_dimensions.Prism.generate_points "Link to this definition")
    :   Creates the sides of the [`Prism`](#manim.mobject.three_d.three_dimensions.Prism "manim.mobject.three_d.three_dimensions.Prism").

        Return type:
        :   None