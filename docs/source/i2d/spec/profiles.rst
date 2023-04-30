=====================
Profiles & Extensions
=====================

| **NOTE**: Profiles and extensions are a *to be implemented* feature of the Inochi2D specification.
| *Most of this documentation is preliminary context.*

| The Inochi2D format is meant to be portable and usable across many platforms, but for some usescases you want more powerful features.
| For example, maybe you're targeting modern PCs or smartphones and your project's artists want more flexibility in how they render their art.
| Inochi2D provides Profiles and Extensions to cover these needs.
|
| Inochi2D is split up in to 3 main profiles, each profile being a superset of the other.

1. Core
2. Standard
3. Extended

| Additionally Inochi2D will be supporting named extensions to the format, so that implementors can chose to add, remove or modify features of the spec for their needs.
| Every vendor which makes an extension has a unique prefix. The official Inochi2D Extension prefix is ``I2D``.
| Extensions will depend on a profile and Inochi2D version to be available, the extensions will in general specify which version of Inochi2D they target and what profile.

.. list-table:: 
    :header-rows: 1

    * - Tag
      - Vendor
    * - I2D
      - Inochi2D Project

| 
| 

---------------
Profiles
---------------

| Following are the profiles specced out for Inochi2D as of current.
| This list may be subject to change.

~~~~~~~~~~~~~~~~
The Core Profile
~~~~~~~~~~~~~~~~

| Core is meant for low power devices which may not have recent features, think PCs from 2012 and newer, or smartphones from 2013.
| As such, Core is quite stripped down compared to what you see in Inochi Creator by default, and is to some extent rather limited.
| Due to the nature of the core profile it's not recommended for most use cases, only use this if you're targetting really old hardware.

.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - Minimum
      - Recommended
    * - GL
      - 2.1
      - 2.2
    * - DirectX
      - 9
      - 10
    * - Vulkan
      - 1.0
      - 1.0
    * - Metal
      - Latest
      - Latest

~~~~~~~~~~~~~~~~~~~~
The Standard Profile
~~~~~~~~~~~~~~~~~~~~

| The standard profile is the profile most people should be targeting.
| It's aimed at modern PCs, phones and games consoles, although some features may need to be approximated on some platforms, it's the best in terms of feature-to-stability ratio.

.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - Minimum
      - Recommended
    * - GL
      - 3.1
      - 3.2
    * - DirectX
      - 10
      - 12
    * - Vulkan
      - 1.0
      - 1.3
    * - Metal
      - Latest
      - Latest

~~~~~~~~~~~~~~~~~~~~
The Extended Profile
~~~~~~~~~~~~~~~~~~~~

| The extended profile contains features that have a potential of making it in to Standard.
| These features can be very experimental in nature and is, in general, not recommended for production use.
| Generally things making it to Extended should start out as extensions instead.

.. list-table:: 
    :header-rows: 1
    :stub-columns: 1

    * - 
      - Minimum
      - Recommended
    * - GL
      - 3.1
      - 4.5
    * - DirectX
      - 10
      - 12
    * - Vulkan
      - 1.0
      - 1.3
    * - Metal
      - Latest
      - Latest

| 
| 

---------------
Extensions
---------------

| Extensions recognized by the Inochi2D Project are listed here.
| If more documentation is available about the extension, said documentation can be seen by clicking the name of the extension.

.. list-table:: 
    :header-rows: 1

    * - Name
      - Version
      - Profile
    * - I2D_BLEND_ACCURACY [#early_extension]_
      - 8.0
      - Standard
    * - I2D_EXTENDED_BLEND_MODES [#early_extension]_
      - 8.0
      - Standard

.. [#early_extension] This extension was introduced before extensions were added to the spec.
    
    As such, older Inochi2D implementations will more or less just assume it's there.