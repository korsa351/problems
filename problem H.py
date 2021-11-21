ans = 0
uniq_obj = []
for obj in objects:
    if obj in uniq_obj:
        pass
    else:
        ans += 1
        uniq_obj.append(obj)
print(ans)
