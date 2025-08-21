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
      - `JSON Object <#json-payload>`__
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

JSON Payload
------------

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Notes
    * - ``meta``
      - `object(Puppet Meta) <#puppet-meta>`__
      - Meta information (name, artist, etc) about the puppet
    * - ``physics``
      - `object(Physics) <#physics>`__
      - Physics info
    * - ``nodes``
      - object(Node)
      - The root node of the puppet, contains all other nodes
    * - ``param``
      - optional<list<Parameter>>
      - The parameters of the puppet
    * - ``automation``
      - optional<list<Automation>>
      - The parameters of the puppet
    * - ``animations``
      - optional<X>
      - Named animations of the puppet

Puppet Meta
-----------

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Notes
    * - ``name``
      - optional<string>
      - Name of the puppet
    * - ``version``
      - string
      - Version of the Inochi2D spec that was used when creating this model
    * - ``rigger``
      - optional<string>
      - Rigger(s) of the puppet
    * - ``artist``
      - optional<string>
      - Artist(s) of the puppet
    * - ``rights``
      - `optional<object(Meta Rights)> <#meta-rights>`__
      - Usage Rights of the puppet
    * - ``copyright``
      - optional<string>
      - Copyright string
    * - ``licenseURL``
      - optional<string>
      - URL of the license
    * - ``contact``
      - optional<string>
      - Contact information of the first author
    * - ``reference``
      - optional<string>
      - Link to the origin of this puppet
    * - ``thumbnailId``
      - optional<uint32>
      - Texture ID of this puppet's thumbnail
    * - ``preservePixels``
      - boolean
      - Whether the puppet should preserve pixel borders. This feature is mainly useful for puppets that use pixel art

Meta Rights
-----------

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Notes
    * - ``allowedUsers``
      - enum<``onlyAuthor|onlyLicensee|everyone``>
      - Pixels-per-meter for the physics system
    * - ``allowViolence``
      - boolean
      - Whether violent content is allowed
    * - ``allowSexual``
      - boolean
      - Whether sexual content is allowed
    * - ``allowCommercial``
      - boolean
      - Whether commercial use is allowed
    * - ``allowRedistribution``
      - enum<``prohibited|viralLicense|copyleftLicense``>
      - Whether a model may be redistributed
    * - ``allowModification``
      - enum<``prohibited|allowPersonal|allowRedistribute``>
      - Whether a model may be modified
    * - ``requireAttribution``
      - boolean
      - Whether the author(s) must be attributed for use

Physics
-------

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Notes
    * - ``pixelsPerMeter``
      - optional<float>
      - Pixels-per-meter for the physics system
    * - ``gravity``
      - optional<float>
      - Gravity for the physics system

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
