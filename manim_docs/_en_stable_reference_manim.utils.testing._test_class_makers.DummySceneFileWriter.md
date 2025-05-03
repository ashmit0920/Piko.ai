# Source: https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

DummySceneFileWriter[¶](#dummyscenefilewriter "Link to this heading")
=====================================================================

Qualified name: `manim.utils.testing.\_test\_class\_makers.DummySceneFileWriter`

*class* DummySceneFileWriter(*renderer*, *scene\_name*, *\*\*kwargs*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter "Link to this definition")
:   Bases: [`SceneFileWriter`](manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter")

    Delegate of SceneFileWriter used to test the frames.

    Methods

    |  |  |
    | --- | --- |
    | [`add_partial_movie_file`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file "manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file") | Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash. |
    | [`begin_animation`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation "manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation") | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file. |
    | [`clean_cache`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache "manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache") | Will clean the cache by removing the oldest partial\_movie\_files. |
    | [`combine_to_movie`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie "manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie") | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
    | [`combine_to_section_videos`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos "manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos") | Concatenate partial movie files for each section. |
    | [`end_animation`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation "manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation") | Internally used by Manim to stop streaming to FFMPEG gracefully. |
    | [`init_output_directories`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories "manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories") | Initialise output directories. |
    | [`write_frame`](#manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame "manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame") | Used internally by Manim to write a frame to the FFMPEG input buffer. |

    Attributes

    |  |  |
    | --- | --- |
    | `force_output_as_scene_name` |  |

    Parameters:
    :   * **renderer** (*CairoRenderer* *|* *OpenGLRenderer*)
        * **scene\_name** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))
        * **kwargs** (*Any*)

    add\_partial\_movie\_file(*hash\_animation*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.add_partial_movie_file)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file "Link to this definition")
    :   Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash.
        This method will compute the path from the hash. In addition to that it adds the new animation to the current section.

        Parameters:
        :   **hash\_animation** (*str*) – Hash of the animation.

        Return type:
        :   None

    begin\_animation(*allow\_write=True*, *file\_path=None*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.begin_animation)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation "Link to this definition")
    :   Used internally by manim to stream the animation to FFMPEG for
        displaying or writing to a file.

        Parameters:
        :   * **allow\_write** (*bool*) – Whether or not to write to a video file.
            * **file\_path** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") *|* *None*)

        Return type:
        :   Any

    clean\_cache()[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.clean_cache)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache "Link to this definition")
    :   Will clean the cache by removing the oldest partial\_movie\_files.

        Return type:
        :   None

    combine\_to\_movie()[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.combine_to_movie)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie "Link to this definition")
    :   Used internally by Manim to combine the separate
        partial movie files that make up a Scene into a single
        video file for that Scene.

        Return type:
        :   None

    combine\_to\_section\_videos()[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.combine_to_section_videos)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos "Link to this definition")
    :   Concatenate partial movie files for each section.

        Return type:
        :   None

    end\_animation(*allow\_write=False*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.end_animation)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation "Link to this definition")
    :   Internally used by Manim to stop streaming to
        FFMPEG gracefully.

        Parameters:
        :   **allow\_write** (*bool*) – Whether or not to write to a video file.

        Return type:
        :   None

    init\_output\_directories(*scene\_name*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.init_output_directories)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories "Link to this definition")
    :   Initialise output directories.

        Notes

        The directories are read from `config`, for example
        `config['media_dir']`. If the target directories don’t already
        exist, they will be created.

        Parameters:
        :   **scene\_name** ([*StrPath*](manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

        Return type:
        :   None

    write\_frame(*frame\_or\_renderer*, *num\_frames=1*)[[source]](../_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.write_frame)[¶](#manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame "Link to this definition")
    :   Used internally by Manim to write a frame to
        the FFMPEG input buffer.

        Parameters:
        :   * **frame\_or\_renderer** ([*PixelArray*](manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray") *|* *OpenGLRenderer*) – Pixel array of the frame.
            * **num\_frames** (*int*) – The number of times to write frame.

        Return type:
        :   None