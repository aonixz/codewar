def make_readable(seconds):
    sec = str(seconds % 60).zfill(2)
    mint = str((seconds // 60)%60).zfill(2)
    hour = str((seconds // (60**2))%100).zfill(2)
    return f"{hour}:{mint}:{sec}"