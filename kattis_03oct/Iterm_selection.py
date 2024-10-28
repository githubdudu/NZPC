n, m, s, p, q = [int(x) for x in input().split()]
s = s -1
plist = []
qlist = []
for i in range(p):
    pval = int(input()) - 1
    plist.append(pval)

for i in range(q):
    qval = int(input()) - 1
    qlist.append(qval)

pages_num = n // m + 1


ans = 0

page_changed = set()
for page in range(pages_num):
    setp = set()
    setq = set()
    for K in range(page * m, (page + 1) * m):
        if K in plist:
            setp.add(K)
        if K in qlist:
            setq.add(K)
    
    if setp == setq:
        continue

    page_changed.add(page)
    
    # compare set
    modify_by_check = len(setp) + len(setq) - 2 * len(set.intersection(setp, setq))
    
    all_items = m if page != pages_num - 1 else n - page * m
    modify_by_checkall = 1 + all_items - len(setq)
    modify_by_uncheckall = 1 + len(setq)
    # print(modify_by_check, modify_by_checkall, modify_by_uncheckall)
    ans += min(modify_by_check, modify_by_checkall, modify_by_uncheckall)


if len(page_changed):
    min_changed_page = min(page_changed)
    max_changed_page = max(page_changed)
    
    turn_left = abs(min_changed_page - s)
    turn_right = abs(max_changed_page - s)

    if s >= min_changed_page and s <= max_changed_page:
        ans += turn_left + turn_right + min(turn_right, turn_left)
    else:
        ans += max(turn_right, turn_left)
    
print(ans)