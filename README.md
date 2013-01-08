# pickleBase64
A really, admittedly, lazy interface into Python for pickling/unpickling an object, based on Matt Robenolt's node_pickle
The interface mimics Python's pickle.dumps & pickle.loads.

node_pickle seems to have some trouble when trying to unpickle an string containing non-ascii chars after base64 deserialization, so the base64 raw string is passed into the converter.


## Usage
```javascript
var pickle = require('pickle');

pickle.dumps({hello: "world"}, function(pickled) {
  console.log("pickled:", pickled);
  pickle.loads(pickled, function(original) {
    console.log("original:", original);
  });
});
```

## License 

(The MIT License)

Copyright (c) 2011 Matt Robenolt &lt;root@drund.com&gt;
Copyright (c) 2012 Pablo Casado &lt;p.casado.arias@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
