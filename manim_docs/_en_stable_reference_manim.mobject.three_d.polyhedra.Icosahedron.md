# Source: https://docs.manim.community/en/stable/reference/manim.mobject.three_d.polyhedra.Icosahedron.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Icosahedron[¶](#icosahedron "Link to this heading")
===================================================

Qualified name: `manim.mobject.three\_d.polyhedra.Icosahedron`

*class* Icosahedron(*edge\_length=1*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/three_d/polyhedra.html#Icosahedron)[¶](#manim.mobject.three_d.polyhedra.Icosahedron "Link to this definition")
:   Bases: [`Polyhedron`](manim.mobject.three_d.polyhedra.Polyhedron.html#manim.mobject.three_d.polyhedra.Polyhedron "manim.mobject.three_d.polyhedra.Polyhedron")

    An icosahedron, one of the five platonic solids. It has 20 faces, 30 edges and 12 vertices.

    Parameters:
    :   **edge\_length** (*float*) – The length of an edge between any two vertices.

    Examples

    Example: IcosahedronScene [¶](#icosahedronscene)

    ![../_images/IcosahedronScene-1.png](../_images/IcosahedronScene-1.png)

    ```
    from manim import *

    class IcosahedronScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            obj = Icosahedron()
            self.add(obj)

    ```

    ```

    class IcosahedronScene(ThreeDScene):
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            obj = Icosahedron()
            self.add(obj)


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

    \_original\_\_init\_\_(*edge\_length=1*, *\*\*kwargs*)[¶](#manim.mobject.three_d.polyhedra.Icosahedron._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   **edge\_length** (*float*)