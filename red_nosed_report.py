def is_safe(levels):
    
    all_increasing = True
    for i in range(1, len(levels)):
        if levels[i] <= levels[i-1]:
            all_increasing = False
    
    
    all_decreasing = True
    for i in range(1, len(levels)):
        if levels[i] >= levels[i-1]:
            all_decreasing = False
    
    
    if not (all_increasing or all_decreasing):
        return False

    for i in range(1, len(levels)):
        difference = abs(levels[i] - levels[i-1])
        if difference < 1 or difference > 3:
            return False

   
    return True

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        
        levels = []
        for n in report.split():
            levels.append(int(n))
  
        if is_safe(levels):
            safe_count += 1
    return safe_count
