# Source: https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

JSONFormatter[¶](#jsonformatter "Link to this heading")
=======================================================

Qualified name: `manim.\_config.logger\_utils.JSONFormatter`

*class* JSONFormatter(*fmt=None*, *datefmt=None*, *style='%'*, *validate=True*, *\**, *defaults=None*)[[source]](../_modules/manim/_config/logger_utils.html#JSONFormatter)[¶](#manim._config.logger_utils.JSONFormatter "Link to this definition")
:   Bases: `Formatter`

    A formatter that outputs logs in a custom JSON format.

    This class is used internally for testing purposes.

    Initialize the formatter with specified format strings.

    Initialize the formatter either with the specified format string, or a
    default as described above. Allow for specialized date formatting with
    the optional datefmt argument. If datefmt is omitted, you get an
    ISO8601-like (or RFC 3339-like) format.

    Use a style parameter of ‘%’, ‘{’ or ‘$’ to specify that you want to
    use one of %-formatting, `str.format()` (`{}`) formatting or
    `string.Template` formatting in your format string.

    Changed in version 3.2: Added the `style` parameter.

    Methods

    |  |  |
    | --- | --- |
    | [`format`](#manim._config.logger_utils.JSONFormatter.format "manim._config.logger_utils.JSONFormatter.format") | Format the record in a custom JSON format. |

    Attributes

    |  |  |
    | --- | --- |
    | `default_msec_format` |  |
    | `default_time_format` |  |

    format(*record*)[[source]](../_modules/manim/_config/logger_utils.html#JSONFormatter.format)[¶](#manim._config.logger_utils.JSONFormatter.format "Link to this definition")
    :   Format the record in a custom JSON format.

        Parameters:
        :   **record** (*LogRecord*)

        Return type:
        :   str