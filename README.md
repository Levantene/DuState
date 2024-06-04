"# DuState"

git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch \*.csv" \
--prune-empty --tag-name-filter cat -- --all
