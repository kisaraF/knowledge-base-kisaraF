# A Workflow when using Git

## How do I keep my feature branch up to date with the main branch?

1. Switch to the main branch
2. `git pull origin main` on the main branch where the feature branch is based on. By specifying "origina main" you're always pulling from the correct branch even if upstream is not set
3. Switch to the feature branch
4. `git rebase main` This will provide a clean history of the main branch while preserving feature branch commits

---
## How do I resolve divergent branches?

### Why divergence happens?

Divergence happens when:

- Your local branch has commits that the remote does NOT have, and
- The remote branch has commits that your local branch does NOT have.

In other words, both sides moved forward independently, creating two different histories.

Has faced this incident especially when working in a feature branch which was originally unapproved from the pull request and then needed to be worked on. After making the necessary changes, committing and when it's time for pushing the commits, a message where "divergent branches" are displayed. In such cases,

1. `git pull --rebase` should be performed. This will again make the working history clean and get the HEAD to reflect current changes while preserving original work (It rewrites your local commits on top of the latest remote commits, producing a clean and linear history)
2. (optional) if every git pull needs to be a rebase from here onwards, `git config pull.rebase true` can be set
3. If there are no conflics it will display "Successfully rebased ..." type of a message
4. If in case any merge conflicts are there, then they should be resolved by hopping into an editor
5. Once the conflicts are resolved, `git rebase --continue` should be provided to confirm the conflicts resolved and to complete the rebase
6. Finally do `git push --force-with-lease`

After pushing, your feature branch is now fully synchronized with both main (from earlier rebase) and its own remote branch.

### Why --force-with-lease?

- `--force-with-lease` will check if there are other commits made by another user and if there are any, it won't push. Hence it is safe.
- Unlike in `--force` where it will ignore everything and will do a hard force push.
- This is useful when there are other people who are also working on the same feature branch as you are.

---

## Reviving a Screw up

Imagine you have been working on something and accidently screw up some work or something devastating or diabolical happens. In such cases, reverting back to the previous sane state of the code can help immensly.

### Reset `HARD`

If you want to get to the previous sane working state, without any of the modifications you have done so far, then this is the best bet. This will revive everything back to that last commit point by erasing all work you have done so far.

To get started, do `git reflog` and you will find something similar to below,

```
d3a324c (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
833800a (origin/main, origin/HEAD) HEAD@{1}: commit: test wip
d3a324c (HEAD -> main) HEAD@{2}: commit: Instance methods & attribute protectors in encapsulation
fdd52f3 HEAD@{3}: reset: moving to HEAD~1
4a2c318 HEAD@{4}: commit: Instance methods & protected attributes of encapsulation
fdd52f3 HEAD@{5}: commit: Adding Python class notes
31150f9 HEAD@{6}: reset: moving to HEAD@{1}
1728147 HEAD@{7}: reset: moving to HEAD~1
31150f9 HEAD@{8}: commit: Modifying gitignore
1728147 HEAD@{9}: checkout: moving from temp to main
7e96567 (origin/temp) HEAD@{10}: checkout: moving from main to temp
1728147 HEAD@{11}: pull: Fast-forward
56164c9 HEAD@{12}: checkout: moving from temp to main
7e96567 (origin/temp) HEAD@{13}: checkout: moving from main to temp
56164c9 HEAD@{14}: pull origin main: Fast-forward
afac433 HEAD@{15}: reset: moving to HEAD
afac433 HEAD@{16}: commit: Adding Higher Order Functions
24307e7 HEAD@{17}: reset: moving to HEAD
24307e7 HEAD@{18}: pull: Merge made by the 'ort' strategy.
75d933e HEAD@{19}: commit: Python Logging Tutorial
89a3189 HEAD@{20}: commit: Adding the Python Sets Note
2a4d957 HEAD@{21}: commit (merge): Merge branch 'main' of github.com:kisaraF/knowledge-base-kisaraF
d8659e2 HEAD@{22}: commit (amend): WIP! Python Files Organizing
ff1fe4c HEAD@{23}: pull: Fast-forward
4df591e HEAD@{24}: clone: from github.com:kisaraF/knowledge-base-kisaraF.git
```

Now all you have to do is, find the last commit where you want to revert back to, and do the following,
`git reset --hard HEAD@{n}`

Practically you will go back to that commit point. But still, if you have commited the progress of your screwd up work at any point, you still can revert back to their too.

Notice in the above git reflog log, there are several places where I have reset and moved back on the timeline.

### Reset `SOFT`

But what if you only want to change one small place that causes a big trouble where you don't want to edit the other 100 lines of code all over again?

Imagine the situation of that AI bot review at Superloop. Just because of one line the whole pipeline fails and all I have to do is uncommit that commit and unstage just one file to make the pipeline successful. And if I hard reset, I'd have to do all manually all over again. Because a new commit is also not an option. 

In such cases, all you have to do is, do `git reset --soft HEAD~n`.

If you want to go back just one commit back, the head value is 1. If it's 2 commits back then 2.

This will keep all the changes you made along the way back on the staging area and remove those commits, which is a huge life saver.

