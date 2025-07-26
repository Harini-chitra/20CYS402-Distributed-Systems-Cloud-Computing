def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m
def minutes_to_time(m):
    h = m // 60
    m = m % 60
    return f"{h:02d}:{m:02d}"
daemon_time = "15:00"
node_times = ["15:10", "14:50", "15:25"]
all_times_min = [time_to_minutes(daemon_time)] + [time_to_minutes(t) for t in node_times]
avg_time_min = sum(all_times_min) // len(all_times_min)
avg_time_str = minutes_to_time(avg_time_min)
print(f"After Synchronization...\n")
print(f"Time Daemon : {avg_time_str}")
for i, t in enumerate(node_times, 1):
    node_min = time_to_minutes(t)
    correction = avg_time_min - node_min
    correction_sign = "+" if correction >= 0 else ""
    print(f"Node {i}: {avg_time_str} [Correction Value: {correction_sign}{correction}]")
