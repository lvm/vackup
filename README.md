# youtube-dl front end

Or _vackup_ (Video bACKUP).

## what

An over-engineered solution to download _movies_ from Youtube (and the other platforms supported by `youtube-dl`) directly to my raspberry-pi, because I found tiresome to `ssh` to it to download something when using my phone.

## components

* flask app, listening on port 5000
* celery
* redis
* flower (to monitor tasks), listening on port 5555

## how to run

Make sure you've modified `docker-compose.yml` to match your directory where you store your videos, then:

```
git clone https://github.com/lvm/vackup \
    && cd vackup \
    && docker-compose up --build -d
```

Yes, you need to have docker (18.09+) and docker-compose (1.24+).

## license

yes.
