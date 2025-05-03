# Source: https://docs.manim.community/en/stable/reference/manim.mobject.svg.svg_mobject.SVGMobject.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

SVGMobject[¶](#svgmobject "Link to this heading")
=================================================

Qualified name: `manim.mobject.svg.svg\_mobject.SVGMobject`

*class* SVGMobject(*file\_name=None*, *should\_center=True*, *height=2*, *width=None*, *color=None*, *opacity=None*, *fill\_color=None*, *fill\_opacity=None*, *stroke\_color=None*, *stroke\_opacity=None*, *stroke\_width=None*, *svg\_default=None*, *path\_string\_config=None*, *use\_svg\_cache=True*, *\*\*kwargs*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject "Link to this definition")
:   Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    A vectorized mobject created from importing an SVG file.

    Parameters:
    :   * **file\_name** (*str* *|* *os.PathLike* *|* *None*) – The path to the SVG file.
        * **should\_center** (*bool*) – Whether or not the mobject should be centered after
          being imported.
        * **height** (*float* *|* *None*) – The target height of the mobject, set to 2 Manim units by default.
          If the height and width are both set to `None`, the mobject
          is imported without being scaled.
        * **width** (*float* *|* *None*) – The target width of the mobject, set to `None` by default. If
          the height and the width are both set to `None`, the mobject
          is imported without being scaled.
        * **color** (*str* *|* *None*) – The color (both fill and stroke color) of the mobject. If
          `None` (the default), the colors set in the SVG file
          are used.
        * **opacity** (*float* *|* *None*) – The opacity (both fill and stroke opacity) of the mobject.
          If `None` (the default), the opacity set in the SVG file
          is used.
        * **fill\_color** (*str* *|* *None*) – The fill color of the mobject. If `None` (the default),
          the fill colors set in the SVG file are used.
        * **fill\_opacity** (*float* *|* *None*) – The fill opacity of the mobject. If `None` (the default),
          the fill opacities set in the SVG file are used.
        * **stroke\_color** (*str* *|* *None*) – The stroke color of the mobject. If `None` (the default),
          the stroke colors set in the SVG file are used.
        * **stroke\_opacity** (*float* *|* *None*) – The stroke opacity of the mobject. If `None` (the default),
          the stroke opacities set in the SVG file are used.
        * **stroke\_width** (*float* *|* *None*) – The stroke width of the mobject. If `None` (the default),
          the stroke width values set in the SVG file are used.
        * **svg\_default** (*dict* *|* *None*) – A dictionary in which fallback values for unspecified
          properties of elements in the SVG file are defined. If
          `None` (the default), `color`, `opacity`, `fill_color`
          `fill_opacity`, `stroke_color`, and `stroke_opacity`
          are set to `None`, and `stroke_width` is set to 0.
        * **path\_string\_config** (*dict* *|* *None*) – A dictionary with keyword arguments passed to
          [`VMobjectFromSVGPath`](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath") used for importing path elements.
          If `None` (the default), no additional arguments are passed.
        * **use\_svg\_cache** (*bool*) – If True (default), the svg inputs (e.g. file\_name, settings)
          will be used as a key and a copy of the created mobject will
          be saved using that key to be quickly retrieved if the same
          inputs need be processed later. For large SVGs which are used
          only once, this can be omitted to improve performance.
        * **kwargs** – Further arguments passed to the parent class.

    Methods

    |  |  |
    | --- | --- |
    | [`apply_style_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject") | Apply SVG style information to the converted mobject. |
    | [`ellipse_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject") | Convert an ellipse or circle element to a vectorized mobject. |
    | [`generate_config_style_dict`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict "manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict") | Generate a dictionary holding the default style information. |
    | [`generate_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject "manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject") | Parse the SVG and translate its elements to submobjects. |
    | [`get_file_path`](#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path "manim.mobject.svg.svg_mobject.SVGMobject.get_file_path") | Search for an existing file based on the specified file name. |
    | [`get_mobjects_from`](#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from "manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from") | Convert the elements of the SVG to a list of mobjects. |
    | [`handle_transform`](#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform "manim.mobject.svg.svg_mobject.SVGMobject.handle_transform") | Apply SVG transformations to the converted mobject. |
    | [`init_svg_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject "manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject") | Checks whether the SVG has already been imported and generates it if not. |
    | [`line_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject") | Convert a line element to a vectorized mobject. |
    | [`modify_xml_tree`](#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree "manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree") | Modifies the SVG element tree to include default style information. |
    | [`move_into_position`](#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position "manim.mobject.svg.svg_mobject.SVGMobject.move_into_position") | Scale and move the generated mobject into position. |
    | [`path_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject") | Convert a path element to a vectorized mobject. |
    | [`polygon_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject") | Convert a polygon element to a vectorized mobject. |
    | [`polyline_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject") | Convert a polyline element to a vectorized mobject. |
    | [`rect_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject") | Convert a rectangle element to a vectorized mobject. |
    | [`text_to_mobject`](#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject "manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject") | Convert a text element to a vectorized mobject. |

    Attributes

    |  |  |
    | --- | --- |
    | `animate` | Used to animate the application of any method of `self`. |
    | `animation_overrides` |  |
    | `color` |  |
    | `depth` | The depth of the mobject. |
    | `fill_color` | If there are multiple colors (for gradient) this returns the first one |
    | [`hash_seed`](#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed "manim.mobject.svg.svg_mobject.SVGMobject.hash_seed") | A unique hash representing the result of the generated mobject points. |
    | `height` | The height of the mobject. |
    | `n_points_per_curve` |  |
    | `sheen_factor` |  |
    | `stroke_color` |  |
    | `width` | The width of the mobject. |

    \_original\_\_init\_\_(*file\_name=None*, *should\_center=True*, *height=2*, *width=None*, *color=None*, *opacity=None*, *fill\_color=None*, *fill\_opacity=None*, *stroke\_color=None*, *stroke\_opacity=None*, *stroke\_width=None*, *svg\_default=None*, *path\_string\_config=None*, *use\_svg\_cache=True*, *\*\*kwargs*)[¶](#manim.mobject.svg.svg_mobject.SVGMobject._original__init__ "Link to this definition")
    :   Initialize self. See help(type(self)) for accurate signature.

        Parameters:
        :   * **file\_name** (*str* *|* *PathLike* *|* *None*)
            * **should\_center** (*bool*)
            * **height** (*float* *|* *None*)
            * **width** (*float* *|* *None*)
            * **color** (*str* *|* *None*)
            * **opacity** (*float* *|* *None*)
            * **fill\_color** (*str* *|* *None*)
            * **fill\_opacity** (*float* *|* *None*)
            * **stroke\_color** (*str* *|* *None*)
            * **stroke\_opacity** (*float* *|* *None*)
            * **stroke\_width** (*float* *|* *None*)
            * **svg\_default** (*dict* *|* *None*)
            * **path\_string\_config** (*dict* *|* *None*)
            * **use\_svg\_cache** (*bool*)

    *static* apply\_style\_to\_mobject(*mob*, *shape*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.apply_style_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.apply_style_to_mobject "Link to this definition")
    :   Apply SVG style information to the converted mobject.

        Parameters:
        :   * **mob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The converted mobject.
            * **shape** (*GraphicObject*) – The parsed SVG element.

        Return type:
        :   [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    *static* ellipse\_to\_mobject(*ellipse*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.ellipse_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.ellipse_to_mobject "Link to this definition")
    :   Convert an ellipse or circle element to a vectorized mobject.

        Parameters:
        :   **ellipse** (*Ellipse* *|* *Circle*) – The parsed SVG ellipse or circle.

        Return type:
        :   [*Circle*](manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle "manim.mobject.geometry.arc.Circle")

    generate\_config\_style\_dict()[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.generate_config_style_dict)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.generate_config_style_dict "Link to this definition")
    :   Generate a dictionary holding the default style information.

        Return type:
        :   dict[str, str]

    generate\_mobject()[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.generate_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject "Link to this definition")
    :   Parse the SVG and translate its elements to submobjects.

        Return type:
        :   None

    get\_file\_path()[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.get_file_path)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.get_file_path "Link to this definition")
    :   Search for an existing file based on the specified file name.

        Return type:
        :   *Path*

    get\_mobjects\_from(*svg*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.get_mobjects_from)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.get_mobjects_from "Link to this definition")
    :   Convert the elements of the SVG to a list of mobjects.

        Parameters:
        :   **svg** (*SVG*) – The parsed SVG file.

        Return type:
        :   list[[*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")]

    *static* handle\_transform(*mob*, *matrix*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.handle_transform)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.handle_transform "Link to this definition")
    :   Apply SVG transformations to the converted mobject.

        Parameters:
        :   * **mob** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The converted mobject.
            * **matrix** (*Matrix*) – The transformation matrix determined from the SVG
              transformation.

        Return type:
        :   [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    *property* hash\_seed*: tuple*[¶](#manim.mobject.svg.svg_mobject.SVGMobject.hash_seed "Link to this definition")
    :   A unique hash representing the result of the generated
        mobject points.

        Used as keys in the `SVG_HASH_TO_MOB_MAP` caching dictionary.

    init\_svg\_mobject(*use\_svg\_cache*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.init_svg_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.init_svg_mobject "Link to this definition")
    :   Checks whether the SVG has already been imported and
        generates it if not.

        See also

        [`SVGMobject.generate_mobject()`](#manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject "manim.mobject.svg.svg_mobject.SVGMobject.generate_mobject")

        Parameters:
        :   **use\_svg\_cache** (*bool*)

        Return type:
        :   None

    *static* line\_to\_mobject(*line*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.line_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.line_to_mobject "Link to this definition")
    :   Convert a line element to a vectorized mobject.

        Parameters:
        :   **line** (*Line*) – The parsed SVG line.

        Return type:
        :   [*Line*](manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line "manim.mobject.geometry.line.Line")

    modify\_xml\_tree(*element\_tree*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.modify_xml_tree)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.modify_xml_tree "Link to this definition")
    :   Modifies the SVG element tree to include default
        style information.

        Parameters:
        :   **element\_tree** (*ElementTree*) – The parsed element tree from the SVG file.

        Return type:
        :   *ElementTree*

    move\_into\_position()[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.move_into_position)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.move_into_position "Link to this definition")
    :   Scale and move the generated mobject into position.

        Return type:
        :   None

    path\_to\_mobject(*path*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.path_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.path_to_mobject "Link to this definition")
    :   Convert a path element to a vectorized mobject.

        Parameters:
        :   **path** (*Path*) – The parsed SVG path.

        Return type:
        :   [*VMobjectFromSVGPath*](manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath")

    *static* polygon\_to\_mobject(*polygon*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.polygon_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.polygon_to_mobject "Link to this definition")
    :   Convert a polygon element to a vectorized mobject.

        Parameters:
        :   **polygon** (*Polygon*) – The parsed SVG polygon.

        Return type:
        :   [*Polygon*](manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon "manim.mobject.geometry.polygram.Polygon")

    polyline\_to\_mobject(*polyline*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.polyline_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.polyline_to_mobject "Link to this definition")
    :   Convert a polyline element to a vectorized mobject.

        Parameters:
        :   **polyline** (*Polyline*) – The parsed SVG polyline.

        Return type:
        :   [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

    *static* rect\_to\_mobject(*rect*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.rect_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.rect_to_mobject "Link to this definition")
    :   Convert a rectangle element to a vectorized mobject.

        Parameters:
        :   **rect** (*Rect*) – The parsed SVG rectangle.

        Return type:
        :   [*Rectangle*](manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle "manim.mobject.geometry.polygram.Rectangle")

    *static* text\_to\_mobject(*text*)[[source]](../_modules/manim/mobject/svg/svg_mobject.html#SVGMobject.text_to_mobject)[¶](#manim.mobject.svg.svg_mobject.SVGMobject.text_to_mobject "Link to this definition")
    :   Convert a text element to a vectorized mobject.

        Warning

        Not yet implemented.

        Parameters:
        :   **text** (*Text*) – The parsed SVG text.