import hashlib,json
from collections import OrderedDict
class My_MerkTree:

	def __init__(self,listoftransaction=None):
		self.listoftransaction = listoftransaction
		self.past_transaction = []

	def create_tree(self):

		listoftransaction = self.listoftransaction
		past_transaction = self.past_transaction
		temp_transaction = []
		tempDict = OrderedDict()

		for index in range(0,len(listoftransaction),2):
			current = listoftransaction[index]

			if index+1 != len(listoftransaction):
				current_right = listoftransaction[index+1]
			else:
				current_right = current

			current_hash = hashlib.sha256(hashlib.sha256(current.encode('utf-8')).hexdigest().encode('utf-8'))
			current_right_hash = hashlib.sha256(hashlib.sha256(current_right.encode('utf-8')).hexdigest().encode('utf-8'))

			tempDict[listoftransaction[index]] = current_hash.hexdigest()

			if index+1 != len(listoftransaction):
				tempDict[listoftransaction[index+1]] = current_right_hash.hexdigest()

			temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())
		past_transaction.append(tempDict)

		if len(listoftransaction) != 1:
			self.listoftransaction = temp_transaction
			self.past_transaction = past_transaction
			self.create_tree()

	def get_past_transaction(self):
		return self.past_transaction

	def get_root_leaf(self):
		last_key = list(self.past_transaction[-1].keys())[-1]
		return self.past_transaction[-1][last_key]

# Declare the main part of the function to run
if __name__ == "__main__":

	# a) Create the new class of My_MerkTree
	My_Tree = My_MerkTree()

	# b) Give list of transaction
	transaction = ['a','b','c','d']

	# c) pass on the transaction list 
	My_Tree.listoftransaction = transaction

	# d) Create the Merkle Tree transaction
	My_Tree.create_tree()

	# e) Retrieve the transaction 
	past_transaction = My_Tree.get_past_transaction()

	# f) Get the last transaction and print all 
	print ("First Example - Even number of transaction Merkel Tree")
	print ('Final root of the tree : ',My_Tree.get_root_leaf())
	print(json.dumps(past_transaction, indent=4))
	print ("-" * 50 )

	# h) Second example
	print ("Second Example - Odd number of transaction Merkel Tree")
	My_Tree = My_MerkTree()
	transaction = ['a','b','c','d','e']
	My_Tree.listoftransaction = transaction
	My_Tree.create_tree()
	past_transaction = My_Tree.get_past_transaction()
	print ('Final root of the tree : ',My_Tree.get_root_leaf())
	print(json.dumps(past_transaction, indent=4))
	print ("-" * 50 )

	# i) Actual Use Case
	print ("Final Example - Actuall use case of the Merkle Tree")

	# i-1) Declare a transaction - the ground truth
	ground_truth_Tree = My_MerkTree()
	ground_truth_transaction = ['a','b','c','d','e']
	ground_truth_Tree.listoftransaction = ground_truth_transaction
	ground_truth_Tree.create_tree()
	ground_truth_past_transaction = ground_truth_Tree.get_past_transaction()
	ground_truth_root = ground_truth_Tree.get_root_leaf()

	# i-2) Declare a tampered transaction
	tampered_Tree = My_MerkTree()
	tampered_Tree_transaction = ['a','b','c','d','f']
	tampered_Tree.listoftransaction = tampered_Tree_transaction
	tampered_Tree.create_tree()
	tampered_Tree_past_transaction = tampered_Tree.get_past_transaction()
	tampered_Tree_root = tampered_Tree.get_root_leaf()

	# i-3) The three company share all of the transaction 
	print ('Company A - my final transaction hash : ',ground_truth_root)
	print ('Company B - my final transaction hash : ',ground_truth_root)
	print ('Company C - my final transaction hash : ',tampered_Tree_root)

	# i-4) Print out all of the past transaction
	print ("\n\nGround Truth past Transaction ")
	print(json.dumps(ground_truth_past_transaction, indent=4))
	
	print ("\n\nTamper Truth past Transaction ")
	print(json.dumps(tampered_Tree_past_transaction, indent=4))





# ---- END OF THE CODE ------