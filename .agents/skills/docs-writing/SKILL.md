---
name: docs-writing
description: How pages on docs.arkelectron.com read, covering voice, sentence shape, what to cut, accuracy, formatting and GitBook markup. Use before writing or editing any page in this repo, and when asked to make a page read better, tighten it or review a docs PR for style.
---

# Writing ARK docs

Readers are engineers putting ARK hardware on a vehicle. They open a page to find a fact or to finish a task. Write the way you would explain it to one of them at the bench: whole sentences, addressed to "you", with nothing they would miss if it were gone.

## Sentences

- **One thought per sentence.** Finish it before the next one starts. A second thought doesn't go in parentheses, after a dash or a semicolon, or in a trailing "which" clause. Give it its own sentence or cut it.
- **Whole sentences.** Every sentence has a subject and a verb. Shortness comes from fewer thoughts, never from dropping verbs and articles. A page of clipped fragments reads like notes.
- **Active voice, present tense, the reader as "you".** Write "Connect the carrier's USB-C port to a computer", not "The USB-C port can be connected to a computer".
- **The action or fact first, then its condition.** "On a vehicle, power the carrier from the battery input."
- **Plain words.** "The radio shows up as a network adapter" beats "the radio enumerates as a CDC-ECM device". Use the exact term when the reader has to type it or search for it.
- **Names the reader can find.** Call a control, menu entry or tool what the screen calls it. Spell out any abbreviation the page hasn't introduced.

A page goes wrong in two directions: clipped notes, and long chains of clauses.

| Reads like notes or a chain | Reads like a person |
|---|---|
| Both inputs can stay connected. The higher voltage powers the radio. | You can connect battery and USB-C at the same time, and the carrier runs from whichever is the higher voltage. |
| `demo.sh [user@host]` | `demo.sh jetson@jetson.local` |
| The adapter level-translates it from the camera port's `CAMn_PWDN` pin, and the host drivers release it once and never pull it low again, so a camera driver powering down cannot reset the Boson. | The EO sensor and the Boson share the reset on pin 17. ARK's drivers release it once and never pull it low again, so powering down the EO camera does not reset the Boson. |

## What to Cut

- Why the page exists, who it's for, or what it will cover. A page that leaves a topic to another manual can say so in one sentence and link to it.
- Reassurance, such as "no X required", "works out of the box", "simply", "easily" or "seamless".
- Intensifiers, such as "single worst", "completely", "significantly" or "perfectly". Give the number instead: "raises the noise floor by 20 dB".
- Failure stories. State the limit and what to do about it. The customer report that prompted a change belongs in the commit message.
- Whatever the table, command or figure next to the sentence already shows.
- Internals the reader can't act on, such as how the image builds a driver or which clock pin limits a port's lanes. Keep the constraint and drop the mechanism.
- Datasheet detail, such as which part sets a rating, absolute maximums or the PCB stackup.
- Example values the reader picks, such as radio addresses, unless a later step uses them.
- Placeholder sections reading "N/A", "TBD" or "Coming soon".

## Accuracy

- Every fact comes from a source you read: the schematic, firmware source, the store listing, a bench result or upstream docs. Don't fill a gap with a plausible value.
- Say what was measured. Give the symptom, not a cause nobody measured. Give the cases tested, not a rule drawn from them: "ran out of memory on an Orin Nano 4GB and ran on an Orin NX 16GB", not "needs an Orin NX 16GB". Call a nominal limit "typical".
- Say plainly when a setup hasn't been tested on hardware.
- Lead with what works. The supported version or the standard setup comes first, and workarounds and custom builds go below it.
- Give a shared fact one home, and link to it from the other pages. Copies drift. AFBR range, for example, lives only in `sensor/ark-dist/hardware.md#range`.
- Use the store's product names and spellings, such as SoM, PCIe and InvenSense. The board is a "flight controller". PX4 and ArduPilot are the autopilots.
- Compliance claims are "USA built", "NDAA" and "Blue Framework listed", and only where the store or the docs already state them. ARK products make no FCC claim.
- Docs land with a product's launch, so a page can describe an image release, a store page or an ark-hardware PR that is still in flight. Don't promise files or features that nobody is making.

## Structure

- Open a section with what the thing does or shows. The command or table comes next.
- Put per-item facts in a table, such as facts per carrier, per port, per mode or per control. A table cell that holds several sentences means the data needs its own table, or a paragraph under the table.
- Give parallel options parallel sections. USB and UART flashing are two subsections at the same level. Don't put one in the parent's prose and nest the other below it.
- Show every way to run a tool. If a script works over USB and UART, give the command for each.
- Write commands as the reader types them, with real defaults. Then say in a sentence what to change for another setup.
- A list holds bare items or whole sentences. A bold label, as in `* **Label:** value`, suits fact lists such as landing bullets.
- Save hints for what the reader must not miss. Use `warning` for what breaks a setup or exceeds a rating, `danger` for what damages hardware, and `info` for a fact that is easy to overlook. Open the hint with what to do, then give the limit.

## Formatting

- Headings are in Title Case. The H1 is the page title and matches the page's `SUMMARY.md` entry.
- UI names are bold, with `>` between menu levels: **Vehicle Settings > Parameters**.
- Parameters, paths, device nodes, addresses and values the reader types go in code spans: `CANNODE_TERM`, `/dev/i2c-7`, `0x68`. Fenced code blocks name their language, such as `bash`.
- Escape underscores in link text, as GitBook's own export does: `[UAVCAN\_ENABLE](…)`.
- Put a space between a number and its unit, as in 5 V, 1.5 A and 400 kHz. Ranges take an en dash, as in 5.5–55 V. Counts take `×`, as in 2× CAN.
- Don't hard-wrap a paragraph. Break lines only between paragraphs, list items, headings, fences and blockquotes.
- Link other docs pages by a relative path to the `.md` file, such as `../../gps/ark-teseo-gps/README.md`. Link to upstream sources and manuals rather than restating them.
- Keep GitBook blocks intact: `{% hint %}`, `{% embed %}`, `{% file %}`, `{% tabs %}`, `{% content-ref %}`, `<figure>` and the `<a class="button …">` buttons.

## Editing a Page for Style

1. Read the whole page and its sibling pages first. Find sentences that carry several facts, table cells that hold paragraphs, and facts repeated across pages.
2. Split the chains into sentences. Move per-item facts into tables. Give each repeated fact one home.
3. Leave sentences that already read well. Don't change commands, values, pinouts or links.
4. Keep every fact unless it's an internal the reader can't act on. Name what you dropped in the PR description, so the author can object.

## Reviewing a Docs PR

Check each claim against its source. Leave out findings that only say a dependency hasn't landed, such as an unreleased image, a draft store product, or 3D model links waiting on an ark-hardware PR. Flag a claim only when it will still be wrong once the dependency lands.
