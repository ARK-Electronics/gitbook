---
name: product-pages
description: The pages each ARK product has on docs.arkelectron.com and what goes on each one, covering the landing README, Firmware, Hardware Reference, the PX4, ArduPilot and Betaflight instructions, nav order in SUMMARY.md and redirects in .gitbook.yaml. Use when adding a product, when adding, moving or deleting a product's pages, or when restructuring a product section.
---

# Product Pages

Each product has a directory in its section, such as `gps/ark-teseo-gps/`. Copy the shape of these pages:

| Case | Model on |
|---|---|
| CAN node with firmware | `gps/ark-teseo-gps/` |
| Landing with variants | `flight-controller/arkv6x/README.md` |
| Second configuration that builds on the first | `gps/ark-g5-rtk-heading-gps/` |

Facts come from the existing docs, the store listing, the schematic or the source you read. When the store and the docs disagree, keep the docs value and say so in the PR. The prose follows the `docs-writing` skill.

## Nav

List the product in `SUMMARY.md` under its section, and add a `{% content-ref %}` block for it to the section's `README.md`. Child pages go in this order: Firmware, Hardware Reference and its children, PX4 Instructions, ArduPilot Instructions, Betaflight Instructions, then setup guides and other pages.

## Landing

`README.md` holds these, in this order:

1. Frontmatter with `cover` and `coverY`. Leave out `description:`, because GitBook shows it as a subtitle that repeats the intro.
2. The product name as the H1, spelled as the store spells it.
3. An intro of one sentence, two at most, saying what the product is and what it plugs into or works with. It holds at most one link, to another ARK docs page. Caveats, vendor links and pointers to other products go on the subpages.
4. The button row, on one line with a space between buttons:
   - `<a href="<store url>" class="button primary" data-icon="cart-shopping">Buy</a>`. For several store variants, link the category or tag page that lists them, never `#variants`. A carrier sold bare and as an NDAA bundle gets two primary buttons, `Buy carrier` and `Buy NDAA bundle`.
   - Then come the secondary buttons, when ark-hardware has the files. All three use `class="button secondary"`.

     | Button | `data-icon` | Links to |
     |---|---|---|
     | 3D model | `cube` | `…/tree/main/<DIR>/model` |
     | Case | `box` | `…/tree/main/<DIR>/case` |
     | Datasheet | `file-pdf` | The datasheet PDF |
5. Bullets with the facts a buyer scans for, as `* **Label:** value` in plain text with no links. Use as many as the product has. Reuse the labels other landings use, such as Processor, Receiver, Sensors, Interface, Power, Autopilots and Compliance. A bullet states the fact. Version requirements, per-variant qualifiers and caveats go on the subpage that covers them. Compliance reads `USA built, NDAA, Blue Framework listed`, or the part of that the store states.
6. `## Variants`, only when the store sells several: `| Variant | <what differs> | … | Buy |`, with the variant name in bold and `[Buy](<store url>)` in each row. When each variant sells as a module and as a bundle, use two Buy columns, such as `Module` and `On PAB carrier`.
7. `## Documentation`, listing the top-level child pages in nav order, with the nav title as link text and no descriptions.

The landing has no specifications, pinout, firmware, embeds or package contents. The store lists what ships. A block the reader needs before anything else, such as the Jetson carriers' Where to Start, goes after the bullets.

## Firmware

`firmware.md` exists only for products whose firmware the user updates or configures, such as CAN nodes, ESCs, flight controllers and configurable receivers. It holds these sections, in this order, as they apply:

1. How to update. Keep existing embeds.
2. `## Downloads`, linking the files under `downloads.arkelectron.com/firmware/<product>/latest/` and the product's directory of all releases.
3. Bootloader notes.
4. `## Node Parameters`, as one `| Parameter | Default | Description |` table. Read the defaults from the firmware source. In `private_px4` they are in `src/**/*params*.yaml` and `src/**/parameters.yaml`, and `boards/ark/<board>/init/rc.board_defaults` overrides them. ESC defaults come from `ARK32` and `ark32-configurator`. When you can't find a default, keep the existing wording and say so in the PR.
5. Sub-tables, such as constellations.
6. `## Release Notes` last, newest first, with one `### v<version> - <hash> - <date>` heading per release.

## Hardware Reference

`hardware.md` holds these sections, in this order, as they apply:

1. `## Specifications`, as a `| Specification | Value |` table. Chips link to the vendor's product page. Cover the MCU, interfaces, power as voltage and current, dimensions, mounting, weight and temperature ratings. A Blue Framework listed product gets a `Compliance` row that links the [framework list](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).
2. `## Pinout`, with one `###` per connector named `<Function> (J<n>) — <N>-pin <connector type>` and a `| Pin | Signal | Voltage |` table under it. Leave out the designator when the silkscreen has none. Merge identical connectors as `(×N)`. Number pins the way the mating ARK boards' pages do, so pin 1 on one page meets pin 1 on the other.
3. `## LEDs`.
4. Other hardware sections the product needs, such as a block diagram, mechanical drawing, mounting, wiring or power.
5. `## 3D Model and Case`, as a `| File | Contents |` table linking the latest revision's files at `https://github.com/ARK-Electronics/ark-hardware/raw/main/<path>`. Below it goes `All files: [<DIR> in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/<DIR>)`.
6. `## Schematic and BOM`, only when ark-hardware has `schematic/` or `bom/` files for the product.

Small hardware pages, such as a separate pinout, LED or 3D model page, fold into `hardware.md`. A large one, such as a long pinout or a block diagram with many images, can stay as a child of `hardware.md`, which then lists it.

## Autopilot Instructions

`px4-instructions.md`, `ardupilot-instructions.md` and `betaflight-instructions.md` cover setup on the flight controller only. A CAN node's page has this shape, followed by any tuning sections and `## Troubleshooting`:

```
## Single GPS Configuration
One sentence on how to connect it.
### Flight Controller Parameters
#### Required      | Parameter | Value | Description |
#### Optional      | Parameter | Description |
### CAN Node Parameters
One or two sentences linking firmware.md#node-parameters.
```

- PX4 parameter names link to the PX4 parameter reference at `https://docs.px4.io/main/en/advanced_config/parameter_reference.html#<NAME>`.
- Document a publish and subscribe pair, such as `CANNODE_PUB_MAG` and `UAVCAN_SUB_MAG`, only when the product has that sensor on board.
- A second configuration, such as dual-antenna heading, gets its own H2 that builds on the first: "Apply the [Single GPS Configuration](#single-gps-configuration) above, then add the following".
- The ArduPilot page mirrors the PX4 page's layout. It opens with the ArduPilot version that works, and custom builds go below it.
- Battery monitor parameters use the instance placeholder the page already uses, `BATTx_*` or `BATTn_*`, never a fixed instance such as `BATT2_*`.

## Moving or Deleting Pages

GitBook builds URLs from the nesting in `SUMMARY.md`. A page that is renamed, deleted or moved to a new parent needs a redirect in `.gitbook.yaml`. The comment at the top of that file gives the key format. A landing never moves, because store pages link to it.

Fix every link to a moved page or anchor. Find them with `git grep -n '<old path or anchor>'`.

GitBook ignores a new redirect for a page deleted in the same sync. After the merge, open the old URLs. If they 404, push another change to `.gitbook.yaml` so the next sync applies the redirects.
