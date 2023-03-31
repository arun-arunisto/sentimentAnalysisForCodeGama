def sentiment_analysis(text, pipe):
    analysis = pipe([text])
    if analysis[0]['label'] == 'POS':
        n = ['checked', 'disabled', 'disabled']
    elif analysis[0]['label'] == 'NEU':
        n = ['disabled', 'checked', 'disabled']
    elif analysis[0]['label'] == 'NEG':
        n = ['disabled', 'disabled', 'checked']
    return n