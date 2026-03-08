def calculate_risk(wave_height):
    if wave_height < 2:
        return "Low"
    elif wave_height < 4:
        return "Medium"
    else:
        return "High"