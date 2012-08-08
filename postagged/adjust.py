from citation_extractor.Utils import aph_corpus
from citation_extractor.Utils import IO
import glob
import os

collections = [
			#"C2"
			#,"C1"
			#,"eff_cand_1_a"
			#,"eff_cand_1_b"
			#,"eff_cand_2_a"
			#,"eff_cand_2_b"
			#,"eff_cand_3_a"
			#,"eff_cand_3_b"
			#,"eff_cand_4_a"
			#,"eff_cand_5_a"
			#,"eff_cand_6_a"
			#,"eff_cand_6_b"
			#,"eff_cand_7"
			#,"eff_cand_8"
			#,"eff_cand_9"
			"eff_cand_10"
			]

base_dir = "/Users/56k/phd/code/APh/corpus/by_collection/"
base_url = "http://cwkb.webfactional.com/aph_corpus/collections/"
base_new_dir = "/Users/56k/phd/code/APh/corpus/postagged/"

directories = ["%s%s/"%(base_dir,collection) for collection in collections]
urls = ["%s%s/"%(base_url,collection) for collection in collections]
failed = []
print urls,directories

for n,directory in enumerate(directories):
	file_id_mappings = IO.scan_iob_files(directory)
	collections_details = aph_corpus.get_collection_details([urls[n]])
	print collections_details
	print file_id_mappings
	print directory
	for infile in glob.glob( os.path.join(directory, '*.iob') ):
		try:
			dir = os.path.split(infile)[0]
			fname = os.path.split(infile)[1]
			newdir = "%s%s/"%(base_new_dir,collections[n])
			print newdir
			print infile
			print fname,file_id_mappings[fname]
			print collections_details["lang"][file_id_mappings[fname]]
			if not os.path.exists(newdir):
			    os.makedirs(newdir)
			aph_corpus.reformat_iob(infile,"%s/aph_corpus%s.iob"%(newdir,file_id_mappings[fname]),collections_details["lang"][file_id_mappings[fname]])	
		except Exception, e:
			print e
			failed.append(infile)
print failed

