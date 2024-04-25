import re
import os

pattern = re.compile("(?<!= )(?<= )[a-zA-Z]+?(?=\()", re.I | re.M)
file = open("/workspace/webhcs/resources/hcs/src/structuredfindingmodule.h")
text = file.read()
file.close()

matches = re.findall(pattern, text)
print(matches)


def get_actual_function_name(line):
    for match in matches:
        if match in line:
            return re.sub(r"{.*?}", "{" + match + "}", line)

    return line


# get .dot file

dotfile = open(
    "/workspace/webhcs/resources/hcs/src/structuredfindingmodule.ll.callgraph.dot"
)
nodes_list = []
definition_node_regex = re.compile("(?<=\t).+?(?= \[)")
first_node_regex = re.compile("(?<=\t).+?(?= ->)")
second_node_regex = re.compile("(?<= -> ).+?(?=;)")

# collect node definitions
for line in dotfile:

    # check if line contains any structured finding method
    if any([match in line for match in matches]):
        # get the corresponding node of the method
        node = re.findall(definition_node_regex, line)

        # check if the node is not empty
        if len(node) > 0:
            nodes_list.append(node[0])


print(nodes_list)
print(len(nodes_list))
# remove all lines with nodes that are not in list
new_file_text = ""

dotfile.seek(0)
for line in dotfile:
    first_node = re.findall(first_node_regex, line)
    second_node = re.findall(second_node_regex, line)
    definition_node = re.findall(definition_node_regex, line)
    # write line if it's a connection between two nodes that are in the list
    if len(first_node) > 0 and len(second_node) > 0:
        if first_node[0] in nodes_list and second_node[0] in nodes_list:
            new_file_text += "\n" + line
    # write line if it's a node definition for a structured finding method
    elif len(definition_node) > 0 and definition_node[0] in nodes_list:
        new_file_text += "\n" + get_actual_function_name(line)


dotfile.close()


new_file = open("newfile.dot", "w")
new_file.write(
    f"""
digraph "Call graph: 'structuredfindingmodule.ll'" {{
label="Call graph: structuredfindingmodule.ll";

{new_file_text}
               
               
               }}"""
)

os.system("dot -Tpng -O -v newfile.dot")
