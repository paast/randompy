from slackclient import SlackClient
import os
import json


def unpack(client, channel, start=""):
	"""Retrieves the entire message
	history of channel (string id
	e.g. 'CXXXXXXXX').

	'start' parameter used for
	internal recursion.

	Returns in list, ordered by
	timestamp from most to least recent."""

	hold = []

	chunk = client.api_call("channels.history",
		channel=channel,
		count="1000",
		latest=start)

	for message in chunk['messages']:
		if 'subtype' not in message:
			hold.append(message['text'])

	print('+', len(hold))

	if (chunk['has_more'] == True):
		start = chunk['messages'][-1]['ts']
		hold += unpack(client, channel, start)

	return hold


def main():

	channel_id = 'C6928G0MA'

	AUTH_TOKEN = os.environ['AUTH']
	sc = SlackClient(AUTH_TOKEN)

	test = json.dumps(unpack(sc, channel_id))

	file = open(channel_id + "-dump.json", "w")
	file.write(test)
	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__": main()
