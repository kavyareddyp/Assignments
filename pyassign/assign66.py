for line_str in open("myfile"):
    line_obj = json.loads(line_str)
    if "ERROR" in line_obj:
        print line_obj
