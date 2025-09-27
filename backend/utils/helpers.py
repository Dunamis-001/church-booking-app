from datetime import datetime

def parse_iso(dt_str: str) -> datetime:
    if not isinstance(dt_str, str):
        raise ValueError("not a string")
    s = dt_str.strip()
    if s.endswith('Z'):
        s = s[:-1] + '+00:00'
    try:
        return datetime.fromisoformat(s)
    except Exception:
        if '.' in s:
            s = s.split('.')[0]
            return datetime.fromisoformat(s)
        raise