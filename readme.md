MD to Patchouli
===============

This script is a barebones WIP that converts markdown to Patchouli.

Right now it does nothing. It's not helpful. What are you doing even looking at this? Holy cow.

Dev-Toolchain
-------------
I'm working in WSL using the Ubuntu 18.04 image. Pandoc asserts it's version `1.19.2.4~dfsg-1build4` from the current repos... In python3 I've installed `panflute`. You don't necessarily need a venv, but you probably should be using one. Eventually I'll generate one specific to this project and include the reqs in it. Sorry in the meantime.

Expected workflow
-----------------
For the time being, I'm only focused on writing page contents for ordinary text and tags - the contents of the [Text Formatting 101](https://github.com/Vazkii/Patchouli/wiki/Text-Formatting-101) page. This means all the metadata json files will have to be written by hand, and any mettadata around the text will have to be written by hand.

Nor is the format well-defined; for the time being, I'm experimenting with how I want the input to look. tl;dr - don't get too attached to anything that's not in the standard markdown spec as native.

Longer term goals
-----------------
Including features that are highly unlikely to happen

* [ ] Template Support
  * [ ] Patchouli Templates
  * [ ] Some sort of markdown preprocessor
* [ ] Language Support
  * [X] Basic Text
  * [ ] All isomorphic tags
    * [X] `$(br)` (linebreak)
    * [X] `$(br2)` (paragraph break)
    * [ ] `$(li)` (unordered list item)
      * [ ] `$(li2)` to some number (6?) - list item levels.
    * [X] `$(l)`  (bold)
    * [X] `$(m)` (strikethrough
    * [X] `$(o)` (italics)
    * [x] `$(l:...)...($/l)` (links)
    * [x] `$(k:...)` (keyboard buttons, basically.)
  * [ ] Presumably span tags
    * [ ] `$(#RRGGBB)` - colors (span with style?)
    * [ ] `$(#RGB)`    - colors (span with style?)
    * [ ] `$(#C)`      - palette index colors (span with style?)
	* [ ] `$(c:/command here)...(/c)` - commands (span with custom property?)
  * [ ] Custom/psudeo- tags.
    * [ ] `$(playername)` - Player's name (`<playername />`?)
    * [ ] `$(k)` - obfuscated text (not a clue)
    * [ ] `$(t:...)...($/t)` - Tooltips. (`<tooltip text="...">...</tooltip>` ?)
    * [ ] `$()` - clears formatting - `<clear />` or `<reset />` or even both?
  * [ ] Patchouli's macros
    * [ ] `$(obf)` --> `$(k)` via `<obf>...</obf>`?
    * [X] `$(bold)`
    * [X] `$(strike)`
    * [X] `$(italic)`
    * [X] `$(italics)`
    * [ ] `$(list)`
    * [ ] `$(reset)`
    * [ ] `$(clear)`
    * [X] `$(2br)` (but why though?)
    * [X] `$(p)` (again, but why though?)
    * [X] `<br>` - again, but why?
    * [ ] `$(nocolor)` - resets color to palette 0.
    * [ ] `$(item)` - sets color to `#b0b`, `<item>...</item>`?
    * [ ] `$(thing)` - sets color to `#490`, `<thing>...</thing>`?
* [ ] Support for YAML instead of JSON in JSON files
  * [ ] book.json
  * [ ] category json files
  * [ ] document front matter (`panflute.getOption()` ?)
  * [ ] page front matter
* [ ] Split pages somehow in Markdown (Horizontal rules? Headers for pages with titles?)
* [ ] Support for alternative page types
  * [ ] Text
  * [ ] Image
  * [ ] Crafting
  * [ ] Smelting
  * [ ] Multiblock
  * [ ] Entity
  * [ ] Spotlight
  * [ ] Link
  * [ ] Relations
  * [ ] Quest
  * [ ] Empty
* [ ] Support for other features in Patchouli that I'm probably not listing with enough detail here.
  * [ ] Advancement locking
  * [ ] Book extensions
  * [ ] Flag support
  * [ ] Multiblock support
* [ ] Support for requested features
  * [ ] Auto-Pagination support