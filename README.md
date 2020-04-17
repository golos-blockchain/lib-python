# Python GOLOS Library

This is a fork of [golodranets](https://github.com/steepshot/golodranets) GOLOS
library for Python which was forked from official STEEM library for Python. It
comes with a BIP38 encrypted wallet.

The main differences from the `steem-python`:

* directed to work with GOLOS blockchain
* websocket support
* convert Cyrillic to Latin for tags and categories
* Golos assets - `STEEM` -> `GOLOS`, `SBD` -> `GBG`, `VESTS` -> `GESTS`
* renamed modules - `steem` -> `golos`, `steemdata` -> `golosdata`
* for `Post` instance added two fields - `score_trending` and `score_hot`. This fields may be helpful if you want to sort your saved posts like `get_discussions_by_trending` and `get_discussions_by_trending` methods do. `reblogged_by` field is also filled now
* for `Account` instance methods `get_followers` and `get_following` were improved - now it takes `limit` and `offset` parameters

GOLOS HF 17-22 is supported.

# Installation

From source:

```
git clone https://github.com/bitfag/golos-python.git
cd golos-python
python3 setup.py install
```

## Homebrew Build Prereqs

If you're on a mac, you may need to do the following first:

```
brew install openssl
export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"
```

# Documentation

Unfortunately we do not have documentation for Golodranets yet, but documentation from steem-python may help you -  **http://steem.readthedocs.io**

# Tests

Some tests are included.  They can be run via:

* `python setup.py test`
