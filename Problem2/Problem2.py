import json


def remove_json_ele(ele):
    f = open('Problem2/test_payload.json', )
    data = json.load(f)

    try:
        del data[ele]
    except:
        for key, value in data.items():
            if ele in value:
                value.pop(ele)
                break

    with open("Problem2/output.json", "w") as outfile:
        json.dump(data, outfile)

    # Closing file
    f.close()
