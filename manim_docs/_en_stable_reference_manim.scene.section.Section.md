# Source: https://docs.manim.community/en/stable/reference/manim.scene.section.Section.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

Section[¶](#section "Link to this heading")
===========================================

Qualified name: `manim.scene.section.Section`

*class* Section(*type\_*, *video*, *name*, *skip\_animations*)[[source]](../_modules/manim/scene/section.html#Section)[¶](#manim.scene.section.Section "Link to this definition")
:   Bases: `object`

    A [`Scene`](manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene") can be segmented into multiple Sections.
    Refer to [the documentation](../tutorials/output_and_config.html) for more info.
    It consists of multiple animations.

    Parameters:
    :   * **type\_** (*str*)
        * **video** (*str* *|* *None*)
        * **name** (*str*)
        * **skip\_animations** (*bool*)

    type\\_
    :   Can be used by a third party applications to classify different types of sections.

    video[¶](#manim.scene.section.Section.video "Link to this definition")
    :   Path to video file with animations belonging to section relative to sections directory.
        If `None`, then the section will not be saved.

    name[¶](#manim.scene.section.Section.name "Link to this definition")
    :   Human readable, non-unique name for this section.

    skip\_animations[¶](#manim.scene.section.Section.skip_animations "Link to this definition")
    :   Skip rendering the animations in this section when `True`.

    partial\_movie\_files[¶](#manim.scene.section.Section.partial_movie_files "Link to this definition")
    :   Animations belonging to this section.

    See also

    [`DefaultSectionType`](manim.scene.section.DefaultSectionType.html#manim.scene.section.DefaultSectionType "manim.scene.section.DefaultSectionType"), `CairoRenderer.update_skipping_status()`, `OpenGLRenderer.update_skipping_status()`

    Methods

    |  |  |
    | --- | --- |
    | [`get_clean_partial_movie_files`](#manim.scene.section.Section.get_clean_partial_movie_files "manim.scene.section.Section.get_clean_partial_movie_files") | Return all partial movie files that are not `None`. |
    | [`get_dict`](#manim.scene.section.Section.get_dict "manim.scene.section.Section.get_dict") | Get dictionary representation with metadata of output video. |
    | [`is_empty`](#manim.scene.section.Section.is_empty "manim.scene.section.Section.is_empty") | Check whether this section is empty. |

    get\_clean\_partial\_movie\_files()[[source]](../_modules/manim/scene/section.html#Section.get_clean_partial_movie_files)[¶](#manim.scene.section.Section.get_clean_partial_movie_files "Link to this definition")
    :   Return all partial movie files that are not `None`.

        Return type:
        :   list[str]

    get\_dict(*sections\_dir*)[[source]](../_modules/manim/scene/section.html#Section.get_dict)[¶](#manim.scene.section.Section.get_dict "Link to this definition")
    :   Get dictionary representation with metadata of output video.

        The output from this function is used from every section to build the sections index file.
        The output video must have been created in the `sections_dir` before executing this method.
        This is the main part of the Segmented Video API.

        Parameters:
        :   **sections\_dir** (*Path*)

        Return type:
        :   dict[str, *Any*]

    is\_empty()[[source]](../_modules/manim/scene/section.html#Section.is_empty)[¶](#manim.scene.section.Section.is_empty "Link to this definition")
    :   Check whether this section is empty.

        Note that animations represented by `None` are also counted.

        Return type:
        :   bool