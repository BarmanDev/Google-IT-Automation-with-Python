import re

log = "Juli 31 07:41:48 mycomputer bad_process[12321]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(
    regex, "A completely different string that also has numbers [34567]")
print(result)


def extract_pid(log_line):
    regex = r"\[(\d) \]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]


print(extract_pid(log))
