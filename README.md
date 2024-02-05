# Anchor

Simple ANSI CLI parts.

License: MIT - See the `LICENSE` file. 

### Sample usage

```py
import anchor

anchor.FONT_COLOR = anchor.COLOR.CYAN

anchor.banner('Hello, **world!**\nThis is Anchor!')

name = anchor.entry("What's your name? >")
anchor.banner(f"Great, $RED({name})! What's your favorite color?")

colors = ['Red', 'Blue', 'Green', 'Yellow', 'White']
color = colors[ anchor.select_large(colors) ]
anchor.FONT_COLOR = anchor.COLOR.get(color)

anchor.banner(f'**{color}!** I love that color too! ^^')
```
