import json

commit_message = '''[NullAway] dereferenced expression failure is @Nullable
new DecodingException("Failed to decode: " + failure.getMessage(), failure));
^'''

# Automatically escape quotes and other characters
escaped_commit_message = json.dumps(commit_message)

print(escaped_commit_message)
