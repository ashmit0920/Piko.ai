# Source: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

mobject[¶](#module-manim.mobject.mobject "Link to this heading")
================================================================

Base classes for objects that can be displayed.

Type Aliases

*class* TimeBasedUpdater[¶](#manim.mobject.mobject.TimeBasedUpdater "Link to this definition")
:   ```
    Callable[['Mobject', float], object]

    ```

*class* NonTimeBasedUpdater[¶](#manim.mobject.mobject.NonTimeBasedUpdater "Link to this definition")
:   ```
    Callable[['Mobject'], object]

    ```

*class* Updater[¶](#manim.mobject.mobject.Updater "Link to this definition")
:   ```
    NonTimeBasedUpdater` | TimeBasedUpdater`
    ```

Classes

|  |  |
| --- | --- |
| [`Group`](manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group") | Groups together multiple [`Mobjects`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") | Mathematical Object: base class for objects that can be displayed on screen. |

Functions

override\_animate(*method*)[[source]](../_modules/manim/mobject/mobject.html#override_animate)[¶](#manim.mobject.mobject.override_animate "Link to this definition")
:   Decorator for overriding method animations.

    This allows to specify a method (returning an [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
    which is called when the decorated method is used with the `.animate` syntax
    for animating the application of a method.

    See also

    [`Mobject.animate`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate")

    Note

    Overridden methods cannot be combined with normal or other overridden
    methods using method chaining with the `.animate` syntax.

    Examples

    Example: AnimationOverrideExample [¶](#animationoverrideexample)

    [
    ](./AnimationOverrideExample-1.mp4)

    ```
    from manim import *

    class CircleWithContent(VGroup):
        def __init__(self, content):
            super().__init__()
            self.circle = Circle()
            self.content = content
            self.add(self.circle, content)
            content.move_to(self.circle.get_center())

        def clear_content(self):
            self.remove(self.content)
            self.content = None

        @override_animate(clear_content)
        def _clear_content_animation(self, anim_args=None):
            if anim_args is None:
                anim_args = {}
            anim = Uncreate(self.content, **anim_args)
            self.clear_content()
            return anim

    class AnimationOverrideExample(Scene):
        def construct(self):
            t = Text("hello!")
            my_mobject = CircleWithContent(t)
            self.play(Create(my_mobject))
            self.play(my_mobject.animate.clear_content())
            self.wait()

    ```

    ```

    class CircleWithContent(VGroup):
        def __init__(self, content):
            super().__init__()
            self.circle = Circle()
            self.content = content
            self.add(self.circle, content)
            content.move_to(self.circle.get_center())

        def clear_content(self):
            self.remove(self.content)
            self.content = None

        @override_animate(clear_content)
        def _clear_content_animation(self, anim_args=None):
            if anim_args is None:
                anim_args = {}
            anim = Uncreate(self.content, **anim_args)
            self.clear_content()
            return anim

    class AnimationOverrideExample(Scene):
        def construct(self):
            t = Text("hello!")
            my_mobject = CircleWithContent(t)
            self.play(Create(my_mobject))
            self.play(my_mobject.animate.clear_content())
            self.wait()


    ```

    Return type:
    :   *LambdaType*