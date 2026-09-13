---
name: game-text-style
description: The voice of every string the player reads: dialogue, lore, item text, battle messages, and UI labels. Terse, concrete, grim, dry. Load before you write or review any entry in the string table or any content file with player text.
---

# Game text style skill

This skill holds the voice of the game (D-11, D-27, D-63). It binds every string the player reads. It does not bind documents, which follow `ste-writing`. The owner approves this skill under OQ-15, and every text batch after it (D-57).

## The voice in one line

Short sentences. Physical detail. No purple prose. Dry understatement. The world is grim and lethal, and the text never says so. It shows a thing and stops.

## Rules

1. Prefer a concrete noun to an adjective. "The blade is notched" beats "the ancient, terrible blade".
2. One sentence, one image. Cut the second image.
3. Understate. A dead soldier "did not get up". Do not write "his life was cruelly torn away".
4. No exclamation marks outside a shout in dialogue.
5. No modern idiom, no slang, no wink at the player.
6. Humor is dry and rare. It comes from a character, never from the narrator.
7. Dialogue sounds like a person under strain. Short lines. People interrupt, deflect, and lie.
8. Battle messages state the fact and the number. "Vess takes 41." "The wolf falls."
9. Item text gives what the item does in one line, and one line of flavor at most.
10. The player finds lore. Nobody tells it. A page, a carving, a corpse. Never a narrator lecture.
11. Names are short and pronounceable. One or two syllables for people. Places can take three.
12. Never name a mechanic in a story line. A save point is a shrine, a campfire, a bell, whatever the hub makes it.
13. Show violence in short physical detail, in the flat tone of rule 3. Never show sexual violence. Never show harm to a child on screen (D-126).

## Length limits

| Kind | Limit |
|---|---|
| Battle message | 40 characters |
| Menu label | 16 characters |
| Item description | 2 lines at 60 characters |
| Dialogue line | 3 lines at 80 characters |
| Lore entry | 12 lines at 80 characters |

The frame is 1280 by 800 with a 16-pixel font (D-228). The font pick sets how many characters fit across. A panel holds less. The limit is the panel, not the frame.

## Examples

Good: "The gate is open. Nobody opened it."

Good: "She counts the arrows again. Six. She does not say the number."

Bad: "An eerie, foreboding silence hung over the desolate, cursed gate like a shroud."

Bad: "Wow, that was close! Let's get out of here!"

## Procedure

1. Write the text.
2. Read it aloud. Cut every word that does not carry an image or a fact.
3. Check each line against the length limits.
4. Put the text in the string table with an id. Never in code (G-7).
5. Put the batch in the PR description, so the owner reads it in one place (D-57).
