# Design rules (starter)

Copy this file to `<records>/design-rules.md` on the first round, then make it the owner's: add every rule from an owner review, quoted, and drop any the owner doesn't hold. The orchestrator checks every rule in the project's copy on every round, on every changed page. A round that breaks one is not a pass, even when every task was reached.

- **Subheaders** say what a thing is in a few words, and never list what the page can do. Unclear terms get a (?).
- **Action labels** name what they act on: "Approve refund", not "Approve". Every label passes the action-name test.
- **Lists always paginate:** a range and a total, first, previous, next and last, and rows per page, on one line at every width. A collection reads as a list even when it has one item.
- **Actions that collect information open a modal** with a dark backdrop, no blur, and a short animation in and out. Nothing is appended to the page, and nothing moves.
- **A handled item stays in place** and says what happened to it.
- **A short list of choices** (up to about five) shows as visible options, not a dropdown.
- **Every named entity is a link** to it, with its entity icon.
- **Table headers stay on one line.** A long name moves into a (?).
- **Controls show they can be used without hovering.** A row that opens and closes ends in a "Show / Hide" cue; a row that opens something ends in a chevron.
- **Parts of a page keep clear spacing,** for example between the view tabs and the content.
- **A record opened beside a list is a full-height sidebar,** pinned at the window's edge and resizable.
- **Tooltips float above everything** from one layer on the page, so no pane crops them.
- **The page scrolls across the whole work area,** so its scrollbar sits at the window's edge. Content width is limited inside the page.
- **Header actions wrap under the title** before the title itself breaks.
- **Product terms stay exact:** each term keeps the one wording the owner chose, everywhere.
