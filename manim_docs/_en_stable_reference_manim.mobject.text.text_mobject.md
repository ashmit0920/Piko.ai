# Source: https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

text\_mobject[¶](#module-manim.mobject.text.text_mobject "Link to this heading")
================================================================================

Mobjects used for displaying (non-LaTeX) text.

Note

Just as you can use [`Tex`](manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex "manim.mobject.text.tex_mobject.Tex") and [`MathTex`](manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex "manim.mobject.text.tex_mobject.MathTex") (from the module [`tex_mobject`](manim.mobject.text.tex_mobject.html#module-manim.mobject.text.tex_mobject "manim.mobject.text.tex_mobject"))
to insert LaTeX to your videos, you can use [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") to to add normal text.

Important

See the corresponding tutorial [Text Without LaTeX](../guides/using_text.html#using-text-objects), especially for information about fonts.

The simplest way to add text to your animations is to use the [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") class. It uses the Pango library to render text.
With Pango, you are also able to render non-English alphabets like 你好 or こんにちは or 안녕하세요 or مرحبا بالعالم.

Examples

Example: HelloWorld [¶](#helloworld)

![../_images/HelloWorld-2.png](../_images/HelloWorld-2.png)

```
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)

```

```

class HelloWorld(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)


```

Example: TextAlignment [¶](#textalignment)

![../_images/TextAlignment-1.png](../_images/TextAlignment-1.png)

```
from manim import *

class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)

        t2 = Text("2. Clustering").set_color(WHITE)

        t3 = Text("3. Regression").set_color(WHITE)

        t4 = Text("4. Prediction").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)

```

```

class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)

        t2 = Text("2. Clustering").set_color(WHITE)

        t3 = Text("3. Regression").set_color(WHITE)

        t4 = Text("4. Prediction").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)


```

Classes

|  |  |
| --- | --- |
| [`MarkupText`](manim.mobject.text.text_mobject.MarkupText.html#manim.mobject.text.text_mobject.MarkupText "manim.mobject.text.text_mobject.MarkupText") | Display (non-LaTeX) text rendered using [Pango](https://pango.gnome.org/). |
| [`Paragraph`](manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") | Display a paragraph of text. |
| [`Text`](manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") |  |

Functions

register\_font(*font\_file*)[[source]](../_modules/manim/mobject/text/text_mobject.html#register_font)[¶](#manim.mobject.text.text_mobject.register_font "Link to this definition")
:   Temporarily add a font file to Pango’s search path.

    This searches for the font\_file at various places. The order it searches it described below.

    1. Absolute path.
    2. In `assets/fonts` folder.
    3. In `font/` folder.
    4. In the same directory.

    Parameters:
    :   **font\_file** (*str* *|* *Path*) – The font file to add.

    Examples

    Use `with register_font(...)` to add a font file to search
    path.

    ```
    with register_font("path/to/font_file.ttf"):
        a = Text("Hello", font="Custom Font Name")

    ```

    Raises:
    :   * **FileNotFoundError:** – If the font doesn’t exists.
        * **AttributeError:** – If this method is used on macOS.
        * **.. important ::** – This method is available for macOS for `ManimPango>=v0.2.3`. Using this
          method with previous releases will raise an `AttributeError` on macOS.

    Parameters:
    :   **font\_file** (*str* *|* *Path*)

remove\_invisible\_chars(*mobject*)[[source]](../_modules/manim/mobject/text/text_mobject.html#remove_invisible_chars)[¶](#manim.mobject.text.text_mobject.remove_invisible_chars "Link to this definition")
:   Function to remove unwanted invisible characters from some mobjects.

    Parameters:
    :   **mobject** ([*SVGMobject*](manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")) – Any SVGMobject from which we want to remove unwanted invisible characters.

    Returns:
    :   The SVGMobject without unwanted invisible characters.

    Return type:
    :   [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject "manim.mobject.svg.svg_mobject.SVGMobject")