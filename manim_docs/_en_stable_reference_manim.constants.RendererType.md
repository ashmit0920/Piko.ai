# Source: https://docs.manim.community/en/stable/reference/manim.constants.RendererType.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

RendererType[¶](#renderertype "Link to this heading")
=====================================================

Qualified name: `manim.constants.RendererType`

*class* RendererType(*value*, *names=<not given>*, *\*values*, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](../_modules/manim/constants.html#RendererType)[¶](#manim.constants.RendererType "Link to this definition")
:   Bases: `Enum`

    An enumeration of all renderer types that can be assigned to
    the `config.renderer` attribute.

    Manim’s configuration allows assigning string values to the renderer
    setting, the values are then replaced by the corresponding enum object.
    In other words, you can run:

    ```
    config.renderer = "opengl"

    ```

    and checking the renderer afterwards reveals that the attribute has
    assumed the value:

    ```
    <RendererType.OPENGL: 'opengl'>

    ```

    Attributes

    |  |  |
    | --- | --- |
    | [`CAIRO`](#manim.constants.RendererType.CAIRO "manim.constants.RendererType.CAIRO") | A renderer based on the cairo backend. |
    | [`OPENGL`](#manim.constants.RendererType.OPENGL "manim.constants.RendererType.OPENGL") | An OpenGL-based renderer. |

    CAIRO *= 'cairo'*[¶](#manim.constants.RendererType.CAIRO "Link to this definition")
    :   A renderer based on the cairo backend.

    OPENGL *= 'opengl'*[¶](#manim.constants.RendererType.OPENGL "Link to this definition")
    :   An OpenGL-based renderer.