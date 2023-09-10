========
Blending
========

| Inochi2D allows for porter-duff blending modes to be applied to Part nodes and Composite nodes, these blending nodes affect how colors are mixed on compositing with the screen.
| Additionally the special blending modes "Clip to Lower" and "Slice from Lower" are supported to provide a nicer looking but less flexible form of masking.

| 
| 

----------------------
Rendering equations
----------------------

.. list-table:: 
    :header-rows: 1

    * - Mode
      - Equation
      - Src
      - Dst
      - Src (Alpha)
      - Dst (Alpha)
    * - Normal
      - Add
      - 1
      - 1-SrcAlpha
      - 
      - 
    * - Multiply
      - Add
      - DstColor
      - 1-SrcAlpha
      - 
      - 
    * - Screen
      - Add
      - 1
      - 1-SrcColor
      - 
      - 
    * - Lighten
      - Max
      - DstColor
      - 1
      - 
      - 
    * - Color Dodge
      - Add
      - DstColor
      - 1
      - 
      - 
    * - Linear Dodge
      - Add
      - 1
      - 1-SrcColor
      - 1
      - 1-SrcAlpha
    * - Add (Glow)
      - Add
      - 1
      - 1
      - 1
      - 1-SrcAlpha
    * - Subtract
      - ReverseSubtract
      - 1-DstColor
      - 1
      - 
      - 
    * - Exclusion
      - Add
      - 1-DstColor
      - 1-SrcColor
      - 1
      - 1
    * - Inverse
      - Add
      - 1-DstColor
      - 1-SrcAlpha
      - 
      - 
    * - Destination In
      - Add
      - 0
      - SrcAlpha
      - 
      - 
    * - Clip to Lower
      - Add
      - DstAlpha
      - 1-SrcAlpha
      - 
      - 
    * - Slice from Lower
      - Add
      - 0
      - 1-SrcAlpha
      - 
      - 


| 
| 

------------------------
Blend Accuracy Extension
------------------------

| Inochi2D provides the ``I2D_BLEND_ACCURACY`` :doc:`extension </spec/inp/profiles>`, this extension is entirely implementation side.
| If the Inochi2D implementation indicates support for this extension, it means that instead of emulating porter and duff blending modes, it will use GPU extensions to implement them properly.
| This extension affects the rendering of the following blending modes.

* Normal
* Multiply
* Screen
* Lighten
* Color Dodge
* Subtract
* Inverse

| This extension additionally affects the rendering of the following blending modes if ``I2D_EXTENDED_BLEND_MODES`` is supported.

* Overlay
* Darken
* Color Burn
* Hard Light
* Soft Light
* Difference
* Exclusion

These blending modes use legacy blending if you have more than a Albedo output on some platforms.

**Implementation Notes**

* This extension can be implemented in OpenGL via the `GL_KHR_blend_equation_advanced and GL_KHR_blend_equation_advanced_coherent <https://registry.khronos.org/OpenGL/extensions/KHR/KHR_blend_equation_advanced.txt>`__ extensions.
* This extension can be implemented in Vulkan via the `VK_EXT_blend_operation_advanced <https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VK_EXT_blend_operation_advanced.html>`__ extension.
* This extension can be implemented on tiler GPUs, such as PowerVR and Apple Silicon chips, via framebuffer fetch.

| This extension was introduced in Inochi2D 0.8 Standard.

| 
| 

--------------------
Extended Blend Modes
--------------------

| Inochi2D provides the ``I2D_EXTENDED_BLEND_MODES`` :doc:`extension </spec/inp/profiles>`.
| This extension adds support for the following blending modes.

* Overlay
* Darken
* Color Burn
* Hard Light
* Soft Light
* Difference
* Exclusion

These blending modes are disabled if you have more than Albedo output.

**Implementation Notes**

* This extension can be emulated by shaders using Texture Barriers.
* This extension can be emulated by shaders using a ping-pong framebuffer setup, this is unoptimal.

| This extension was introduced in Inochi2D 0.8 Standard.
| This extension is influenced by ``I2D_BLEND_ACCURACY``.