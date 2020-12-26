def timeConversion(s):
    if "AM" in s:
        if s.split(':')[0] == '12':
            return s.replace('12','00').replace('AM','')
        return s.replace('AM','')

    else:
        hours = s.split(':')[0]
        if hours == '12':
            return s.replace('PM','')
        full_time = str((int(hours) + 12)) + s.replace(str(hours), '',1)
        full_time = full_time.replace('PM','')
        return full_time

print(timeConversion('12:01:00AM'))
