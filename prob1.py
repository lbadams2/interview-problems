#
# Complete the 'eliminate_non_preferred_sources' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY analysis_sources as parameter.
#
import collections
def eliminate_non_preferred_sources(analysis_sources):
    unordered_data = {}
    ordered_keys = []
    ordered_dict = collections.OrderedDict()
    
    for line in analysis_sources:
        for item in line:
            kv = item.split(':')
            key = kv[0]
            val = kv[1]
            if key not in ordered_keys:
                ordered_keys.append(key)
            unordered_data[key] = val

    for key in ordered_keys:
        yield str(unordered_data[key])

