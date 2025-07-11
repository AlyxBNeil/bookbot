def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    return len(text.lower())

# Assuming you have your empty dictionary called `counts_dict`
def count_each_letter(text):
    text = text.lower()
    counts_dict = {}
    for char in text: # This line needs to be at the same indentation level as counts_dict = {}
        if char in counts_dict:
            counts_dict[char] +=1
        else:
            counts_dict[char] =1

    return counts_dict

def sort_on(d):
    return d["num"]

def char_report(counts_dict):
    report_list = []

    for char, count in counts_dict.items():
        if char.isalpha():
            report_list.append({"char": char, "num": count})

    report_list.sort(key=sort_on, reverse=True)
    return report_list

            
