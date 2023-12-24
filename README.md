# e6-pool-monitor
Ever wanted to be notified when a new page is added to a pool on e621.net? This is the program for you! Ready for easy Docker deployment!

Easily interfaces with a Discord bot as a frontend with slash commands and embeds.

Built on Python 3.11

## Credits
[Check out the open source libraries used in this project!](/CREDITS.md)


## Installation
### Docker
`TBD`

### Environment Variables
| Variable | Description | Default |
| --- | --- | --- |
| `LOGGING_LEVEL` | Logging Level. Can be `debug` or `info` | `info` |
| `E621_USERNAME` | Username for e621.net. This must be set as it is required for generating a UserAgent string. Read more [here](https://e621.net/help/api)| `None` |