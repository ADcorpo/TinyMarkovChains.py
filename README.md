#TinyMarkovChains

This is a small python module providing a Markov chain text generator.

## Usage

```
from markov import MarkovChain

generator = MarkovChain()
# instanciating the generator

generator.train("GNU/Linux is an operatig system")
generator.train("Here is an ice cream")
# Training the generator with sample sentences

print(generator.talk())
# Output: GNU/Linux is an ice cream
```

## Interest

Uhh…
