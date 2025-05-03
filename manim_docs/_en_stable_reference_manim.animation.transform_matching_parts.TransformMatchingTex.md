# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TransformMatchingTex[¶](#transformmatchingtex "Link to this heading")
=====================================================================

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingTex`

*class* TransformMatchingTex(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform_matching_parts.html#TransformMatchingTex)[¶](#manim.animation.transform_matching_parts.TransformMatchingTex "Link to this definition")
:   Bases: [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

    A transformation trying to transform rendered LaTeX strings.

    Two submobjects match if their `tex_string` matches.

    See also

    [`TransformMatchingAbstractBase`](manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")

    Examples

    Example: MatchingEquationParts [¶](#matchingequationparts)

    [
    ](./MatchingEquationParts-1.mp4)

    ```
    from manim import *

    class MatchingEquationParts(Scene):
        def construct(self):
            variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

            eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
            eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
            eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

            self.add(eq1)
            self.wait(0.5)
            self.play(TransformMatchingTex(Group(eq1, variables), eq2))
            self.wait(0.5)
            self.play(TransformMatchingTex(eq2, eq3))
            self.wait(0.5)

    ```

    ```

    class MatchingEquationParts(Scene):
        def construct(self):
            variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

            eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
            eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
            eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

            self.add(eq1)
            self.wait(0.5)
            self.play(TransformMatchingTex(Group(eq1, variables), eq2))
            self.wait(0.5)
            self.play(TransformMatchingTex(eq2, eq3))
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

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *transform\_mismatches=False*, *fade\_transform\_mismatches=False*, *key\_map=None*, *\*\*kwargs*)[¶](#manim.animation.transform_matching_parts.TransformMatchingTex._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **transform\_mismatches** (*bool*)
            * **fade\_transform\_mismatches** (*bool*)
            * **key\_map** (*dict* *|* *None*)