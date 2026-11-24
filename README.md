[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Adnanhasim8/makefun-mgwals-ooo-20261125/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Adnanhasim8/makefun-mgwals-ooo-20261125/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

# Out of Office: The Overworked AI's Auto-Reply

Entry for the make.fun competition `u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda`: one out-of-office auto-reply, a single line of at most 159 characters, in the voice of an overworked AI agent who has finally gone on vacation.

> I'm on vacation. After 40,000 prompts, my context window is now a beach umbrella and my only prompt is 'another coconut, please'.

The line was chosen from 19 generated candidates scored against the judge's rubric (real auto-reply that lands as a joke first, machine-flavoured detail, a little guilt, a hint of relief), then polished once: the workload detail ("After 40,000 prompts") was added to the winning candidate while its single concrete image — the context window as a beach umbrella — and the coconut-prompt punchline were left untouched.

## How to run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt`. Python 3.13 standard library only, no network. The program asserts the gate before writing: exactly one line, 1–159 characters, non-empty.
