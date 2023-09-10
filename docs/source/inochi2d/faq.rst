==========================
Frequently Asked Questions
==========================

We get asked some questions often, we've compiled some of them and listed answers to them here.

How much does Inochi2D Cost?
----------------------------

**Nothing**, Inochi2D is free, BSD 2-clause licensed software. You may download and use it at no cost, with the only limit being that you may not remove the license text from the software.
You can *optionally* support the development monetarily via `Patreon <https://patreon.com/LunaFoxgirlVT>`__ or `GitHub Sponsors <https://github.com/sponsors/LunaTheFoxgirl>`__, though this is completely optional.

Is Inochi2D ready for use?
--------------------------

Inochi2D and the accompanying tools are still heavily work-in-progress. 
They are usable for usecases we officially support, but it's still evolving very quickly so we can't promise that it is ready for game development.
Some of the tooling is still a work in progress and will be improved with time to be easier to use.

Can I load my PSD file in to Inochi Creator?
--------------------------------------------
Yes, under the File->Import menu you can import Photoshop PSD documents, do note that PSD support is still a work in progress and some metadata may load incorrectly (blending modes being applied wrong or layers being hidden that shouldn't)
You may need to do some manual work setting blending modes and unhiding/hiding nodes in the node tree in that case.

Can I use my existing Live2D models with Inochi2D?
--------------------------------------------------
No, Inochi2D is an entirely new open format that is on a fundamental level incompatible with Live2D. As such the model will have to be re-rigged for Inochi2D. Inochi2D should for the most part be compatible with PSDs cut for Live2D use, though.

What advantages does Inochi2D have over Live2D?
-----------------------------------------------
Inochi2D has multiple advantages, some still in development:
 1. Inochi2D is open source and has no licensing fees for integration in your project
 2. Inochi2D natively supports multi-texturing for render passes, this means you can add special rendering effects to your model at low rendering cost, such as eyes that glow in the dark, make your model react to lighting in a scene and more.
 3. Inochi2D is extensible, if you're a developer you can add new Node and Automation types to Inochi2D without breaking other applications that support Inochi2D.
 4. Inochi2D combines all the required assets and data in to its INP file format, this format additionally allows apps to save settings to your model, allowing those settings to transfer over if you move the model to a new computer.
 5. Inochi2D is quite light on PC resources, while Inochi2D has not had a proper optimization pass yet the performance is already pretty decent. We'll be improving performance further over time as we get closer to 1.0.

Does Inochi2D support pre-defined animations?
---------------------------------------------

From version 0.8 of Inochi2D you can create animations and save them to your model.

Does Inochi2D do face tracking?
-------------------------------

Inochi2D in of itself is just a format for 2D puppets/models. The official Inochi Session app and facetrack-d library provides you with the ability to use your Inochi2D puppet in conjunction with face tracking technologies.

Why does text in Inochi Creator in X language look like question marks?
-----------------------------------------------------------------------

Inochi Creator uses ImGui to render its UI, as of current ImGui does not support dynamically loading glyphs from fonts, and loading every text character under the sun would be bad for performance. Until dynamic character loading is in place English and Japanese are the main supported languages.
Translations may specify metadata files with font and glyph range information for their respective languages, but text from those languages will only render properly if you set Inochi Creator to that language.
Inochi Creator does not support languages that require advanced font shaping (eg. Arabic) as well as right-to-left languages currently due to ImGui limitations. If those limitations some day get solved we'll let you know.

I would like to use Inochi2D for blockchain/web3/etc., is this supported?
-------------------------------------------------------------------------

*No*, and we're not interested in any "projects" using that technology.
We ask that you do not harass our team members and contributors about it,
nor bring it up on our Discord.