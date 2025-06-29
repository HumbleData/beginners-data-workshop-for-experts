mask_PW_PL = (df['days_overdue'] > 2) & (df['member_type'] == "Adult")
df[mask_PW_PL]