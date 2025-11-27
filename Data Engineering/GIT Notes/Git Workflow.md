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