def study_schedule(permanence_period, target_time):
    total = 0
    try:
        for check_in, check_out in permanence_period:
            if check_in <= target_time <= check_out:
                total += 1
        return total
    except TypeError:
        return None
