# Source: https://docs.manim.community/en/stable/reference/manim.utils.commands.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

commands[¶](#module-manim.utils.commands "Link to this heading")
================================================================

Classes

|  |  |
| --- | --- |
| [`VideoMetadata`](manim.utils.commands.VideoMetadata.html#manim.utils.commands.VideoMetadata "manim.utils.commands.VideoMetadata") |  |

Functions

capture(*command*, *cwd=None*, *command\_input=None*)[[source]](../_modules/manim/utils/commands.html#capture)[¶](#manim.utils.commands.capture "Link to this definition")
:   Parameters:
    :   * **command** (*str*)
        * **cwd** ([*StrOrBytesPath*](manim.typing.html#manim.typing.StrOrBytesPath "manim.typing.StrOrBytesPath") *|* *None*)
        * **command\_input** (*str* *|* *None*)

    Return type:
    :   tuple[str, str, int]

get\_dir\_layout(*dirpath*)[[source]](../_modules/manim/utils/commands.html#get_dir_layout)[¶](#manim.utils.commands.get_dir_layout "Link to this definition")
:   Get list of paths relative to dirpath of all files in dir and subdirs recursively.

    Parameters:
    :   **dirpath** (*Path*)

    Return type:
    :   *Generator*[str, None, None]

get\_video\_metadata(*path\_to\_video*)[[source]](../_modules/manim/utils/commands.html#get_video_metadata)[¶](#manim.utils.commands.get_video_metadata "Link to this definition")
:   Parameters:
    :   **path\_to\_video** (*str* *|* *PathLike*)

    Return type:
    :   [*VideoMetadata*](manim.utils.commands.VideoMetadata.html#manim.utils.commands.VideoMetadata "manim.utils.commands.VideoMetadata")