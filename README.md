# Open Notify API (python)

Open Nofity API client for python

> Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data.

For other languages, see [Open Notify API clients](https://github.com/iArmanKarimi/Open-Notify-API-clients)

## Installation

```bash

```

## Examples

Create an instance of OpenNotify:

```python
open_notify = OpenNotify()
```

Number of People in Space:

```python
iss_location = open_notify.get_ISS_location()
print("ISS location:")
print("latitude:", iss_location.location.latitude)
print("longitude:", iss_location.location.longitude)
```

Current Location of the International Space Station:

```python
people_in_space = open_notify.get_people_in_space()
for people in people_in_space.people:
    print(f"craft: {people.craft}, name: {people.name}")
```

## References

[Open Notify Website](http://open-notify.org/)

[Official API documentation](http://open-notify.org/Open-Notify-API/)

## License

[MIT](https://github.com/iArmanKarimi/Open-Notify-API-python/blob/main/LICENSE)
