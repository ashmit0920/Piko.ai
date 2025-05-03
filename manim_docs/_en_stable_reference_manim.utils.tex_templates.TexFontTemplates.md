# Source: https://docs.manim.community/en/stable/reference/manim.utils.tex_templates.TexFontTemplates.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

TexFontTemplates[¶](#texfonttemplates "Link to this heading")
=============================================================

Qualified name: `manim.utils.tex\_templates.TexFontTemplates`

*class* TexFontTemplates[[source]](../_modules/manim/utils/tex_templates.html#TexFontTemplates)[¶](#manim.utils.tex_templates.TexFontTemplates "Link to this definition")
:   Bases: `object`

    A collection of TeX templates for the fonts described at <http://jf.burnol.free.fr/showcase.html>

    These templates are specifically designed to allow you to typeset formulae and mathematics using
    different fonts. They are based on the mathastext LaTeX package.

    Examples

    Normal usage as a value for the keyword argument tex\_template of Tex() and MathTex() mobjects:

    ```
    ``Tex("My TeX code", tex_template=TexFontTemplates.comic_sans)``

    ```

    Notes

    Many of these templates require that specific fonts
    are installed on your local machine.
    For example, choosing the template TexFontTemplates.comic\_sans will
    not compile if the Comic Sans Microsoft font is not installed.

    To experiment, try to render the TexFontTemplateLibrary example scene:
    :   `manim path/to/manim/example_scenes/advanced_tex_fonts.py TexFontTemplateLibrary -p -ql`

    Methods

    Attributes

    |  |  |
    | --- | --- |
    | [`american_typewriter`](#manim.utils.tex_templates.TexFontTemplates.american_typewriter "manim.utils.tex_templates.TexFontTemplates.american_typewriter") | American Typewriter |
    | [`antykwa`](#manim.utils.tex_templates.TexFontTemplates.antykwa "manim.utils.tex_templates.TexFontTemplates.antykwa") | Antykwa Półtawskiego (TX Fonts for Greek and math symbols) |
    | [`apple_chancery`](#manim.utils.tex_templates.TexFontTemplates.apple_chancery "manim.utils.tex_templates.TexFontTemplates.apple_chancery") | Apple Chancery |
    | [`auriocus_kalligraphicus`](#manim.utils.tex_templates.TexFontTemplates.auriocus_kalligraphicus "manim.utils.tex_templates.TexFontTemplates.auriocus_kalligraphicus") | Auriocus Kalligraphicus (Symbol Greek) |
    | [`baskervald_adf_fourier`](#manim.utils.tex_templates.TexFontTemplates.baskervald_adf_fourier "manim.utils.tex_templates.TexFontTemplates.baskervald_adf_fourier") | Baskervald ADF with Fourier |
    | [`baskerville_it`](#manim.utils.tex_templates.TexFontTemplates.baskerville_it "manim.utils.tex_templates.TexFontTemplates.baskerville_it") | Baskerville (Italic) |
    | [`biolinum`](#manim.utils.tex_templates.TexFontTemplates.biolinum "manim.utils.tex_templates.TexFontTemplates.biolinum") | Biolinum |
    | [`brushscriptx`](#manim.utils.tex_templates.TexFontTemplates.brushscriptx "manim.utils.tex_templates.TexFontTemplates.brushscriptx") | BrushScriptX-Italic (PX math and Greek) |
    | [`chalkboard_se`](#manim.utils.tex_templates.TexFontTemplates.chalkboard_se "manim.utils.tex_templates.TexFontTemplates.chalkboard_se") | Chalkboard SE |
    | [`chalkduster`](#manim.utils.tex_templates.TexFontTemplates.chalkduster "manim.utils.tex_templates.TexFontTemplates.chalkduster") | Chalkduster |
    | [`comfortaa`](#manim.utils.tex_templates.TexFontTemplates.comfortaa "manim.utils.tex_templates.TexFontTemplates.comfortaa") | Comfortaa |
    | [`comic_sans`](#manim.utils.tex_templates.TexFontTemplates.comic_sans "manim.utils.tex_templates.TexFontTemplates.comic_sans") | Comic Sans MS |
    | [`droid_sans`](#manim.utils.tex_templates.TexFontTemplates.droid_sans "manim.utils.tex_templates.TexFontTemplates.droid_sans") | Droid Sans |
    | [`droid_sans_it`](#manim.utils.tex_templates.TexFontTemplates.droid_sans_it "manim.utils.tex_templates.TexFontTemplates.droid_sans_it") | Droid Sans (Italic) |
    | [`droid_serif`](#manim.utils.tex_templates.TexFontTemplates.droid_serif "manim.utils.tex_templates.TexFontTemplates.droid_serif") | Droid Serif |
    | [`droid_serif_px_it`](#manim.utils.tex_templates.TexFontTemplates.droid_serif_px_it "manim.utils.tex_templates.TexFontTemplates.droid_serif_px_it") | Droid Serif (PX math symbols) (Italic) |
    | [`ecf_augie`](#manim.utils.tex_templates.TexFontTemplates.ecf_augie "manim.utils.tex_templates.TexFontTemplates.ecf_augie") | ECF Augie (Euler Greek) |
    | [`ecf_jd`](#manim.utils.tex_templates.TexFontTemplates.ecf_jd "manim.utils.tex_templates.TexFontTemplates.ecf_jd") | ECF JD (with TX fonts) |
    | [`ecf_skeetch`](#manim.utils.tex_templates.TexFontTemplates.ecf_skeetch "manim.utils.tex_templates.TexFontTemplates.ecf_skeetch") | ECF Skeetch (CM Greek) |
    | [`ecf_tall_paul`](#manim.utils.tex_templates.TexFontTemplates.ecf_tall_paul "manim.utils.tex_templates.TexFontTemplates.ecf_tall_paul") | ECF Tall Paul (with Symbol font) |
    | [`ecf_webster`](#manim.utils.tex_templates.TexFontTemplates.ecf_webster "manim.utils.tex_templates.TexFontTemplates.ecf_webster") | ECF Webster (with TX fonts) |
    | [`electrum_adf`](#manim.utils.tex_templates.TexFontTemplates.electrum_adf "manim.utils.tex_templates.TexFontTemplates.electrum_adf") | Electrum ADF (CM Greek) |
    | [`epigrafica`](#manim.utils.tex_templates.TexFontTemplates.epigrafica "manim.utils.tex_templates.TexFontTemplates.epigrafica") | Epigrafica |
    | [`fourier_utopia`](#manim.utils.tex_templates.TexFontTemplates.fourier_utopia "manim.utils.tex_templates.TexFontTemplates.fourier_utopia") | Fourier Utopia (Fourier upright Greek) |
    | [`french_cursive`](#manim.utils.tex_templates.TexFontTemplates.french_cursive "manim.utils.tex_templates.TexFontTemplates.french_cursive") | French Cursive (Euler Greek) |
    | [`gfs_bodoni`](#manim.utils.tex_templates.TexFontTemplates.gfs_bodoni "manim.utils.tex_templates.TexFontTemplates.gfs_bodoni") | GFS Bodoni |
    | [`gfs_didot`](#manim.utils.tex_templates.TexFontTemplates.gfs_didot "manim.utils.tex_templates.TexFontTemplates.gfs_didot") | GFS Didot (Italic) |
    | [`gfs_neoHellenic`](#manim.utils.tex_templates.TexFontTemplates.gfs_neoHellenic "manim.utils.tex_templates.TexFontTemplates.gfs_neoHellenic") | GFS NeoHellenic |
    | [`gnu_freesans_tx`](#manim.utils.tex_templates.TexFontTemplates.gnu_freesans_tx "manim.utils.tex_templates.TexFontTemplates.gnu_freesans_tx") | GNU FreeSerif (and TX fonts symbols) |
    | [`gnu_freeserif_freesans`](#manim.utils.tex_templates.TexFontTemplates.gnu_freeserif_freesans "manim.utils.tex_templates.TexFontTemplates.gnu_freeserif_freesans") | GNU FreeSerif and FreeSans |
    | [`helvetica_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.helvetica_fourier_it "manim.utils.tex_templates.TexFontTemplates.helvetica_fourier_it") | Helvetica with Fourier (Italic) |
    | [`latin_modern_tw`](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw "manim.utils.tex_templates.TexFontTemplates.latin_modern_tw") | Latin Modern Typewriter Proportional |
    | [`latin_modern_tw_it`](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw_it "manim.utils.tex_templates.TexFontTemplates.latin_modern_tw_it") | Latin Modern Typewriter Proportional (CM Greek) (Italic) |
    | [`libertine`](#manim.utils.tex_templates.TexFontTemplates.libertine "manim.utils.tex_templates.TexFontTemplates.libertine") | Libertine |
    | [`libris_adf_fourier`](#manim.utils.tex_templates.TexFontTemplates.libris_adf_fourier "manim.utils.tex_templates.TexFontTemplates.libris_adf_fourier") | Libris ADF with Fourier |
    | [`minion_pro_myriad_pro`](#manim.utils.tex_templates.TexFontTemplates.minion_pro_myriad_pro "manim.utils.tex_templates.TexFontTemplates.minion_pro_myriad_pro") | Minion Pro and Myriad Pro (and TX fonts symbols) |
    | [`minion_pro_tx`](#manim.utils.tex_templates.TexFontTemplates.minion_pro_tx "manim.utils.tex_templates.TexFontTemplates.minion_pro_tx") | Minion Pro (and TX fonts symbols) |
    | [`new_century_schoolbook`](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook "manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook") | New Century Schoolbook (Symbol Greek) |
    | [`new_century_schoolbook_px`](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook_px "manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook_px") | New Century Schoolbook (Symbol Greek, PX math symbols) |
    | [`noteworthy_light`](#manim.utils.tex_templates.TexFontTemplates.noteworthy_light "manim.utils.tex_templates.TexFontTemplates.noteworthy_light") | Noteworthy Light |
    | [`palatino`](#manim.utils.tex_templates.TexFontTemplates.palatino "manim.utils.tex_templates.TexFontTemplates.palatino") | Palatino (Symbol Greek) |
    | [`papyrus`](#manim.utils.tex_templates.TexFontTemplates.papyrus "manim.utils.tex_templates.TexFontTemplates.papyrus") | Papyrus |
    | [`romande_adf_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.romande_adf_fourier_it "manim.utils.tex_templates.TexFontTemplates.romande_adf_fourier_it") | Romande ADF with Fourier (Italic) |
    | [`slitex`](#manim.utils.tex_templates.TexFontTemplates.slitex "manim.utils.tex_templates.TexFontTemplates.slitex") | SliTeX (Euler Greek) |
    | [`times_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.times_fourier_it "manim.utils.tex_templates.TexFontTemplates.times_fourier_it") | Times with Fourier (Italic) |
    | [`urw_avant_garde`](#manim.utils.tex_templates.TexFontTemplates.urw_avant_garde "manim.utils.tex_templates.TexFontTemplates.urw_avant_garde") | URW Avant Garde (Symbol Greek) |
    | [`urw_zapf_chancery`](#manim.utils.tex_templates.TexFontTemplates.urw_zapf_chancery "manim.utils.tex_templates.TexFontTemplates.urw_zapf_chancery") | URW Zapf Chancery (CM Greek) |
    | [`venturis_adf_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.venturis_adf_fourier_it "manim.utils.tex_templates.TexFontTemplates.venturis_adf_fourier_it") | Venturis ADF with Fourier (Italic) |
    | [`verdana_it`](#manim.utils.tex_templates.TexFontTemplates.verdana_it "manim.utils.tex_templates.TexFontTemplates.verdana_it") | Verdana (Italic) |
    | [`vollkorn`](#manim.utils.tex_templates.TexFontTemplates.vollkorn "manim.utils.tex_templates.TexFontTemplates.vollkorn") | Vollkorn (TX fonts for Greek and math symbols) |
    | [`vollkorn_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.vollkorn_fourier_it "manim.utils.tex_templates.TexFontTemplates.vollkorn_fourier_it") | Vollkorn with Fourier (Italic) |
    | [`zapf_chancery`](#manim.utils.tex_templates.TexFontTemplates.zapf_chancery "manim.utils.tex_templates.TexFontTemplates.zapf_chancery") | Zapf Chancery |

    american\_typewriter *= TexTemplate(\_body='', tex\_compiler='xelatex', description='American Typewriter', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{American Typewriter}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.american_typewriter "Link to this definition")
    :   American Typewriter

    antykwa *= TexTemplate(\_body='', tex\_compiler='latex', description='Antykwa Półtawskiego (TX Fonts for Greek and math symbols)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[OT4,OT1]{fontenc}\n\\usepackage{txfonts}\n\\usepackage[upright]{txgreeks}\n\\usepackage{antpolt}\n\\usepackage[defaultmathsizes,nolessnomore]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.antykwa "Link to this definition")
    :   Antykwa Półtawskiego (TX Fonts for Greek and math symbols)

    apple\_chancery *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Apple Chancery', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Apple Chancery}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.apple_chancery "Link to this definition")
    :   Apple Chancery

    auriocus\_kalligraphicus *= TexTemplate(\_body='', tex\_compiler='latex', description='Auriocus Kalligraphicus (Symbol Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{aurical}\n\\renewcommand{\\rmdefault}{AuriocusKalligraphicus}\n\\usepackage[symbolgreek]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.auriocus_kalligraphicus "Link to this definition")
    :   Auriocus Kalligraphicus (Symbol Greek)

    baskervald\_adf\_fourier *= TexTemplate(\_body='', tex\_compiler='latex', description='Baskervald ADF with Fourier', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[upright]{fourier}\n\\usepackage{baskervald}\n\\usepackage[defaultmathsizes,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.baskervald_adf_fourier "Link to this definition")
    :   Baskervald ADF with Fourier

    baskerville\_it *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Baskerville (Italic)', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Baskerville}\n\\usepackage[defaultmathsizes,italic]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.baskerville_it "Link to this definition")
    :   Baskerville (Italic)

    biolinum *= TexTemplate(\_body='', tex\_compiler='latex', description='Biolinum', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{libertine}\n\\renewcommand{\\familydefault}{\\sfdefault}\n\\usepackage[greek=n,biolinum]{libgreek}\n\\usepackage[noasterisk,defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.biolinum "Link to this definition")
    :   Biolinum

    brushscriptx *= TexTemplate(\_body='', tex\_compiler='xelatex', description='BrushScriptX-Italic (PX math and Greek)', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{pxfonts}\n%\\usepackage{pbsi}\n\\renewcommand{\\rmdefault}{pbsi}\n\\renewcommand{\\mddefault}{xl}\n\\renewcommand{\\bfdefault}{xl}\n\\usepackage[defaultmathsizes,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='\\boldmath\n')*[¶](#manim.utils.tex_templates.TexFontTemplates.brushscriptx "Link to this definition")
    :   BrushScriptX-Italic (PX math and Greek)

    chalkboard\_se *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Chalkboard SE', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Chalkboard SE}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.chalkboard_se "Link to this definition")
    :   Chalkboard SE

    chalkduster *= TexTemplate(\_body='', tex\_compiler='lualatex', description='Chalkduster', output\_format='.pdf', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Chalkduster}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.chalkduster "Link to this definition")
    :   Chalkduster

    comfortaa *= TexTemplate(\_body='', tex\_compiler='latex', description='Comfortaa', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[default]{comfortaa}\n\\usepackage[LGRgreek,defaultmathsizes,noasterisk]{mathastext}\n\\let\\varphi\\phi\n\\linespread{1.06}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.comfortaa "Link to this definition")
    :   Comfortaa

    comic\_sans *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Comic Sans MS', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Comic Sans MS}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.comic_sans "Link to this definition")
    :   Comic Sans MS

    droid\_sans *= TexTemplate(\_body='', tex\_compiler='latex', description='Droid Sans', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[default]{droidsans}\n\\usepackage[LGRgreek]{mathastext}\n\\let\\varepsilon\\epsilon\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.droid_sans "Link to this definition")
    :   Droid Sans

    droid\_sans\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Droid Sans (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[default]{droidsans}\n\\usepackage[LGRgreek,defaultmathsizes,italic]{mathastext}\n\\let\\varphi\\phi\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.droid_sans_it "Link to this definition")
    :   Droid Sans (Italic)

    droid\_serif *= TexTemplate(\_body='', tex\_compiler='latex', description='Droid Serif', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[default]{droidserif}\n\\usepackage[LGRgreek]{mathastext}\n\\let\\varepsilon\\epsilon\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.droid_serif "Link to this definition")
    :   Droid Serif

    droid\_serif\_px\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Droid Serif (PX math symbols) (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{pxfonts}\n\\usepackage[default]{droidserif}\n\\usepackage[LGRgreek,defaultmathsizes,italic,basic]{mathastext}\n\\let\\varphi\\phi\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.droid_serif_px_it "Link to this definition")
    :   Droid Serif (PX math symbols) (Italic)

    ecf\_augie *= TexTemplate(\_body='', tex\_compiler='latex', description='ECF Augie (Euler Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\renewcommand\\familydefault{fau} % emerald package\n\\usepackage[defaultmathsizes,eulergreek]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.ecf_augie "Link to this definition")
    :   ECF Augie (Euler Greek)

    ecf\_jd *= TexTemplate(\_body='', tex\_compiler='latex', description='ECF JD (with TX fonts)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{txfonts}\n\\usepackage[upright]{txgreeks}\n\\renewcommand\\familydefault{fjd} % emerald package\n\\usepackage{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='\\mathversion{bold}\n')*[¶](#manim.utils.tex_templates.TexFontTemplates.ecf_jd "Link to this definition")
    :   ECF JD (with TX fonts)

    ecf\_skeetch *= TexTemplate(\_body='', tex\_compiler='latex', description='ECF Skeetch (CM Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[T1]{fontenc}\n\\DeclareFontFamily{T1}{fsk}{}\n\\DeclareFontShape{T1}{fsk}{m}{n}{<->s\*[1.315] fskmw8t}{}\n\\renewcommand\\rmdefault{fsk}\n\\usepackage[noendash,defaultmathsizes,nohbar,defaultimath]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.ecf_skeetch "Link to this definition")
    :   ECF Skeetch (CM Greek)

    ecf\_tall\_paul *= TexTemplate(\_body='', tex\_compiler='latex', description='ECF Tall Paul (with Symbol font)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\DeclareFontFamily{T1}{ftp}{}\n\\DeclareFontShape{T1}{ftp}{m}{n}{\n    <->s\*[1.4] ftpmw8t\n}{} % increase size by factor 1.4\n\\renewcommand\\familydefault{ftp} % emerald package\n\\usepackage[symbol]{mathastext}\n\\let\\infty\\inftypsy\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.ecf_tall_paul "Link to this definition")
    :   ECF Tall Paul (with Symbol font)

    ecf\_webster *= TexTemplate(\_body='', tex\_compiler='latex', description='ECF Webster (with TX fonts)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{txfonts}\n\\usepackage[upright]{txgreeks}\n\\renewcommand\\familydefault{fwb} % emerald package\n\\usepackage{mathastext}\n\\renewcommand{\\int}{\\intop\\limits}\n\\linespread{1.5}\n', placeholder\_text='YourTextHere', post\_doc\_commands='\n\\mathversion{bold}\n')*[¶](#manim.utils.tex_templates.TexFontTemplates.ecf_webster "Link to this definition")
    :   ECF Webster (with TX fonts)

    electrum\_adf *= TexTemplate(\_body='', tex\_compiler='latex', description='Electrum ADF (CM Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[LGRgreek,basic,defaultmathsizes]{mathastext}\n\\usepackage[lf]{electrum}\n\\Mathastext\n\\let\\varphi\\phi\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.electrum_adf "Link to this definition")
    :   Electrum ADF (CM Greek)

    epigrafica *= TexTemplate(\_body='', tex\_compiler='latex', description='Epigrafica', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[LGR,OT1]{fontenc}\n\\usepackage{epigrafica}\n\\usepackage[basic,LGRgreek,defaultmathsizes]{mathastext}\n\\let\\varphi\\phi\n\\linespread{1.2}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.epigrafica "Link to this definition")
    :   Epigrafica

    fourier\_utopia *= TexTemplate(\_body='', tex\_compiler='latex', description='Fourier Utopia (Fourier upright Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[upright]{fourier}\n\\usepackage{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.fourier_utopia "Link to this definition")
    :   Fourier Utopia (Fourier upright Greek)

    french\_cursive *= TexTemplate(\_body='', tex\_compiler='latex', description='French Cursive (Euler Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[default]{frcursive}\n\\usepackage[eulergreek,noplusnominus,noequal,nohbar,%\nnolessnomore,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.french_cursive "Link to this definition")
    :   French Cursive (Euler Greek)

    gfs\_bodoni *= TexTemplate(\_body='', tex\_compiler='latex', description='GFS Bodoni', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\renewcommand{\\rmdefault}{bodoni}\n\\usepackage[LGRgreek]{mathastext}\n\\let\\varphi\\phi\n\\linespread{1.06}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.gfs_bodoni "Link to this definition")
    :   GFS Bodoni

    gfs\_didot *= TexTemplate(\_body='', tex\_compiler='latex', description='GFS Didot (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\renewcommand\\rmdefault{udidot}\n\\usepackage[LGRgreek,defaultmathsizes,italic]{mathastext}\n\\let\\varphi\\phi\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.gfs_didot "Link to this definition")
    :   GFS Didot (Italic)

    gfs\_neoHellenic *= TexTemplate(\_body='', tex\_compiler='latex', description='GFS NeoHellenic', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\renewcommand{\\rmdefault}{neohellenic}\n\\usepackage[LGRgreek]{mathastext}\n\\let\\varphi\\phi\n\\linespread{1.06}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.gfs_neoHellenic "Link to this definition")
    :   GFS NeoHellenic

    gnu\_freesans\_tx *= TexTemplate(\_body='', tex\_compiler='xelatex', description='GNU FreeSerif (and TX fonts symbols)', output\_format='.pdf', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\usepackage{txfonts}  %\\let\\mathbb=\\varmathbb\n\\setmainfont[ExternalLocation,\n                Mapping=tex-text,\n                BoldFont=FreeSerifBold,\n                ItalicFont=FreeSerifItalic,\n                BoldItalicFont=FreeSerifBoldItalic]{FreeSerif}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.gnu_freesans_tx "Link to this definition")
    :   GNU FreeSerif (and TX fonts symbols)

    gnu\_freeserif\_freesans *= TexTemplate(\_body='', tex\_compiler='xelatex', description='GNU FreeSerif and FreeSans', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble="\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[ExternalLocation,\n                Mapping=tex-text,\n                BoldFont=FreeSerifBold,\n                ItalicFont=FreeSerifItalic,\n                BoldItalicFont=FreeSerifBoldItalic]{FreeSerif}\n\\setsansfont[ExternalLocation,\n                Mapping=tex-text,\n                BoldFont=FreeSansBold,\n                ItalicFont=FreeSansOblique,\n                BoldItalicFont=FreeSansBoldOblique,\n                Scale=MatchLowercase]{FreeSans}\n\\renewcommand{\\familydefault}{lmss}\n\\usepackage[LGRgreek,defaultmathsizes,noasterisk]{mathastext}\n\\renewcommand{\\familydefault}{\\sfdefault}\n\\Mathastext\n\\let\\varphi\\phi % no `var' phi in LGR encoding\n\\renewcommand{\\familydefault}{\\rmdefault}\n", placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.gnu_freeserif_freesans "Link to this definition")
    :   GNU FreeSerif and FreeSans

    helvetica\_fourier\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Helvetica with Fourier (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[scaled]{helvet}\n\\usepackage{fourier}\n\\renewcommand{\\rmdefault}{phv}\n\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.helvetica_fourier_it "Link to this definition")
    :   Helvetica with Fourier (Italic)

    latin\_modern\_tw *= TexTemplate(\_body='', tex\_compiler='latex', description='Latin Modern Typewriter Proportional', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[variablett]{lmodern}\n\\renewcommand{\\rmdefault}{\\ttdefault}\n\\usepackage[LGRgreek]{mathastext}\n\\MTgreekfont{lmtt} % no lgr lmvtt, so use lgr lmtt\n\\Mathastext\n\\let\\varepsilon\\epsilon % only \\varsigma in LGR\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw "Link to this definition")
    :   Latin Modern Typewriter Proportional

    latin\_modern\_tw\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Latin Modern Typewriter Proportional (CM Greek) (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[variablett,nomath]{lmodern}\n\\renewcommand{\\familydefault}{\\ttdefault}\n\\usepackage[frenchmath]{mathastext}\n\\linespread{1.08}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw_it "Link to this definition")
    :   Latin Modern Typewriter Proportional (CM Greek) (Italic)

    libertine *= TexTemplate(\_body='', tex\_compiler='latex', description='Libertine', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{libertine}\n\\usepackage[greek=n]{libgreek}\n\\usepackage[noasterisk,defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.libertine "Link to this definition")
    :   Libertine

    libris\_adf\_fourier *= TexTemplate(\_body='', tex\_compiler='latex', description='Libris ADF with Fourier', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage[upright]{fourier}\n\\usepackage{libris}\n\\renewcommand{\\familydefault}{\\sfdefault}\n\\usepackage[noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.libris_adf_fourier "Link to this definition")
    :   Libris ADF with Fourier

    minion\_pro\_myriad\_pro *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Minion Pro and Myriad Pro (and TX fonts symbols)', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{txfonts}\n\\usepackage[upright]{txgreeks}\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Minion Pro}\n\\setsansfont[Mapping=tex-text,Scale=MatchUppercase]{Myriad Pro}\n\\renewcommand\\familydefault\\sfdefault\n\\usepackage[defaultmathsizes]{mathastext}\n\\renewcommand\\familydefault\\rmdefault\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.minion_pro_myriad_pro "Link to this definition")
    :   Minion Pro and Myriad Pro (and TX fonts symbols)

    minion\_pro\_tx *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Minion Pro (and TX fonts symbols)', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{txfonts}\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Minion Pro}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.minion_pro_tx "Link to this definition")
    :   Minion Pro (and TX fonts symbols)

    new\_century\_schoolbook *= TexTemplate(\_body='', tex\_compiler='latex', description='New Century Schoolbook (Symbol Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{newcent}\n\\usepackage[symbolgreek]{mathastext}\n\\linespread{1.1}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook "Link to this definition")
    :   New Century Schoolbook (Symbol Greek)

    new\_century\_schoolbook\_px *= TexTemplate(\_body='', tex\_compiler='latex', description='New Century Schoolbook (Symbol Greek, PX math symbols)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{pxfonts}\n\\usepackage{newcent}\n\\usepackage[symbolgreek,defaultmathsizes]{mathastext}\n\\linespread{1.06}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook_px "Link to this definition")
    :   New Century Schoolbook (Symbol Greek, PX math symbols)

    noteworthy\_light *= TexTemplate(\_body='', tex\_compiler='latex', description='Noteworthy Light', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Noteworthy Light}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.noteworthy_light "Link to this definition")
    :   Noteworthy Light

    palatino *= TexTemplate(\_body='', tex\_compiler='latex', description='Palatino (Symbol Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{palatino}\n\\usepackage[symbolmax,defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.palatino "Link to this definition")
    :   Palatino (Symbol Greek)

    papyrus *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Papyrus', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Papyrus}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.papyrus "Link to this definition")
    :   Papyrus

    romande\_adf\_fourier\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Romande ADF with Fourier (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{fourier}\n\\usepackage{romande}\n\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\n\\renewcommand{\\itshape}{\\swashstyle}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.romande_adf_fourier_it "Link to this definition")
    :   Romande ADF with Fourier (Italic)

    slitex *= TexTemplate(\_body='', tex\_compiler='latex', description='SliTeX (Euler Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{tpslifonts}\n\\usepackage[eulergreek,defaultmathsizes]{mathastext}\n\\MTEulerScale{1.06}\n\\linespread{1.2}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.slitex "Link to this definition")
    :   SliTeX (Euler Greek)

    times\_fourier\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Times with Fourier (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{fourier}\n\\renewcommand{\\rmdefault}{ptm}\n\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.times_fourier_it "Link to this definition")
    :   Times with Fourier (Italic)

    urw\_avant\_garde *= TexTemplate(\_body='', tex\_compiler='latex', description='URW Avant Garde (Symbol Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{avant}\n\\renewcommand{\\familydefault}{\\sfdefault}\n\\usepackage[symbolgreek,defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.urw_avant_garde "Link to this definition")
    :   URW Avant Garde (Symbol Greek)

    urw\_zapf\_chancery *= TexTemplate(\_body='', tex\_compiler='latex', description='URW Zapf Chancery (CM Greek)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\DeclareFontFamily{T1}{pzc}{}\n\\DeclareFontShape{T1}{pzc}{mb}{it}{<->s\*[1.2] pzcmi8t}{}\n\\DeclareFontShape{T1}{pzc}{m}{it}{<->ssub \* pzc/mb/it}{}\n\\DeclareFontShape{T1}{pzc}{mb}{sl}{<->ssub \* pzc/mb/it}{}\n\\DeclareFontShape{T1}{pzc}{m}{sl}{<->ssub \* pzc/mb/sl}{}\n\\DeclareFontShape{T1}{pzc}{m}{n}{<->ssub \* pzc/mb/it}{}\n\\usepackage{chancery}\n\\usepackage{mathastext}\n\\linespread{1.05}', placeholder\_text='YourTextHere', post\_doc\_commands='\n\\boldmath\n')*[¶](#manim.utils.tex_templates.TexFontTemplates.urw_zapf_chancery "Link to this definition")
    :   URW Zapf Chancery (CM Greek)

    venturis\_adf\_fourier\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Venturis ADF with Fourier (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{fourier}\n\\usepackage[lf]{venturis}\n\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.venturis_adf_fourier_it "Link to this definition")
    :   Venturis ADF with Fourier (Italic)

    verdana\_it *= TexTemplate(\_body='', tex\_compiler='xelatex', description='Verdana (Italic)', output\_format='.xdv', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[no-math]{fontspec}\n\\setmainfont[Mapping=tex-text]{Verdana}\n\\usepackage[defaultmathsizes,italic]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.verdana_it "Link to this definition")
    :   Verdana (Italic)

    vollkorn *= TexTemplate(\_body='', tex\_compiler='latex', description='Vollkorn (TX fonts for Greek and math symbols)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage[T1]{fontenc}\n\\usepackage{txfonts}\n\\usepackage[upright]{txgreeks}\n\\usepackage{vollkorn}\n\\usepackage[defaultmathsizes]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.vollkorn "Link to this definition")
    :   Vollkorn (TX fonts for Greek and math symbols)

    vollkorn\_fourier\_it *= TexTemplate(\_body='', tex\_compiler='latex', description='Vollkorn with Fourier (Italic)', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\usepackage{fourier}\n\\usepackage{vollkorn}\n\\usepackage[italic,nohbar]{mathastext}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.vollkorn_fourier_it "Link to this definition")
    :   Vollkorn with Fourier (Italic)

    zapf\_chancery *= TexTemplate(\_body='', tex\_compiler='latex', description='Zapf Chancery', output\_format='.dvi', documentclass='\\documentclass[preview]{standalone}', preamble='\n\\usepackage[english]{babel}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\n\n\\DeclareFontFamily{T1}{pzc}{}\n\\DeclareFontShape{T1}{pzc}{mb}{it}{<->s\*[1.2] pzcmi8t}{}\n\\DeclareFontShape{T1}{pzc}{m}{it}{<->ssub \* pzc/mb/it}{}\n\\usepackage{chancery} % = \\renewcommand{\\rmdefault}{pzc}\n\\renewcommand\\shapedefault\\itdefault\n\\renewcommand\\bfdefault\\mddefault\n\\usepackage[defaultmathsizes]{mathastext}\n\\linespread{1.05}\n', placeholder\_text='YourTextHere', post\_doc\_commands='')*[¶](#manim.utils.tex_templates.TexFontTemplates.zapf_chancery "Link to this definition")
    :   Zapf Chancery