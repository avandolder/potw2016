class Gene(object):
	def __init__(self, seq):
		self._seq = seq
		self._siblings = []
	
	def get_seq(self):
		return self._seq
	
	def add_sibling(self, sibling):
		if sibling not in self._siblings:
			self._siblings += [sibling]
			sibling.add_sibling(self)

	def get_siblings(self):
		return self._siblings
	
	def is_sibling(self, gene):
		seq = gene.get_seq()
		chars_off = 0
		
		for i in range(4):
			if self._seq[i] != seq[i]:
				chars_off += 1
		
		if chars_off > 1:
			return False
		else:
			return True

def any_genes_unprocessed(g, passed, genes):
	for s in g.get_siblings():
		if genes[s] not in passed:
			return True
			
	return False
			
start_seq = input()
start_gene = None
genes = {}

for i in range(int(input())):
	new_seq = input()
	new_gene = Gene(new_seq)
	
	if new_seq == start_seq:
		start_gene = new_gene
	
	for g in genes:
		if g.is_sibling(new_gene):
			g.add_sibling(new_gene)
	
	genes[new_gene] = len(dict)

# List out all genes and their siblings.
for g in genes:
	print("Gene", g.get_seq())
	
	for s in g.get_siblings():
		print("\tsibling:", s.get_seq())

mutations_to_geek = -1
passed_genes = []
curr_gene = start_gene

while any_genes_unprocessed(start_gene, passed_genes, genes):
	siblings = curr_gene.get_siblings()
	
	
