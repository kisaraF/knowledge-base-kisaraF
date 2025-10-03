# Ripgrep & Xargs

## Usage
Grep any file with a certain text using `ripgrep`, `xargs` it and see if a specific text is not included there.

```
rg --glob="*.sql" -l -e "customer_id"  models/marts/sl_corp/ | xargs -I{} rg --files-without-match customer_sk {}
```
Definition: repgrip .sql files which contains text "customer_id" from models/marts/... directory -> then get those files and pass them line by line (file by file) to see if they don't  contain any specific text as "customer_sk"