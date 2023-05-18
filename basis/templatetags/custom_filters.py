from django import template
import replace

register = template.Library()

bad_words = [
    'job',
    'understand',
    'something',
]

sentence = "I love my job but you don't understand something about it"

@register.filter()
def censor(sentence):
    text = sentence.split()
    for i,word  in enumerate(text):
        if word in bad_words:
            text[i] = word[0] + '***'
    return ' '.join(text)





