# Source: https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TransformMatchingAbstractBase[¶](#transformmatchingabstractbase "Link to this heading")
=======================================================================================

Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingAbstractBase`

*class* TransformMatchingAbstractBase(*mobject=None*, *\*args*, *use\_override=True*, *\*\*kwargs*)[[source]](../_modules/manim/animation/transform_matching_parts.html#TransformMatchingAbstractBase)[¶](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase "Link to this definition")
:   Bases: [`AnimationGroup`](manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup "manim.animation.composition.AnimationGroup")

    Abstract base class for transformations that keep track of matching parts.

    Subclasses have to implement the two static methods
    `get_mobject_parts()` and
    `get_mobject_key()`.

    Basically, this transformation first maps all submobjects returned
    by the `get_mobject_parts` method to certain keys by applying the
    `get_mobject_key` method. Then, submobjects with matching keys
    are transformed into each other.

    Parameters:
    :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The starting [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The target [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
        * **transform\_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
          into each other by using [`Transform`](manim.animation.transform.Transform.html#manim.animation.transform.Transform "manim.animation.transform.Transform"). Default: `False`.
        * **fade\_transform\_mismatches** (*bool*) – Controls whether submobjects without a matching key are transformed
          into each other by using [`FadeTransform`](manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform "manim.animation.transform.FadeTransform"). Default: `False`.
        * **key\_map** (*dict* *|* *None*) – Optional. A dictionary mapping keys belonging to some of the starting mobject’s
          submobjects (i.e., the return values of the `get_mobject_key` method)
          to some keys belonging to the target mobject’s submobjects that should
          be transformed although the keys don’t match.
        * **kwargs** – All further keyword arguments are passed to the submobject transformations.

    Note

    If neither `transform_mismatches` nor `fade_transform_mismatches`
    are set to `True`, submobjects without matching keys in the starting
    mobject are faded out in the direction of the unmatched submobjects in
    the target mobject, and unmatched submobjects in the target mobject
    are faded in from the direction of the unmatched submobjects in the
    start mobject.

    Methods

    |  |  |
    | --- | --- |
    | [`clean_up_from_scene`](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene "manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene") | Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation. |
    | `get_mobject_key` |  |
    | `get_mobject_parts` |  |
    | `get_shape_map` |  |

    Attributes

    |  |  |
    | --- | --- |
    | `run_time` |  |

    \_original\_\_init\_\_(*mobject*, *target\_mobject*, *transform\_mismatches=False*, *fade\_transform\_mismatches=False*, *key\_map=None*, *\*\*kwargs*)[¶](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **target\_mobject** ([*Mobject*](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))
            * **transform\_mismatches** (*bool*)
            * **fade\_transform\_mismatches** (*bool*)
            * **key\_map** (*dict* *|* *None*)

    clean\_up\_from\_scene(*scene*)[[source]](../_modules/manim/animation/transform_matching_parts.html#TransformMatchingAbstractBase.clean_up_from_scene)[¶](#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene "Link to this definition")
    :   Clean up the [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") after finishing the animation.

        This includes to [`remove()`](manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove "manim.scene.scene.Scene.remove") the Animation’s
        [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") if the animation is a remover.

        Parameters:
        :   **scene** ([*Scene*](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.

        Return type:
        :   None