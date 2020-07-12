# NoSQL namespace mocking
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Intro
`nsqlns` generates sub-namespace and keys by overloading some operators,
managing namespace in a unix-path-like manner.

## Usage
```
# Import module:
import nsqlns

# Create a instance with default delimiter(colon):
root_node = nsqlns.NsqlNamespace("root", delim=":")

# Turn instance into string key:
str_key = str(root_node)
# -> "root"

# Just generate a string key:
str_key_direct = root_node > "key"
# -> "root:key"

# Concat other sub namespace:
sub_node = root_node / nsqlns.NsqlNamespace("sub")
# or:
# sub_node = root_node / "sub"
# Turn it into key:
sub_key = str(sub_node)
# -> "root:sub"

# Using different delimiter.
# The `delim` keyword parameter determines the delimiter used in
# node concatenation, note that string concatenate inherites the delimiter
# of parent node.
sub_node2 = sub_node/nsqlns.NsqlNamespace("sub2", delim=">")
sub_key2 = str(sub_node2/"leaf")
# -> "root:sub:sub2>leaf"

```

## License
`nsqlns` is distributed under MIT license.
