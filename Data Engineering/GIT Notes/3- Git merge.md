# Merging branches


## Fast Forward Merges

Imagine you have a branch as "lily" which is infront of the "master" branch like below

```
commit e28dabba82d15bc5dc3cb139e15a926bc905b36f (HEAD -> lily)
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:16:30 2025 +1100

    add lily's doe patronus

commit a77645b29608204debea32e014180b2d985c57a0
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:15:00 2025 +1100

    add snape's doe patronus

commit 5b434b260ac7e202fcd50d9de14a6e021201d787 (master)
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:10:29 2025 +1100

    add empty patronus file
```

What has happened here is:

- Master branch was first created and an empty file was created in it.
- Then a new branch as "lily" was created and 2 new commits were added


Now in order to sync the forwarded commits in "lily" branch to "master" branch, we can do a fast forward merge like below,

First log into the "master" branch

```
git switch master
```

Then merge as,

```
git merge lily
```

Then you could see that git log for "master" branch as,

```
commit e28dabba82d15bc5dc3cb139e15a926bc905b36f (HEAD -> master, lily)
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:16:30 2025 +1100

    add lily's doe patronus

commit a77645b29608204debea32e014180b2d985c57a0
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:15:00 2025 +1100

    add snape's doe patronus

commit 5b434b260ac7e202fcd50d9de14a6e021201d787
Author: Kisara Fernando <kisarawenu@gmail.com>
Date:   Wed Oct 8 16:10:29 2025 +1100

    add empty patronus file
```
