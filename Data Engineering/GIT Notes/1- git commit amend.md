# Git Commit Amend

Whenever a commit has been made and if that commit was incompleted (maybe missed a few files from bein added into the staging area while doing the `git add`). In such cases this command is useful.

`git commit --amend` will redo the previous command (only the previous command).

For example,

Let's say there are 5 files to be added and commit.

```
git add file_1, file_2, file_3, file_4
```

```
git commit -m "Add the files"
```

- Now that you missed file_5, without making a new commit just for that with a different message, you can use `--amend` option as below:

```
git add file_5
```

```
git commit --amend
```

- This will open up a vim editor by default and the previous commit's message will be there. Make a change if necesary or leave it as it is.

After saving changes, try:

```
git log
```

If `--amend` worked, only the previous commit (modified or not) will exist.
