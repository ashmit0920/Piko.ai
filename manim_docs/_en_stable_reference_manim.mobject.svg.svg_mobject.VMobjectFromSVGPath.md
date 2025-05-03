# Source: https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

VMobjectFromSVGPath[¶](#vmobjectfromsvgpath "Link to this heading")
===================================================================

Qualified name: `manim.mobject.svg.svg\_mobject.VMobjectFromSVGPath`

*class* VMobjectFromSVGPath(*path\_obj*, *long\_lines=False*, *should\_subdivide\_sharp\_curves=False*, *should\_remove\_null\_curves=False*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#VMobjectFromSVGPath)[¶](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A vectorized mobject representing an SVG path.

    Note

    The `long_lines`, `should_subdivide_sharp_curves`,
    and `should_remove_null_curves` keyword arguments are
    only respected with the OpenGL renderer.

    Parameters:
    :   * **path\_obj** (*se.Path*) – A parsed SVG path object.
        * **long\_lines** (*bool*) – Whether or not straight lines in the vectorized mobject
          are drawn in one or two segments.
        * **should\_subdivide\_sharp\_curves** (*bool*) – Whether or not to subdivide subcurves further in case
          two segments meet at an angle that is sharper than a
          given threshold.
        * **should\_remove\_null\_curves** (*bool*) – Whether or not to remove subcurves of length 0.
        * **kwargs** – Further keyword arguments are passed to the parent
          class.

    Methods

    |  |  |
    | --- | --- |
    | [`generate_points`](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points") | Initializes `points` and therefore the shape. |
    | `handle_commands` |  |
    | `init_points` |  |

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

    \_original\_\_init\_\_(*path\_obj*, *long\_lines=False*, *should\_subdivide\_sharp\_curves=False*, *should\_remove\_null\_curves=False*, *\*\*kwargs*)[¶](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **path\_obj** (*Path*)
            * **long\_lines** (*bool*)
            * **should\_subdivide\_sharp\_curves** (*bool*)
            * **should\_remove\_null\_curves** (*bool*)

    generate\_points()[¶](#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.generate_points "Link to this definition")
    :   Initializes `points` and therefore the shape.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.

        Return type:
        :   None