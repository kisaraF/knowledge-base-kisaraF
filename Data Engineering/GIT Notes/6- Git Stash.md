# Purpose of Stash

When you have two branches with the same exact files and you modify an existing file. But without committing changes, you try to switch to the other branch. Then you will get a message as,

```
error: Your local changes to the following files would be overwritten by checkout:
        <files>
Please commit your changes or stash them before you switch branches.
Aborting
```

In such cases `git stash` could temporarily save the uncommited changes and help with the switching back and forth