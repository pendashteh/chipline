# chipline
Console for ChatGPT

## Installation
1. Install python requirements (and obviousely python3!)
```
$ pip install -r requirements.txt
```

2. Place your API key at the root directory and call it `key`:
```
$ cat ./key
sk-I0j2C2Co...SjCz45
```

3. Make sure `console` is executable.
```
$ chmod +x ./console
```

## Run
### Console
```
$ cd /path/to/chipline
$ ./console
> 
```
Now you can prompt via the console.

### Direct python call
```
$ python chipline_openai.py [module] [prompt]
```
Available modules:
- chat
- grammar

**Example**:
```
$ python chipline_openai.py chat What is the oldest Empire?
```
