# Source: https://docs.manim.community/en/stable/reference/manim.typing.html

[Back to top](#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

typing[¶](#module-manim.typing "Link to this heading")
======================================================

Custom type definitions used in Manim.

Note for developers

Around the source code there are multiple strings which look like this:

```
'''
[CATEGORY]
<category_name>
'''

```

All type aliases defined under those strings will be automatically
classified under that category.

If you need to define a new category, respect the format described above.

Type Aliases

### Primitive data types[¶](#primitive_data_types "Link to this heading")

*class* ManimFloat[¶](#manim.typing.ManimFloat "Link to this definition")
:   ```
    np.float64

    ```

    A double-precision floating-point value (64 bits, or 8 bytes),
    according to the IEEE 754 standard.

*class* ManimInt[¶](#manim.typing.ManimInt "Link to this definition")
:   ```
    np.int64

    ```

    A long integer (64 bits, or 8 bytes).

    It can take values between \(-2^{63}\) and \(+2^{63} - 1\),
    which expressed in base 10 is a range between around
    \(-9.223 \cdot 10^{18}\) and \(+9.223 \cdot 10^{18}\).

### Color types[¶](#color_types "Link to this heading")

*class* ManimColorDType[¶](#manim.typing.ManimColorDType "Link to this definition")
:   ```
    ManimFloat
    ```

    Data type used in [`ManimColorInternal`](#manim.typing.ManimColorInternal "manim.typing.ManimColorInternal"): a
    double-precision float between 0 and 1.

*class* RGB\_Array\_Float[¶](#manim.typing.RGB_Array_Float "Link to this definition")
:   ```
    NDArray[ManimColorDType]
    ```

    `shape: (3,)`

    A `numpy.ndarray` of 3 floats between 0 and 1, representing a
    color in RGB format.

    Its components describe, in order, the intensity of Red, Green, and
    Blue in the represented color.

*class* RGB\_Tuple\_Float[¶](#manim.typing.RGB_Tuple_Float "Link to this definition")
:   ```
    tuple[float, float, float]

    ```

    `shape: (3,)`

    A tuple of 3 floats between 0 and 1, representing a color in RGB
    format.

    Its components describe, in order, the intensity of Red, Green, and
    Blue in the represented color.

*class* RGB\_Array\_Int[¶](#manim.typing.RGB_Array_Int "Link to this definition")
:   ```
    NDArray[ManimInt]
    ```

    `shape: (3,)`

    A `numpy.ndarray` of 3 integers between 0 and 255,
    representing a color in RGB format.

    Its components describe, in order, the intensity of Red, Green, and
    Blue in the represented color.

*class* RGB\_Tuple\_Int[¶](#manim.typing.RGB_Tuple_Int "Link to this definition")
:   ```
    tuple[int, int, int]

    ```

    `shape: (3,)`

    A tuple of 3 integers between 0 and 255, representing a color in RGB
    format.

    Its components describe, in order, the intensity of Red, Green, and
    Blue in the represented color.

*class* RGBA\_Array\_Float[¶](#manim.typing.RGBA_Array_Float "Link to this definition")
:   ```
    NDArray[ManimColorDType]
    ```

    `shape: (4,)`

    A `numpy.ndarray` of 4 floats between 0 and 1, representing a
    color in RGBA format.

    Its components describe, in order, the intensity of Red, Green, Blue
    and Alpha (opacity) in the represented color.

*class* RGBA\_Tuple\_Float[¶](#manim.typing.RGBA_Tuple_Float "Link to this definition")
:   ```
    tuple[float, float, float, float]

    ```

    `shape: (4,)`

    A tuple of 4 floats between 0 and 1, representing a color in RGBA
    format.

    Its components describe, in order, the intensity of Red, Green, Blue
    and Alpha (opacity) in the represented color.

*class* RGBA\_Array\_Int[¶](#manim.typing.RGBA_Array_Int "Link to this definition")
:   ```
    NDArray[ManimInt]
    ```

    `shape: (4,)`

    A `numpy.ndarray` of 4 integers between 0 and 255,
    representing a color in RGBA format.

    Its components describe, in order, the intensity of Red, Green, Blue
    and Alpha (opacity) in the represented color.

*class* RGBA\_Tuple\_Int[¶](#manim.typing.RGBA_Tuple_Int "Link to this definition")
:   ```
    tuple[int, int, int, int]

    ```

    `shape: (4,)`

    A tuple of 4 integers between 0 and 255, representing a color in RGBA
    format.

    Its components describe, in order, the intensity of Red, Green, Blue
    and Alpha (opacity) in the represented color.

*class* HSV\_Array\_Float[¶](#manim.typing.HSV_Array_Float "Link to this definition")
:   ```
    RGB_Array_Float
    ```

    `shape: (3,)`

    A `numpy.ndarray` of 3 floats between 0 and 1, representing a
    color in HSV (or HSB) format.

    Its components describe, in order, the Hue, Saturation and Value (or
    Brightness) in the represented color.

*class* HSV\_Tuple\_Float[¶](#manim.typing.HSV_Tuple_Float "Link to this definition")
:   ```
    RGB_Tuple_Float
    ```

    `shape: (3,)`

    A tuple of 3 floats between 0 and 1, representing a color in HSV (or
    HSB) format.

    Its components describe, in order, the Hue, Saturation and Value (or
    Brightness) in the represented color.

*class* HSVA\_Array\_Float[¶](#manim.typing.HSVA_Array_Float "Link to this definition")
:   ```
    RGBA_Array_Float
    ```

    `shape: (4,)`

    A `numpy.ndarray` of 4 floats between 0 and 1, representing a
    color in HSVA (or HSBA) format.

    Its components describe, in order, the Hue, Saturation and Value (or
    Brightness) in the represented color.

*class* HSVA\_Tuple\_Float[¶](#manim.typing.HSVA_Tuple_Float "Link to this definition")
:   ```
    RGBA_Tuple_Float
    ```

    `shape: (4,)`

    A tuple of 4 floats between 0 and 1, representing a color in HSVA (or
    HSBA) format.

    Its components describe, in order, the Hue, Saturation and Value (or
    Brightness) in the represented color.

*class* HSL\_Array\_Float[¶](#manim.typing.HSL_Array_Float "Link to this definition")
:   ```
    RGB_Array_Float
    ```

    `shape: (3,)`

    A `numpy.ndarray` of 3 floats between 0 and 1, representing a
    color in HSL format.

    Its components describe, in order, the Hue, Saturation and Lightness
    in the represented color.

*class* HSL\_Tuple\_Float[¶](#manim.typing.HSL_Tuple_Float "Link to this definition")
:   ```
    RGB_Tuple_Float
    ```

    `shape: (3,)`

    A `numpy.ndarray` of 3 floats between 0 and 1, representing a
    color in HSL format.

    Its components describe, in order, the Hue, Saturation and Lightness
    in the represented color.

*class* ManimColorInternal[¶](#manim.typing.ManimColorInternal "Link to this definition")
:   ```
    RGBA_Array_Float
    ```

    `shape: (4,)`

    Internal color representation used by [`ManimColor`](manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor"),
    following the RGBA format.

    It is a `numpy.ndarray` consisting of 4 floats between 0 and
    1, describing respectively the intensities of Red, Green, Blue and
    Alpha (opacity) in the represented color.

### Point types[¶](#point_types "Link to this heading")

*class* PointDType[¶](#manim.typing.PointDType "Link to this definition")
:   ```
    ManimFloat
    ```

    Default type for arrays representing points: a double-precision
    floating point value.

*class* Point2D[¶](#manim.typing.Point2D "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (2,)`

    A NumPy array representing a 2-dimensional point: `[float, float]`.

*class* Point2DLike[¶](#manim.typing.Point2DLike "Link to this definition")
:   ```
    Point2D | tuple[float, float]
    ```

    `shape: (2,)`

    A 2-dimensional point: `[float, float]`.

    This represents anything which can be converted to a :class:[`Point2D`](#manim.typing.Point2D "manim.typing.Point2D") NumPy
    array.

    Normally, a function or method which expects a [`Point2D`](#manim.typing.Point2D "manim.typing.Point2D") as a
    parameter can handle being passed a [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") instead.

*class* Point2D\_Array[¶](#manim.typing.Point2D_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, 2)`

    A NumPy array representing a sequence of [`Point2D`](#manim.typing.Point2D "manim.typing.Point2D") objects:
    `[[float, float], ...]`.

*class* Point2DLike\_Array[¶](#manim.typing.Point2DLike_Array "Link to this definition")
:   ```
    Point2D_Array | Sequence[Point2DLike]
    ```

    `shape: (M, 2)`

    An array of [`Point2DLike`](#manim.typing.Point2DLike "manim.typing.Point2DLike") objects: `[[float, float], ...]`.

    This represents anything which can be converted to a :class:[`Point2D_Array`](#manim.typing.Point2D_Array "manim.typing.Point2D_Array")
    NumPy array.

    Normally, a function or method which expects a [`Point2D_Array`](#manim.typing.Point2D_Array "manim.typing.Point2D_Array") as a
    parameter can handle being passed a [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") instead.

    Please refer to the documentation of the function you are using for
    further type information.

*class* Point3D[¶](#manim.typing.Point3D "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (3,)`

    A NumPy array representing a 3-dimensional point: `[float, float, float]`.

*class* Point3DLike[¶](#manim.typing.Point3DLike "Link to this definition")
:   ```
    Point3D | tuple[float, float, float]
    ```

    `shape: (3,)`

    A 3-dimensional point: `[float, float, float]`.

    This represents anything which can be converted to a :class:[`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") NumPy
    array.

*class* Point3D\_Array[¶](#manim.typing.Point3D_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, 3)`

    A NumPy array representing a sequence of [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects:
    `[[float, float, float], ...]`.

*class* Point3DLike\_Array[¶](#manim.typing.Point3DLike_Array "Link to this definition")
:   ```
    Point3D_Array | Sequence[Point3DLike]
    ```

    `shape: (M, 3)`

    An array of [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects: `[[float, float, float], ...]`.

    This represents anything which can be converted to a :class:[`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array")
    NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* PointND[¶](#manim.typing.PointND "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (N,)`

    A NumPy array representing an N-dimensional point: `[float, ...]`.

*class* PointNDLike[¶](#manim.typing.PointNDLike "Link to this definition")
:   ```
    PointND | Sequence[float]
    ```

    `shape: (N,)`

    An N-dimensional point: `[float, ...]`.

    This represents anything which can be converted to a :class:[`PointND`](#manim.typing.PointND "manim.typing.PointND") NumPy
    array.

*class* PointND\_Array[¶](#manim.typing.PointND_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, N)`

    A NumPy array representing a sequence of [`PointND`](#manim.typing.PointND "manim.typing.PointND") objects:
    `[[float, ...], ...]`.

*class* PointNDLike\_Array[¶](#manim.typing.PointNDLike_Array "Link to this definition")
:   ```
    PointND_Array | Sequence[PointNDLike]
    ```

    `shape: (M, N)`

    An array of [`PointND`](#manim.typing.PointND "manim.typing.PointND") objects: `[[float, ...], ...]`.

    This represents anything which can be converted to a :class:[`PointND_Array`](#manim.typing.PointND_Array "manim.typing.PointND_Array")
    NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

### Vector types[¶](#vector_types "Link to this heading")

*class* Vector2D[¶](#manim.typing.Vector2D "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (2,)`

    A 2-dimensional vector: `[float, float]`.

    Normally, a function or method which expects a [`Vector2D`](#manim.typing.Vector2D "manim.typing.Vector2D") as a
    parameter can handle being passed a [`Vector3D`](#manim.typing.Vector3D "manim.typing.Vector3D") instead.

    Caution

    Do not confuse with the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") or [`Arrow`](manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow "manim.mobject.geometry.line.Arrow")
    VMobjects!

*class* Vector2D\_Array[¶](#manim.typing.Vector2D_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, 2)`

    An array of [`Vector2D`](#manim.typing.Vector2D "manim.typing.Vector2D") objects: `[[float, float], ...]`.

    Normally, a function or method which expects a [`Vector2D_Array`](#manim.typing.Vector2D_Array "manim.typing.Vector2D_Array") as a
    parameter can handle being passed a [`Vector3D_Array`](#manim.typing.Vector3D_Array "manim.typing.Vector3D_Array") instead.

*class* Vector3D[¶](#manim.typing.Vector3D "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (3,)`

    A 3-dimensional vector: `[float, float, float]`.

    Caution

    Do not confuse with the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") or [`Arrow3D`](manim.mobject.three_d.three_dimensions.Arrow3D.html#manim.mobject.three_d.three_dimensions.Arrow3D "manim.mobject.three_d.three_dimensions.Arrow3D")
    VMobjects!

*class* Vector3D\_Array[¶](#manim.typing.Vector3D_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, 3)`

    An array of [`Vector3D`](#manim.typing.Vector3D "manim.typing.Vector3D") objects: `[[float, float, float], ...]`.

*class* VectorND[¶](#manim.typing.VectorND "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape (N,)`

    An \(N\)-dimensional vector: `[float, ...]`.

    Caution

    Do not confuse with the [`Vector`](manim.mobject.geometry.line.Vector.html#manim.mobject.geometry.line.Vector "manim.mobject.geometry.line.Vector") VMobject! This type alias
    is named “VectorND” instead of “Vector” to avoid potential name
    collisions.

*class* VectorND\_Array[¶](#manim.typing.VectorND_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape (M, N)`

    An array of [`VectorND`](#manim.typing.VectorND "manim.typing.VectorND") objects: `[[float, ...], ...]`.

*class* RowVector[¶](#manim.typing.RowVector "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (1, N)`

    A row vector: `[[float, ...]]`.

*class* ColVector[¶](#manim.typing.ColVector "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (N, 1)`

    A column vector: `[[float], [float], ...]`.

### Matrix types[¶](#matrix_types "Link to this heading")

*class* MatrixMN[¶](#manim.typing.MatrixMN "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (M, N)`

    A matrix: `[[float, ...], [float, ...], ...]`.

*class* Zeros[¶](#manim.typing.Zeros "Link to this definition")
:   ```
    MatrixMN
    ```

    `shape: (M, N)`

    A [`MatrixMN`](#manim.typing.MatrixMN "manim.typing.MatrixMN") filled with zeros, typically created with
    `numpy.zeros((M, N))`.

### Bézier types[¶](#bézier_types "Link to this heading")

*class* QuadraticBezierPoints[¶](#manim.typing.QuadraticBezierPoints "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (3, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of three 3D control points for a single quadratic Bézier
    curve:
    `[[float, float, float], [float, float, float], [float, float, float]]`.

*class* QuadraticBezierPointsLike[¶](#manim.typing.QuadraticBezierPointsLike "Link to this definition")
:   ```
    QuadraticBezierPoints | tuple[Point3DLike, Point3DLike, Point3DLike]
    ```

    `shape: (3, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of three 3D control points for a single quadratic Bézier
    curve:
    `[[float, float, float], [float, float, float], [float, float, float]]`.

    This represents anything which can be converted to a
    :class:[`QuadraticBezierPoints`](#manim.typing.QuadraticBezierPoints "manim.typing.QuadraticBezierPoints") NumPy array.

*class* QuadraticBezierPoints\_Array[¶](#manim.typing.QuadraticBezierPoints_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (N, 3, 3)`

    A NumPy array containing \(N\) [`QuadraticBezierPoints`](#manim.typing.QuadraticBezierPoints "manim.typing.QuadraticBezierPoints") objects:
    `[[[float, float, float], [float, float, float], [float, float, float]], ...]`.

*class* QuadraticBezierPointsLike\_Array[¶](#manim.typing.QuadraticBezierPointsLike_Array "Link to this definition")
:   ```
    QuadraticBezierPoints_Array | Sequence[QuadraticBezierPointsLike]
    ```

    `shape: (N, 3, 3)`

    A sequence of \(N\) [`QuadraticBezierPointsLike`](#manim.typing.QuadraticBezierPointsLike "manim.typing.QuadraticBezierPointsLike") objects:
    `[[[float, float, float], [float, float, float], [float, float, float]], ...]`.

    This represents anything which can be converted to a
    :class:[`QuadraticBezierPoints_Array`](#manim.typing.QuadraticBezierPoints_Array "manim.typing.QuadraticBezierPoints_Array") NumPy array.

*class* QuadraticBezierPath[¶](#manim.typing.QuadraticBezierPath "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (3*N, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of \(3N\) points, where each one of the
    \(N\) consecutive blocks of 3 points represents a quadratic
    Bézier curve:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* QuadraticBezierPathLike[¶](#manim.typing.QuadraticBezierPathLike "Link to this definition")
:   ```
    Point3DLike_Array
    ```

    `shape: (3*N, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of \(3N\) points, where each one of the
    \(N\) consecutive blocks of 3 points represents a quadratic
    Bézier curve:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`QuadraticBezierPath`](#manim.typing.QuadraticBezierPath "manim.typing.QuadraticBezierPath") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* QuadraticSpline[¶](#manim.typing.QuadraticSpline "Link to this definition")
:   ```
    QuadraticBezierPath
    ```

    `shape: (3*N, 3)`

    A special case of [`QuadraticBezierPath`](#manim.typing.QuadraticBezierPath "manim.typing.QuadraticBezierPath") where all the \(N\)
    quadratic Bézier curves are connected, forming a quadratic spline:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* QuadraticSplineLike[¶](#manim.typing.QuadraticSplineLike "Link to this definition")
:   ```
    QuadraticBezierPathLike
    ```

    `shape: (3*N, 3)`

    A special case of [`QuadraticBezierPathLike`](#manim.typing.QuadraticBezierPathLike "manim.typing.QuadraticBezierPathLike") where all the \(N\)
    quadratic Bézier curves are connected, forming a quadratic spline:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a :class:[`QuadraticSpline`](#manim.typing.QuadraticSpline "manim.typing.QuadraticSpline")
    NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* CubicBezierPoints[¶](#manim.typing.CubicBezierPoints "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (4, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of four 3D control points for a single cubic Bézier curve:
    `[[float, float, float], [float, float, float], [float, float, float], [float, float, float]]`.

*class* CubicBezierPointsLike[¶](#manim.typing.CubicBezierPointsLike "Link to this definition")
:   ```
    CubicBezierPoints | tuple[Point3DLike, Point3DLike, Point3DLike, Point3DLike]
    ```

    `shape: (4, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of 4 control points for a single cubic Bézier curve:
    `[[float, float, float], [float, float, float], [float, float, float], [float, float, float]]`.

    This represents anything which can be converted to a :class:[`CubicBezierPoints`](#manim.typing.CubicBezierPoints "manim.typing.CubicBezierPoints")
    NumPy array.

*class* CubicBezierPoints\_Array[¶](#manim.typing.CubicBezierPoints_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (N, 4, 3)`

    A NumPy array containing \(N\) [`CubicBezierPoints`](#manim.typing.CubicBezierPoints "manim.typing.CubicBezierPoints") objects:
    `[[[float, float, float], [float, float, float], [float, float, float], [float, float, float]], ...]`.

*class* CubicBezierPointsLike\_Array[¶](#manim.typing.CubicBezierPointsLike_Array "Link to this definition")
:   ```
    CubicBezierPoints_Array | Sequence[CubicBezierPointsLike]
    ```

    `shape: (N, 4, 3)`

    A sequence of \(N\) [`CubicBezierPointsLike`](#manim.typing.CubicBezierPointsLike "manim.typing.CubicBezierPointsLike") objects:
    `[[[float, float, float], [float, float, float], [float, float, float], [float, float, float]], ...]`.

    This represents anything which can be converted to a
    :class:[`CubicBezierPoints_Array`](#manim.typing.CubicBezierPoints_Array "manim.typing.CubicBezierPoints_Array") NumPy array.

*class* CubicBezierPath[¶](#manim.typing.CubicBezierPath "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (4*N, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of \(4N\) points, where each one of the
    \(N\) consecutive blocks of 4 points represents a cubic Bézier
    curve:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* CubicBezierPathLike[¶](#manim.typing.CubicBezierPathLike "Link to this definition")
:   ```
    Point3DLike_Array
    ```

    `shape: (4*N, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of \(4N\) points, where each one of the
    \(N\) consecutive blocks of 4 points represents a cubic Bézier
    curve:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`CubicBezierPath`](#manim.typing.CubicBezierPath "manim.typing.CubicBezierPath") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* CubicSpline[¶](#manim.typing.CubicSpline "Link to this definition")
:   ```
    CubicBezierPath
    ```

    `shape: (4*N, 3)`

    A special case of [`CubicBezierPath`](#manim.typing.CubicBezierPath "manim.typing.CubicBezierPath") where all the \(N\) cubic
    Bézier curves are connected, forming a quadratic spline:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* CubicSplineLike[¶](#manim.typing.CubicSplineLike "Link to this definition")
:   ```
    CubicBezierPathLike
    ```

    `shape: (4*N, 3)`

    A special case of [`CubicBezierPath`](#manim.typing.CubicBezierPath "manim.typing.CubicBezierPath") where all the \(N\) cubic
    Bézier curves are connected, forming a quadratic spline:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`CubicSpline`](#manim.typing.CubicSpline "manim.typing.CubicSpline") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPoints[¶](#manim.typing.BezierPoints "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (PPC, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of \(\text{PPC}\) control points
    (\(\text{PPC: Points Per Curve} = n + 1\)) for a single
    \(n\)-th degree Bézier curve:
    `[[float, float, float], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPointsLike[¶](#manim.typing.BezierPointsLike "Link to this definition")
:   ```
    Point3DLike_Array
    ```

    `shape: (PPC, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of \(\text{PPC}\) control points
    (\(\text{PPC: Points Per Curve} = n + 1\)) for a single
    \(n\)-th degree Bézier curve:
    `[[float, float, float], ...]`.

    This represents anything which can be converted to a
    :class:[`BezierPoints`](#manim.typing.BezierPoints "manim.typing.BezierPoints") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPoints\_Array[¶](#manim.typing.BezierPoints_Array "Link to this definition")
:   ```
    NDArray[PointDType]
    ```

    `shape: (N, PPC, 3)`

    A NumPy array of \(N\) [`BezierPoints`](#manim.typing.BezierPoints "manim.typing.BezierPoints") objects containing
    \(\text{PPC}\) [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects each
    (\(\text{PPC: Points Per Curve} = n + 1\)):
    `[[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPointsLike\_Array[¶](#manim.typing.BezierPointsLike_Array "Link to this definition")
:   ```
    BezierPoints_Array | Sequence[BezierPointsLike]
    ```

    `shape: (N, PPC, 3)`

    A sequence of \(N\) [`BezierPointsLike`](#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike") objects containing
    \(\text{PPC}\) [`Point3DLike`](#manim.typing.Point3DLike "manim.typing.Point3DLike") objects each
    (\(\text{PPC: Points Per Curve} = n + 1\)):
    `[[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`BezierPoints_Array`](#manim.typing.BezierPoints_Array "manim.typing.BezierPoints_Array") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPath[¶](#manim.typing.BezierPath "Link to this definition")
:   ```
    Point3D_Array
    ```

    `shape: (PPC*N, 3)`

    A [`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") of \(\text{PPC} \cdot N\) points, where each
    one of the \(N\) consecutive blocks of \(\text{PPC}\) control
    points (\(\text{PPC: Points Per Curve} = n + 1\)) represents a
    Bézier curve of \(n\)-th degree:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* BezierPathLike[¶](#manim.typing.BezierPathLike "Link to this definition")
:   ```
    Point3DLike_Array
    ```

    `shape: (PPC*N, 3)`

    A [`Point3DLike_Array`](#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array") of \(\text{PPC} \cdot N\) points, where each
    one of the \(N\) consecutive blocks of \(\text{PPC}\) control
    points (\(\text{PPC: Points Per Curve} = n + 1\)) represents a
    Bézier curve of \(n\)-th degree:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`BezierPath`](#manim.typing.BezierPath "manim.typing.BezierPath") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* Spline[¶](#manim.typing.Spline "Link to this definition")
:   ```
    BezierPath
    ```

    `shape: (PPC*N, 3)`

    A special case of [`BezierPath`](#manim.typing.BezierPath "manim.typing.BezierPath") where all the \(N\) Bézier curves
    consisting of \(\text{PPC}\) [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects
    (\(\text{PPC: Points Per Curve} = n + 1\)) are connected, forming
    an \(n\)-th degree spline:
    `[[float, float, float], ...], ...]`.

    Please refer to the documentation of the function you are using for
    further type information.

*class* SplineLike[¶](#manim.typing.SplineLike "Link to this definition")
:   ```
    BezierPathLike
    ```

    `shape: (PPC*N, 3)`

    A special case of [`BezierPathLike`](#manim.typing.BezierPathLike "manim.typing.BezierPathLike") where all the \(N\) Bézier curves
    consisting of \(\text{PPC}\) [`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects
    (\(\text{PPC: Points Per Curve} = n + 1\)) are connected, forming
    an \(n\)-th degree spline:
    `[[float, float, float], ...], ...]`.

    This represents anything which can be converted to a
    :class:[`Spline`](#manim.typing.Spline "manim.typing.Spline") NumPy array.

    Please refer to the documentation of the function you are using for
    further type information.

*class* FlatBezierPoints[¶](#manim.typing.FlatBezierPoints "Link to this definition")
:   ```
    NDArray[PointDType] | tuple[float, ...]
    ```

    `shape: (3*PPC*N,)`

    A flattened array of Bézier control points:
    `[float, ...]`.

### Function types[¶](#function_types "Link to this heading")

*class* FunctionOverride[¶](#manim.typing.FunctionOverride "Link to this definition")
:   ```
    Callable

    ```

    Function type returning an [`Animation`](manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") for the specified
    [`Mobject`](manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

*class* PathFuncType[¶](#manim.typing.PathFuncType "Link to this definition")
:   ```
    Callable[[Point3DLike, Point3DLike, float], Point3DLike]
    ```

    Function mapping two :class:[`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") objects and an alpha value to a new
    :class:[`Point3D`](#manim.typing.Point3D "manim.typing.Point3D").

*class* MappingFunction[¶](#manim.typing.MappingFunction "Link to this definition")
:   ```
    Callable[[Point3D], Point3D]
    ```

    A function mapping a :class:[`Point3D`](#manim.typing.Point3D "manim.typing.Point3D") to another :class:[`Point3D`](#manim.typing.Point3D "manim.typing.Point3D").

*class* MultiMappingFunction[¶](#manim.typing.MultiMappingFunction "Link to this definition")
:   ```
    Callable[[Point3D_Array], Point3D_Array]
    ```

    A function mapping a :class:[`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array") to another
    :class:[`Point3D_Array`](#manim.typing.Point3D_Array "manim.typing.Point3D_Array").

### Image types[¶](#image_types "Link to this heading")

*class* PixelArray[¶](#manim.typing.PixelArray "Link to this definition")
:   ```
    NDArray[ManimInt]
    ```

    `shape: (height, width) | (height, width, 3) | (height, width, 4)`

    A rasterized image with a height of `height` pixels and a width of
    `width` pixels.

    Every value in the array is an integer from 0 to 255.

    Every pixel is represented either by a single integer indicating its
    lightness (for greyscale images), an [`RGB_Array_Int`](#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int") or an
    [`RGBA_Array_Int`](#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int").

*class* GrayscalePixelArray[¶](#manim.typing.GrayscalePixelArray "Link to this definition")
:   ```
    PixelArray
    ```

    `shape: (height, width)`

    A 100% opaque grayscale [`PixelArray`](#manim.typing.PixelArray "manim.typing.PixelArray"), where every pixel value is a
    [`ManimInt`](#manim.typing.ManimInt "manim.typing.ManimInt") indicating its lightness (black -> gray -> white).

*class* RGBPixelArray[¶](#manim.typing.RGBPixelArray "Link to this definition")
:   ```
    PixelArray
    ```

    `shape: (height, width, 3)`

    A 100% opaque [`PixelArray`](#manim.typing.PixelArray "manim.typing.PixelArray") in color, where every pixel value is an
    [`RGB_Array_Int`](#manim.typing.RGB_Array_Int "manim.typing.RGB_Array_Int") object.

*class* RGBAPixelArray[¶](#manim.typing.RGBAPixelArray "Link to this definition")
:   ```
    PixelArray
    ```

    `shape: (height, width, 4)`

    A [`PixelArray`](#manim.typing.PixelArray "manim.typing.PixelArray") in color where pixels can be transparent. Every pixel
    value is an [`RGBA_Array_Int`](#manim.typing.RGBA_Array_Int "manim.typing.RGBA_Array_Int") object.

### Path types[¶](#path_types "Link to this heading")

*class* StrPath[¶](#manim.typing.StrPath "Link to this definition")
:   ```
    str | PathLike[str]

    ```

    A string or `os.PathLike` representing a path to a
    directory or file.

*class* StrOrBytesPath[¶](#manim.typing.StrOrBytesPath "Link to this definition")
:   ```
    str | bytes | PathLike[str] | PathLike[bytes]

    ```

    A string, bytes or `os.PathLike` object representing a path
    to a directory or file.