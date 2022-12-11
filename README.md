# Semantic-Analysis-of-Mahabhrat
The project aims at semantically analyzing the Mahabharat text to
extract interesting insights based on the characters and events. Mahabharat involves a wide array of characters, hence identifying all the characters present
in the text using Named Entity Recognition plays a vital role in the semantic analysis. After identifying the characters, some interesting insights on the characters
can be obtained by extracting the relationships between the different entities. Further analysis on various events is performed to allow a better and comprehensive
understanding of the identified events. We also represent the data by fitting it into templates, which allows easy comparison between different events of the
same type such as different swayamvaras.
The project consists of two phases:
### The entity analysis phase:
  + Identification of Named Entities pertaining to Mahabharat text such as names,
  places, communities, weapons and was strategies, literature and art, events.
  + Training a model to identify the above mentioned entities.
  + Relationship Extraction between two entities using RoBERTa.
  + Identifying count of each entity types in the text.
  + Visualizing graphically the interrelationships between characters with maximum
  frequency.
  + Visualizing graphically the interrelationships between characters with highest
  centralities.
### The event analysis phase:
+ Identification of the event sections in the text.
+ Summarizing the events identified using BART model.
+ The summary obtained is given as context for automatically answering frequently
asked questions using the whole word masking BERT model.
+ Insights of the events are visualized in the form of line and semantic graphs.
