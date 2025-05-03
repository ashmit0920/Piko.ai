# Source: https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ComplexValueTracker.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ComplexValueTracker[¶](#complexvaluetracker "Link to this heading")
===================================================================

Qualified name: `manim.mobject.value\_tracker.ComplexValueTracker`

*class* ComplexValueTracker(*value=0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/value_tracker.html#ComplexValueTracker)[¶](#manim.mobject.value_tracker.ComplexValueTracker "Link to this definition")
:   Bases: [`ValueTracker`](manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker")

    Tracks a complex-valued parameter.

    When the value is set through `animate`, the value will take a straight path from the
    source point to the destination point.

    Examples

    Example: ComplexValueTrackerExample [¶](#complexvaluetrackerexample)

    [
    ](./ComplexValueTrackerExample-1.mp4)

    ```
    from manim import *

    class ComplexValueTrackerExample(Scene):
        def construct(self):
            tracker = ComplexValueTracker(-2+1j)
            dot = Dot().add_updater(
                lambda x: x.move_to(tracker.points)
            )

            self.add(NumberPlane(), dot)

            self.play(tracker.animate.set_value(3+2j))
            self.play(tracker.animate.set_value(tracker.get_value() * 1j))
            self.play(tracker.animate.set_value(tracker.get_value() - 2j))
            self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

    ```

    ```

    class ComplexValueTrackerExample(Scene):
        def construct(self):
            tracker = ComplexValueTracker(-2+1j)
            dot = Dot().add_updater(
                lambda x: x.move_to(tracker.points)
            )

            self.add(NumberPlane(), dot)

            self.play(tracker.animate.set_value(3+2j))
            self.play(tracker.animate.set_value(tracker.get_value() * 1j))
            self.play(tracker.animate.set_value(tracker.get_value() - 2j))
            self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_value`](#manim.mobject.value_tracker.ComplexValueTracker.get_value "manim.mobject.value_tracker.ComplexValueTracker.get_value") | Get the current value of this value tracker as a complex number. |
    | [`set_value`](#manim.mobject.value_tracker.ComplexValueTracker.set_value "manim.mobject.value_tracker.ComplexValueTracker.set_value") | Sets a new complex value to the ComplexValueTracker |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*value=0*, *\*\*kwargs*)[¶](#manim.mobject.value_tracker.ComplexValueTracker._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

    get\_value()[[source]](../_modules/manim/mobject/value_tracker.html#ComplexValueTracker.get_value)[¶](#manim.mobject.value_tracker.ComplexValueTracker.get_value "Link to this definition")
    :   Get the current value of this value tracker as a complex number.

        The value is internally stored as a points array [a, b, 0]. This can be accessed directly
        to represent the value geometrically, see the usage example.

    set\_value(*z*)[[source]](../_modules/manim/mobject/value_tracker.html#ComplexValueTracker.set_value)[¶](#manim.mobject.value_tracker.ComplexValueTracker.set_value "Link to this definition")
    :   Sets a new complex value to the ComplexValueTracker