import json

with open('/mnt/data/gtm-01-and-07.json', 'r') as file:
    gtm_01_and_07 = json.load(file)

with open('/mnt/data/leadForm2.json', 'r') as file:
    leadForm2 = json.load(file)

gtm_01_and_07['containerVersion']['folder'].extend(leadForm2['containerVersion']['folder'])

gtm_01_and_07['containerVersion']['variable'].extend(leadForm2['containerVersion']['variable'])

gtm_01_and_07['containerVersion']['tag'].extend(leadForm2['containerVersion']['tag'])

gtm_01_and_07['containerVersion']['trigger'].extend(leadForm2['containerVersion']['trigger'])

output_path = '/mnt/data/combined_container.json'
with open(output_path, 'w') as file:
    json.dump(gtm_01_and_07, file)

print(f"json: {output_path}")
