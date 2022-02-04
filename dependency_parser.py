import spacy

from verbs import VERBS_DECREASE, VERBS_INCREASE


def parse_dependencies(text: str) -> list[dict]:
    graph_data = list()

    nlp = spacy.load("en_core_web_trf")
    doc = nlp(text)

    for sent in doc.sents:
        sent_root = [token for token in nlp(sent.text) if token.head == token][0]
        
        if sent_root.lemma_ not in VERBS_DECREASE | VERBS_INCREASE:
            continue

        sent_subject = list(sent_root.lefts)[0]
        sent_object = list(sent_root.rights)[0]

        graph_data.append(
            {
                "sentence": sent.text,
                "data": {
                    "subject": sent_subject.lemma_,
                    "predicate": sent_root.lemma_,
                    "object": sent_object.lemma_
                }
            }
        )
    
    return graph_data
