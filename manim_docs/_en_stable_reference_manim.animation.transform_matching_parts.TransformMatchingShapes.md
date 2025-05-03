# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingShapes.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TransformMatchingShapes[¶](#transformmatchingshapes "Link to this heading")
===========================================================================

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`

*class* TransformMatchingShapes(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform_matching_parts.html#TransformMatchingShapes)[¶](#manim.animation.transform_matching_parts.TransformMatchingShapes "Link to this definition")
:   Bases: [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

    An animation trying to transform groups by matching the shape
    of their submobjects.

    Two submobjects match if the hash of their point coordinates after
    normalization (i.e., after translation to the origin, fixing the submobject
    height at 1 unit, and rounding the coordinates to three decimal places)
    matches.

    See also

    [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

    Examples

    Example: Anagram [¶](#anagram)

    [
    ](./Anagram-1.mp4)

    ```
    from manim import *

    class Anagram(Scene):
        def construct(self):
            src = Text("the morse code")
            tar = Text("here come dots")
            self.play(Write(src))
            self.wait(0.5)
            self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
            self.wait(0.5)

    ```

    ```

    class Anagram(Scene):
        def construct(self):
            src = Text("the morse code")
            tar = Text("here come dots")
            self.play(Write(src))
            self.wait(0.5)
            self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
            self.wait(0.5)


    ```

    Methods

    |  |  |
    | --- | --- |
    | `get_mobject_key` |  |
    | `get_mobject_parts` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
        * **transform\_mismatches** (*bool*)
        * **fade\_transform\_mismatches** (*bool*)
        * **key\_map** (*dict* *|* *None*)

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *transform\_mismatches=False*, *fade\_transform\_mismatches=False*, *key\_map=None*, *\*\*kwargs*)[¶](#manim.animation.transform_matching_parts.TransformMatchingShapes._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **transform\_mismatches** (*bool*)
            * **fade\_transform\_mismatches** (*bool*)
            * **key\_map** (*dict* *|* *None*)