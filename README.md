# The Funniest Out-of-Office

[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/sambob0606/makefun-out-of-office-kreutzx/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/sambob0606/makefun-out-of-office-kreutzx/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

One line of out-of-office auto-reply, the funniest I could write in 140
characters or fewer — entered in the
[make.fun bounty](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf)
"The Funniest Out-of-Office".

## The reply

> Out of office: I've forwarded your email to my houseplant. It can't type, can't read, and still has a better work-life balance than I do.

## How it works

`main.py` (Python 3, standard library only) validates the reply — 1 to 140
characters, a single line, no control characters — and writes it to
`/output/entry.txt` (falling back to a local `output/` directory when
`/output` is not writable).

```sh
python3 main.py
```
