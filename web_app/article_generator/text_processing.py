# import nltk
# import numpy as np
# import networkx as nx
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from sklearn.metrics.pairwise import cosine_similarity
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
#
# def preprocess_text(text):
#     sentences = sent_tokenize(text)
#     stop_words = set(stopwords.words("russian"))
#
#     preprocessed_sentences = []
#     for sentence in sentences:
#         words = word_tokenize(sentence)
#         words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
#         preprocessed_sentences.append(words)
#
#     return preprocessed_sentences
#
#
# def compute_similarity_matrix(sentences):
#     similarity_matrix = np.zeros((len(sentences), len(sentences)))
#
#     for i in range(len(sentences)):
#         for j in range(len(sentences)):
#             if i != j:
#                 sentence1 = sentences[i]
#                 sentence2 = sentences[j]
#                 all_words = list(set(sentence1 + sentence2))
#                 vector1 = [sentence1.count(word) for word in all_words]
#                 vector2 = [sentence2.count(word) for word in all_words]
#
#                 similarity_score = cosine_similarity([vector1], [vector2])[0, 0]
#
#                 similarity_matrix[i][j] = similarity_score
#
#     return similarity_matrix
#
#
# def extract_summary(text, max_symbol):
#     preprocessed_sentences = preprocess_text(text)
#
#     similarity_matrix = compute_similarity_matrix(preprocessed_sentences)
#     graph = nx.from_numpy_array(similarity_matrix)
#     scores = nx.pagerank(graph)
#     ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(preprocessed_sentences)),
#                               reverse=True)
#
#     summary_sentences = []
#     summary_length = len(ranked_sentences)
#     for i in range(summary_length):
#         summary_sentences.append(" ".join(ranked_sentences[i][1]))
#         if len(" ".join(summary_sentences)) > max_symbol:
#             break
#     summary = " ".join(summary_sentences)
#     return summary
