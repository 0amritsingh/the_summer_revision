def word_frequency(sentence):
    frequency_dict ={}
    unique_words = set(sentence.split(' '))
    for i in unique_words:
        frequency_dict.update({i:sentence.split(' ').count(i)})
    return frequency_dict

sen = 'the cat sat on the mat the cat'
print(word_frequency(sen))