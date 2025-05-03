# Source: https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

ValueTracker[¶](#valuetracker "Link to this heading")
=====================================================

Qualified name: `manim.mobject.value\_tracker.ValueTracker`

*class* ValueTracker(*value=0*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/value_tracker.html#ValueTracker)[¶](#manim.mobject.value_tracker.ValueTracker "Link to this definition")
:   Bases: [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

    A mobject that can be used for tracking (real-valued) parameters.
    Useful for animating parameter changes.

    Not meant to be displayed. Instead the position encodes some
    number, often one which another animation or continual\_animation
    uses for its update function, and by treating it as a mobject it can
    still be animated and manipulated just like anything else.

    This value changes continuously when animated using the `animate` syntax.

    Examples

    Example: ValueTrackerExample [¶](#valuetrackerexample)

    [
    ](./ValueTrackerExample-1.mp4)

    ```
    from manim import *

    class ValueTrackerExample(Scene):
        def construct(self):
            number_line = NumberLine()
            pointer = Vector(DOWN)
            label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

            tracker = ValueTracker(0)
            pointer.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(tracker.get_value()),
                            UP
                        )
            )
            self.add(number_line, pointer,label)
            tracker += 1.5
            self.wait(1)
            tracker -= 4
            self.wait(0.5)
            self.play(tracker.animate.set_value(5))
            self.wait(0.5)
            self.play(tracker.animate.set_value(3))
            self.play(tracker.animate.increment_value(-2))
            self.wait(0.5)

    ```

    ```

    class ValueTrackerExample(Scene):
        def construct(self):
            number_line = NumberLine()
            pointer = Vector(DOWN)
            label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

            tracker = ValueTracker(0)
            pointer.add_updater(
                lambda m: m.next_to(
                            number_line.n2p(tracker.get_value()),
                            UP
                        )
            )
            self.add(number_line, pointer,label)
            tracker += 1.5
            self.wait(1)
            tracker -= 4
            self.wait(0.5)
            self.play(tracker.animate.set_value(5))
            self.wait(0.5)
            self.play(tracker.animate.set_value(3))
            self.play(tracker.animate.increment_value(-2))
            self.wait(0.5)


    ```

    Note

    You can also link ValueTrackers to updaters. In this case, you have to make sure that the
    ValueTracker is added to the scene by `add`

    Example: ValueTrackerExample [¶](#valuetrackerexample)

    [
    ](./ValueTrackerExample-2.mp4)

    ```
    from manim import *

    class ValueTrackerExample(Scene):
        def construct(self):
            tracker = ValueTracker(0)
            label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
            self.add(label)
            self.add(tracker)
            tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
            self.wait(2)

    ```

    ```

    class ValueTrackerExample(Scene):
        def construct(self):
            tracker = ValueTracker(0)
            label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
            self.add(label)
            self.add(tracker)
            tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
            self.wait(2)


    ```

    Methods

    |  |  |
    | --- | --- |
    | [`get_value`](#manim.mobject.value_tracker.ValueTracker.get_value "manim.mobject.value_tracker.ValueTracker.get_value") | Get the current value of this ValueTracker. |
    | [`increment_value`](#manim.mobject.value_tracker.ValueTracker.increment_value "manim.mobject.value_tracker.ValueTracker.increment_value") | Increments (adds) a scalar value to the ValueTracker |
    | [`interpolate`](#manim.mobject.value_tracker.ValueTracker.interpolate "manim.mobject.value_tracker.ValueTracker.interpolate") | Turns self into an interpolation between mobject1 and mobject2. |
    | [`set_value`](#manim.mobject.value_tracker.ValueTracker.set_value "manim.mobject.value_tracker.ValueTracker.set_value") | Sets a new scalar value to the ValueTracker |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `depth` | The depth of the mobject. |
    | `height` | The height of the mobject. |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*value=0*, *\*\*kwargs*)[¶](#manim.mobject.value_tracker.ValueTracker._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

    get\_value()[[source]](../_modules/manim/mobject/value_tracker.html#ValueTracker.get_value)[¶](#manim.mobject.value_tracker.ValueTracker.get_value "Link to this definition")
    :   Get the current value of this ValueTracker.

        Return type:
        :   float

    increment\_value(*d\_value*)[[source]](../_modules/manim/mobject/value_tracker.html#ValueTracker.increment_value)[¶](#manim.mobject.value_tracker.ValueTracker.increment_value "Link to this definition")
    :   Increments (adds) a scalar value to the ValueTracker

        Parameters:
        :   **d\_value** (*float*)

    interpolate(*mobject1*, *mobject2*, *alpha*, *path\_func=<function interpolate>*)[[source]](../_modules/manim/mobject/value_tracker.html#ValueTracker.interpolate)[¶](#manim.mobject.value_tracker.ValueTracker.interpolate "Link to this definition")
    :   Turns self into an interpolation between mobject1
        and mobject2.

    set\_value(*value*)[[source]](../_modules/manim/mobject/value_tracker.html#ValueTracker.set_value)[¶](#manim.mobject.value_tracker.ValueTracker.set_value "Link to this definition")
    :   Sets a new scalar value to the ValueTracker

        Parameters:
        :   **value** (*float*)