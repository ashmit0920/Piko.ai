# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Text[¶](#text "Link to this heading")
=====================================

Qualified name: `manim.mobject.text.text\_mobject.Text`

*class* Text(*text*, *fill\_opacity=1.0*, *stroke\_width=0*, *\**, *color=ManimColor('#FFFFFF')*, *font\_size=48*, *line\_spacing=-1*, *font=''*, *slant='NORMAL'*, *weight='NORMAL'*, *t2c=None*, *t2f=None*, *t2g=None*, *t2s=None*, *t2w=None*, *gradient=None*, *tab\_width=4*, *warn\_missing\_font=True*, *height=None*, *width=None*, *should\_center=True*, *disable\_ligatures=False*, *use\_svg\_cache=False*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text)[¶](#manim.mobject.text.text_mobject.Text "Link to this definition")
:   Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")

    Display (non-LaTeX) text rendered using [Pango](https://pango.gnome.org/).

    Text objects behave like a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup")-like iterable of all characters
    in the given text. In particular, slicing is possible.

    Parameters:
    :   * **text** (*str*) – The text that needs to be created as a mobject.
        * **font** (*str*) – The font family to be used to render the text. This is either a system font or
          one loaded with register\_font(). Note that font family names may be different
          across operating systems.
        * **warn\_missing\_font** (*bool*) – If True (default), Manim will issue a warning if the font does not exist in the
          (case-sensitive) list of fonts returned from manimpango.list\_fonts().
        * **fill\_opacity** (*float*)
        * **stroke\_width** (*float*)
        * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
        * **font\_size** (*float*)
        * **line\_spacing** (*float*)
        * **slant** (*str*)
        * **weight** (*str*)
        * **t2c** (*dict**[**str**,* *str**]*)
        * **t2f** (*dict**[**str**,* *str**]*)
        * **t2g** (*dict**[**str**,* *tuple**]*)
        * **t2s** (*dict**[**str**,* *str**]*)
        * **t2w** (*dict**[**str**,* *str**]*)
        * **gradient** (*tuple*)
        * **tab\_width** (*int*)
        * **height** (*float*)
        * **width** (*float*)
        * **should\_center** (*bool*)
        * **disable\_ligatures** (*bool*)
        * **use\_svg\_cache** (*bool*)

    Returns:
    :   The mobject-like [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup "manim.mobject.types.vectorized_mobject.VGroup").

    Return type:
    :   [`Text`](#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text")

    Examples

    Example: Example1Text [¶](#example1text)

    ![../_images/Example1Text-1.png](../_images/Example1Text-1.png)

    ```
    from manim import *

    class Example1Text(Scene):
        def construct(self):
            text = Text('Hello world').scale(3)
            self.add(text)

    ```

    ```

    class Example1Text(Scene):
        def construct(self):
            text = Text('Hello world').scale(3)
            self.add(text)


    ```

    Example: TextColorExample [¶](#textcolorexample)

    ![../_images/TextColorExample-1.png](../_images/TextColorExample-1.png)

    ```
    from manim import *

    class TextColorExample(Scene):
        def construct(self):
            text1 = Text('Hello world', color=BLUE).scale(3)
            text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
            self.add(text1, text2)

    ```

    ```

    class TextColorExample(Scene):
        def construct(self):
            text1 = Text('Hello world', color=BLUE).scale(3)
            text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
            self.add(text1, text2)


    ```

    Example: TextItalicAndBoldExample [¶](#textitalicandboldexample)

    ![../_images/TextItalicAndBoldExample-1.png](../_images/TextItalicAndBoldExample-1.png)

    ```
    from manim import *

    class TextItalicAndBoldExample(Scene):
        def construct(self):
            text1 = Text("Hello world", slant=ITALIC)
            text2 = Text("Hello world", t2s={'world':ITALIC})
            text3 = Text("Hello world", weight=BOLD)
            text4 = Text("Hello world", t2w={'world':BOLD})
            text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
            text6 = Text(
                "Visit us at docs.manim.community",
                t2c={"docs.manim.community": YELLOW},
                disable_ligatures=True,
           )
            text6.scale(1.3).shift(DOWN)
            self.add(text1, text2, text3, text4, text5 , text6)
            Group(*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)

    ```

    ```

    class TextItalicAndBoldExample(Scene):
        def construct(self):
            text1 = Text("Hello world", slant=ITALIC)
            text2 = Text("Hello world", t2s={'world':ITALIC})
            text3 = Text("Hello world", weight=BOLD)
            text4 = Text("Hello world", t2w={'world':BOLD})
            text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
            text6 = Text(
                "Visit us at docs.manim.community",
                t2c={"docs.manim.community": YELLOW},
                disable_ligatures=True,
           )
            text6.scale(1.3).shift(DOWN)
            self.add(text1, text2, text3, text4, text5 , text6)
            Group(*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)


    ```

    Example: TextMoreCustomization [¶](#textmorecustomization)

    ![../_images/TextMoreCustomization-1.png](../_images/TextMoreCustomization-1.png)

    ```
    from manim import *

    class TextMoreCustomization(Scene):
        def construct(self):
            text1 = Text(
                'Google',
                t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                     '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                     '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
            self.add(text1)

    ```

    ```

    class TextMoreCustomization(Scene):
        def construct(self):
            text1 = Text(
                'Google',
                t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                     '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                     '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
            self.add(text1)


    ```

    As [`Text`](#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") uses Pango to render text, rendering non-English
    characters is easily possible:

    Example: MultipleFonts [¶](#multiplefonts)

    ![../_images/MultipleFonts-1.png](../_images/MultipleFonts-1.png)

    ```
    from manim import *

    class MultipleFonts(Scene):
        def construct(self):
            morning = Text("வணக்கம்", font="sans-serif")
            japanese = Text(
                "日本へようこそ", t2c={"日本": BLUE}
            )  # works same as ``Text``.
            mess = Text("Multi-Language", weight=BOLD)
            russ = Text("Здравствуйте मस नम म ", font="sans-serif")
            hin = Text("नमस्ते", font="sans-serif")
            arb = Text(
                "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
            )  # don't mix RTL and LTR languages nothing shows up then ;-)
            chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
            self.add(morning, japanese, mess, russ, hin, arb, chinese)
            for i,mobj in enumerate(self.mobjects):
                mobj.shift(DOWN*(i-3))

    ```

    ```

    class MultipleFonts(Scene):
        def construct(self):
            morning = Text("வணக்கம்", font="sans-serif")
            japanese = Text(
                "日本へようこそ", t2c={"日本": BLUE}
            )  # works same as ``Text``.
            mess = Text("Multi-Language", weight=BOLD)
            russ = Text("Здравствуйте मस नम म ", font="sans-serif")
            hin = Text("नमस्ते", font="sans-serif")
            arb = Text(
                "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
            )  # don't mix RTL and LTR languages nothing shows up then ;-)
            chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
            self.add(morning, japanese, mess, russ, hin, arb, chinese)
            for i,mobj in enumerate(self.mobjects):
                mobj.shift(DOWN*(i-3))


    ```

    Example: PangoRender [¶](#pangorender)

    [
    ](./PangoRender-1.mp4)

    ```
    from manim import *

    class PangoRender(Scene):
        def construct(self):
            morning = Text("வணக்கம்", font="sans-serif")
            self.play(Write(morning))
            self.wait(2)

    ```

    ```

    class PangoRender(Scene):
        def construct(self):
            morning = Text("வணக்கம்", font="sans-serif")
            self.play(Write(morning))
            self.wait(2)


    ```

    Tests

    Check that the creation of [`Text`](#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") works:

    ```
    >>> Text('The horse does not eat cucumber salad.')
    Text('The horse does not eat cucumber salad.')

    ```

    Methods

    |  |  |
    | --- | --- |
    | `font_list` |  |
    | [`init_colors`](#manim.mobject.text.text_mobject.Text.init_colors "manim.mobject.text.text_mobject.Text.init_colors") | Initializes the colors. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | `font_size` |  |
    | `hash_seed` | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_find\_indexes(*word*, *text*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._find_indexes)[¶](#manim.mobject.text.text_mobject.Text._find_indexes "Link to this definition")
    :   Finds the indexes of `text` in `word`.

        Parameters:
        :   * **word** (*str*)
            * **text** (*str*)

    \_original\_\_init\_\_(*text*, *fill\_opacity=1.0*, *stroke\_width=0*, *color=None*, *font\_size=48*, *line\_spacing=-1*, *font=''*, *slant='NORMAL'*, *weight='NORMAL'*, *t2c=None*, *t2f=None*, *t2g=None*, *t2s=None*, *t2w=None*, *gradient=None*, *tab\_width=4*, *warn\_missing\_font=True*, *height=None*, *width=None*, *should\_center=True*, *disable\_ligatures=False*, *use\_svg\_cache=False*, *\*\*kwargs*)[¶](#manim.mobject.text.text_mobject.Text._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **text** (*str*)
            * **fill\_opacity** (*float*)
            * **stroke\_width** (*float*)
            * **color** ([*ParsableManimColor*](manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") *|* *None*)
            * **font\_size** (*float*)
            * **line\_spacing** (*float*)
            * **font** (*str*)
            * **slant** (*str*)
            * **weight** (*str*)
            * **t2c** (*dict**[**str**,* *str**]*)
            * **t2f** (*dict**[**str**,* *str**]*)
            * **t2g** (*dict**[**str**,* *tuple**]*)
            * **t2s** (*dict**[**str**,* *str**]*)
            * **t2w** (*dict**[**str**,* *str**]*)
            * **gradient** (*tuple*)
            * **tab\_width** (*int*)
            * **warn\_missing\_font** (*bool*)
            * **height** (*float*)
            * **width** (*float*)
            * **should\_center** (*bool*)
            * **disable\_ligatures** (*bool*)
            * **use\_svg\_cache** (*bool*)

        Return type:
        :   None

    \_set\_color\_by\_t2c(*t2c=None*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._set_color_by_t2c)[¶](#manim.mobject.text.text_mobject.Text._set_color_by_t2c "Link to this definition")
    :   Sets color for specified strings.

        Attention

        Deprecated
        The method Text.\_set\_color\_by\_t2c has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.

    \_set\_color\_by\_t2g(*t2g=None*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._set_color_by_t2g)[¶](#manim.mobject.text.text_mobject.Text._set_color_by_t2g "Link to this definition")
    :   Sets gradient colors for specified
        strings. Behaves similarly to `set_color_by_t2c`.

        Attention

        Deprecated
        The method Text.\_set\_color\_by\_t2g has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.

    \_text2hash(*color*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._text2hash)[¶](#manim.mobject.text.text_mobject.Text._text2hash "Link to this definition")
    :   Generates `sha256` hash for file name.

        Parameters:
        :   **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

    \_text2settings(*color*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._text2settings)[¶](#manim.mobject.text.text_mobject.Text._text2settings "Link to this definition")
    :   Converts the texts and styles to a setting for parsing.

        Parameters:
        :   **color** (*str*)

    \_text2svg(*color*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text._text2svg)[¶](#manim.mobject.text.text_mobject.Text._text2svg "Link to this definition")
    :   Convert the text to SVG using Pango.

        Parameters:
        :   **color** ([*ManimColor*](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"))

    init\_colors(*propagate\_colors=True*)[[source]](../_modules/manim/mobject/text/text_mobject.html#Text.init_colors)[¶](#manim.mobject.text.text_mobject.Text.init_colors "Link to this definition")
    :   Initializes the colors.

        Gets called upon creation. This is an empty method that can be implemented by
        subclasses.