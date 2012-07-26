To parse the IOB files using NLTK's conll reader:
	
	import nltk
	root=u'/Users/56k/Documents/Research/CCH_PhD/ResearchProject/code/APh/experiments/postagged/'
	c = nltk.corpus.reader.conll.ConllCorpusReader(root, '.*\.iob',('words','pos','chunk'))
	c.sents()
	c.chunked_sents()
	len(c.chunked_sents())
	
Known problems:

* "A partir de" (in Spanish) get tokenised in the wrong way, leading nltk's Corpus to raise an error (inconsitent number of columns)
	* this is now solved but still I need to pass an abbreviation file to the tokeniser