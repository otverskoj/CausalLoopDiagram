import pprint
import spacy

from verbs import VERBS_DECREASE, VERBS_INCREASE


prepared_sentences = list()

TEXT = "Net income was $9.4 million compared to the prior year of $2.7 million. Revenue exceeded twelve billion dollars, with a loss of $1b."

nlp = spacy.load("en_core_web_trf")
doc = nlp(TEXT)

for sent in doc.sents:
    sent_root = [token for token in nlp(sent.text) if token.head == token][0]
    
    if sent_root.lemma_ not in VERBS_DECREASE + VERBS_INCREASE:
        continue

    sent_subject = list(sent_root.lefts)[0]
    sent_object = list(sent_root.rights)[0]

    prepared_sentences.append(
        {
            "sentence": sent.text,
            "data": {
                "subject": sent_subject.text,
                "predicate": sent_root.lemma_,
                "object": sent_object.text
            }
        }
    )

pprint.pprint(prepared_sentences)
