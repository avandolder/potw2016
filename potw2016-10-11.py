# potw2016-10-11.py
# author: Adam Vandolder
# Validates a series of IP addresses in constant time using Python 3 dictionaries.

import sys

def main(args):
	banned_ips = {}
	output_list = []
	
	for i in range(int(input())):
		# Split the input IP address into a list of integers.
		ip = [int(x) for x in input().split('.') if x.isdigit()]
		
		# Set the first element of the banned IP as a key of the dictionary.
		banned_ips[ip[0]] = {}
		bip = banned_ips[ip[0]]
		
		for j in range(1, len(ip)):
			# Loop through and set any subsequent elements to keys of the
			# inner dictionaries.
			bip[ip[j]] = {}
			bip = bip[ip[j]]
			
	for i in range(int(input())):
		# Split the input IP address into a list of integers.
		ip = [int(x) for x in input().split('.') if x.isdigit()]
		
		bip = banned_ips
		banned = True
		for j in range(len(ip)):
			# Loop through the elements of the IP address.
			if ip[j] not in bip:
				# If the element is not a key of the banned IP dictionary,
				# then the IP is valid.
				banned = False
				break
			elif len(bip[ip[j]]) == 0:
				# If every element of the IP has been a key in a banned
				# ditionary so far, and there is no more inner dictionaries,
				# then the IP is invalid.
				break
				
			bip = bip[ip[j]]
		
		if banned:
			output_list.append('banned')
		else:
			output_list.append('valid')
	
	[print(x) for x in output_list]

if __name__ == '__main__':
	sys.exit(main(sys.argv))
