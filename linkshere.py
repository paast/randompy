import requests



test_url = ('https://en.wikipedia.org/w/api.php?' + 
	'action=query&prop=linkshere&titles=Facebook' + 
	'&lhnamespace=0&lhlimit=max&lhprop=title' + 
	'&format=json&formatversion=2')


def load_lh(url):

	r_set = set({})
	temp = requests.get(url).json()
	if 'continue' in temp:
		cont_param = '&lhcontinue=' + temp['continue']['lhcontinue']
		r_set |= load_lh(url + cont_param)
	if 'linkshere' in temp['query']['pages'][0]:
		for link in temp['query']['pages'][0]['linkshere']:
			r_set.add(link['title'])
	return r_set

def main():
	print(len(load_lh(test_url)))



# ~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__": main()