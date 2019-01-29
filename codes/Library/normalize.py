from scaler import min_max

def normalize_data(search, location, timeline):
    count = 0
    timeline_dict = timeline

    collection = []
    for key, value in timeline_dict.items():
        if count == 4:
            break
        else:
            if location in timeline_dict[key]:
                if search in timeline_dict[key][location]:
                    data = timeline_dict[key][location][search]
                    collection.append(data)
                    count += 1

    results_aspects = {}

    for x in collection:
        for y in x:
            if y[0] in results_aspects:
                results_aspects[y[0]] += y[1]
            else:
                results_aspects.setdefault(y[0], y[1])
                
    pos_aspects = {}

    for key, value in results_aspects.items():
        if value >= 0 :
            pos_aspects.setdefault(key, value)
    
    array_of_num = []

    for key, value in pos_aspects.items():
        array_of_num.append(value)

    normalize_num = min_max(array_of_num,0,100)

    count = 0
    normalize_array = []
    for key, value in pos_aspects.items():
        if normalize_num[count] > 0:
            normalize_array.append((normalize_num[count], key))
        count += 1

    normalize_array.sort(reverse=True)

    return normalize_array   

def get_location(data, hotel_info):
    location = []
    for a in data:
        location.append([a[1], hotel_info[a[1]][0], hotel_info[a[1]][2], hotel_info[a[1]][3]])
        
    return location