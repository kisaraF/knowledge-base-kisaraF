# Head

- Head can be seen in git log specially.
- It is the pointer to the current branch. There can be many branches and only the branch last worked on, currently logged in will be pointed by the HEAD.
- Opening up the git log for a repo with multiple branches confirms this
- Head will point to current branch and the other branches will follow. And usually the current branch will have one color and the rest will have a different.

```
commit <commit_id> (HEAD -> `branch_1`, main)
```
- This means currently in branch_1

- If a new branch is made from the current branch's commit, the head shows the same point for both branches
```
commit <commit_id> (HEAD -> `branch_1`, `main`)
```

This can be explained more with a book analogy

- Book : Repo working on
- Bookmarks : Different branches and there can be multiple branches
- HEAD : The bookmark currently opened (not every bookmark can be opened up at the same time)

## (Optional) On Git Storing Head of each branch

If you do a ```git log```, you can find the git commit history for each branch in that particular branch. Similarly if you go to the `.git` folder, "refs -> heads" folder you can see a text file for each branch with the latest commit hash of that branch. Compare it with git log commit hashes for a clear picture.