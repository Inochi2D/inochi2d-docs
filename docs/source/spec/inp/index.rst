===========================
INP Specification
===========================

INP Stands for **In**\ ochi2D **P**\ uppet, and is a binary container format to contain Inochi2D model, texture and extra data.

INP is subject to change as we get closer to the 1.0 release.

Format Layout
-------------

.. note::
   .. container:: ada-block

    .. image:: /img/ada-think.png
      :class: ada
      :align: left
      :width: 128px
    
    Inochi2D stores values in Big Endian format, please make sure you handle this correctly!

    You can find out more about endianness `here <https://en.wikipedia.org/wiki/Endianness>`__.

.. list-table:: 
    :header-rows: 1

    * - Length (bytes)
      - Contents
      - Notes
    * - 8
      - ``TRNSRTS\0``
      - Magic bytes which tag the file as an INP file. (Trans Rights!)
    * - 4
      - JSON Payload Length
      - Length of JSON Payload
    * - *Payload Length*
      - JSON Data
      - The Inochi2D model and rigging data
    * - 8
      - ``TEX_SECT``
      - Texture Section Header
    * - 4
      - Texture Count
      - Amount of textures in the texture section
    * - *Till Texture Blob End*
      - `Texture Blob <#texture-blob>`__
      - Contains a texture and tag denoting what type the texture is.
    * - 8
      - ``EXT_SECT``
      - **OPTIONAL**: Header for extended vendor data section
    * - 4
      - Payload Count
      - **IF EXT_SECT EXISTS** Amount of payloads that are in this section
    * - *Till EXT Section End*
      - `EXT Section Blob <#extended-vendor-data-blob>`__
      - **IF EXT_SECT EXISTS** The section blob of this EXT section.

Texture Blob
------------

Every texture entry in the Texture Blob have the following encoding

.. list-table:: 
    :header-rows: 1

    * - Length (bytes)
      - Contents
      - Notes
    * - 4
      - Texture Payload Length
      - Length of the Texture Payload
    * - 1
      - `Texture Encoding <#texture-encoding>`__
      - A byte defining what texture encoding is in use. See Texture Encoding section.
    * - *Payload Length*
      - Texture Data
      - Encoding of data depends on previous type

Extended Vendor Data Blob
-------------------------

.. list-table:: 
    :header-rows: 1

    * - Length (bytes)
      - Contents
      - Notes
    * - 4
      - Name Length
      - Length of EXT Payload name
    * - *Name Length*
      - Name
      - The name of the EXT payload
    * - 4
      - Payload Length
      - Length of the EXT payload
    * - *Payload Length*
      - Payload
      - Contents of payload, encoding is up to the individual developer.

Texture Encoding
----------------

There's 3 currently officially supported formats in Inochi2D, which are the following:

.. list-table:: 
    :header-rows: 1

    * - ID
      - Format
    * - 0
      - `PNG - Portable Network Graphics <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`__ (Lossless)
    * - 1
      - `TGA - Truevision TGA <https://en.wikipedia.org/wiki/Truevision_TGA>`__ (Lossless)
    * - 2
      - `BC7 - BPTC Texture Compression <https://www.khronos.org/opengl/wiki/BPTC_Texture_Compression>`__ (Lossy)

.. toctree::
   :maxdepth: 2
   :caption: INP Specification
   :name: sec-spec-inp
   :hidden:

   profiles