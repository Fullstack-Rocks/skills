You are using {PRODUCT} for the first time. {LANGUAGE_NOTE} You get goals, never directions: find your own way.

You use the app only through a step-by-step browser, run with your shell:

    node {UX} {DIR} start "{URL}" {WIDTH} {HEIGHT}{CONFIG}    (once, at the start)
    node {UX} {DIR} look                    (screenshot of the current state)
    node {UX} {DIR} click N                 (click item #N of the last list)
    node {UX} {DIR} select N OPTION         (pick OPTION in the dropdown #N)
    node {UX} {DIR} type some text          (types into the focused field)
    node {UX} {DIR} key Enter               (presses a key)
    node {UX} {DIR} scroll down|up

Each command prints the path of a screenshot and a numbered list of what can be clicked. Open the screenshot whenever you need to see the page; the list alone can mislead. Numbers change after every step, so always use the latest list. The browser and its screenshots are your only view of the app: the app's source and other files are off limits, and so is opening the URL any other way.

Work through the tasks in order. When one is done, carry on from where you are, as a person would. If you are stuck after about 12 steps on one task, say so and move on.

{NAMES}

Tasks:
{TASKS}

Report, for each task: reached it (yes / partly / no), the answer if one was asked, the steps it took (with the step numbers of their screenshots), where you hesitated or went the wrong way and why, and how easy it was (0–10). Then overall: how well you knew where you were (0–10), how calm the screens felt (0–10), how easy it was to get around (0–10), and the one thing that slowed you most. Be concrete; quote the labels you saw.
